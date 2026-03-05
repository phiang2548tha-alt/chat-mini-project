from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from datetime import datetime
import time


app = FastAPI()
clients = []

# รอ MySQL พร้อมก่อน
for i in range(10):
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="chatdb"
        )
        print("DB connected")
        break
    except:
        print("Waiting for DB...")
        time.sleep(2)

cursor = db.cursor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    clients.append(ws)

    try:
        while True:
            data = await ws.receive_text()

            # ส่ง real-time
            for client in clients:
                await client.send_text(data)

            # save ลง DB
            cursor.execute(
                "INSERT INTO messages (content, time) VALUES (%s, %s)",
                (data, datetime.now())
            )
            db.commit()

    except WebSocketDisconnect:
        clients.remove(ws)

@app.get("/history")
def get_history():
    cursor.execute("SELECT content, time FROM messages ORDER BY id ASC")
    return cursor.fetchall()