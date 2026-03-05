# 💬 Real-time Chat Application (Docker)

## 📋 คำอธิบาย

โปรเจกต์นี้เป็นแอปพลิเคชันแชตแบบ Real-time ที่ทำงานโดยใช้ Docker ช่วยในการจัดการและการรัน โปรแกรมได้อย่างรวดเร็ว มีการส่งข้อความแบบ Real-time ผ่าน WebSocket และจัดเก็บข้อความลงในฐานข้อมูล MySQL พร้อมให้ผู้ใช้ดูประวัติการแชตสามารถสำหรับจัดเก็บไว้

---

## 🏗️ สถาปัตยกรรมโครงการ

โปรเจกต์นี้ประกอบด้วย 4 Service หลัก:

```
chat-docker/
├── docker-compose.yml      # Docker Compose Configuration
├── Dockerfile              # Backend Docker Image
├── backend/
│   ├── main.py             # FastAPI Application
│   └── requirements.txt     # Python Dependencies
├── database/
│   └── init.sql            # Database Initialization Script
├── frontend/
│   ├── index.html          # Chat Interface (HTML)
│   └── style.css           # Styling
└── README.md               # This file
```

---

## 🚀 การติดตั้งและการรัน

### ✅ ข้อกำหนดเบื้องต้น

- Docker Desktop (หรือ Docker + Docker Compose)
- Windows, Mac, หรือ Linux

### 📦 ขั้นตอนการติดตั้ง

1. **Clone หรือ Download โปรเจกต์**
   ```bash
   cd c:\Users\yadak\Desktop\MiniProject\chat-docker
   ```

2. **เริ่มต้น Docker Compose**
   ```bash
   docker-compose up -d
   ```
   
   ตัวเลือกเพิ่มเติม:
   - `docker-compose up` - แสดง Logs ในหน้าจอ
   - `docker-compose up -d` - รันเบื้องหลัง
   - `docker-compose down` - ปิดทุก Service

3. **รอให้ Services เริ่มต้นจนเสร็จ** (ประมาณ 10-15 วินาที)

---

## 🌐 การเข้าถึงแอปพลิเคชัน

เมื่อทุก Service เริ่มต้นแล้ว สามารถเข้าถึงได้ที่:

| Service | URL | คำอธิบาย |
|---------|-----|---------|
| Frontend (Chat) | http://localhost:80 | หรือ http://localhost | ร้านการแชตหลัก |
| Backend API | http://localhost:8000 | FastAPI Server |
| History API | http://localhost:8000/history | ดึงประวัติการแชต |
| PhpMyAdmin | http://localhost:8080 | ระบบจัดการฐานข้อมูล |

---

## 🌍 การเข้าถึงจากภายนอกด้วย Ngrok

หากต้องการให้คนอื่นเข้าห้องแชทได้จากอินเทอร์เน็ต สามารถใช้ Ngrok เพื่อสร้าง Public URL:

### 📦 ขั้นตอนการใช้ Ngrok

1. **ติดตั้ง Ngrok** (ถ้ายังไม่มี):
   - ดาวน์โหลดจาก [ngrok.com](https://ngrok.com/download)
   - สมัครบัญชีและรับ Auth Token

2. **ตั้งค่า Auth Token**:
   ```bash
   ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```

3. **เริ่ม Docker Compose**:
   ```bash
   docker-compose up -d
   ```

4. **รัน Ngrok** ใน Terminal ใหม่:
   ```bash
   ngrok http 80
   ```

5. **คัดลอก Public URL** จาก Ngrok และส่งให้เพื่อน:
   - ตัวอย่าง: `https://abc123.ngrok.io`
   - เพื่อนสามารถเข้าห้องแชทได้ที่ URL นี้ และคุยกันแบบ Real-time

**⚠️ หมายเหตุ**:
- Ngrok URL จะเปลี่ยนทุกครั้งที่รันใหม่ (เว้นแต่ใช้ Paid Plan)
- ห้องแชทนี้เป็นห้องเดียวสำหรับทุกคนที่เข้าห้องเดียวกัน
- ตรวจสอบให้แน่ใจว่า Firewall อนุญาต Port 80

## 🔧 รายละเอียด Services

### 1️⃣ **Backend (FastAPI + Python)**
- **Port**: 8000
- **หน้าที่**:
  - จัดการ WebSocket Connections
  - ส่งข้อความแบบ Real-time (Broadcast)
  - บันทึกข้อความลงฐานข้อมูล
  - ให้บริการ API เพื่อดึงประวัติการแชต

**Endpoints**:
```
WebSocket: ws://localhost:8000/ws
GET: /history
```

### 2️⃣ **Database (MySQL)**
- **Port**: 3306
- **ชื่อฐานข้อมูล**: `chatdb`
- **Username**: `root`
- **Password**: `root`

**Table Structure**:
```sql
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT,
    time DATETIME
);
```

### 3️⃣ **PhpMyAdmin**
- **Port**: 8080
- **URL**: http://localhost:8080
- **Username**: `root`
- **Password**: `root`
- ใช้สำหรับการจัดการฐานข้อมูลผ่าน Web Interface

### 4️⃣ **Frontend (Nginx)**
- **Port**: 80
- **หน้าที่**: เสิร์ฟไฟล์ HTML, CSS, JavaScript
- **Technology**:
  - HTML5 สำหรับ Structure
  - CSS3 สำหรับ Styling (Gradient Design)
  - JavaScript สำหรับ WebSocket Client

---

## 💻 วิธีการใช้งานแอปพลิเคชัน

1. **เปิดเบราว์เซอร์** และไปที่ http://localhost

2. **หน้าจอแชต** จะแสดงขึ้นมา:
   - ส่วน Header: กำหนดชื่อแอปพลิเคชัน
   - ส่วนแชต: แสดงข้อความทั้งหมด (ประวัติ + Real-time)
   - ส่วน Input: พื้นที่พิมพ์ข้อความ

3. **ส่งข้อความ**:
   - พิมพ์ข้อความในช่อง Input
   - คลิกปุ่ม "Send" หรือกด Enter
   - ข้อความจะปรากฏทันทีและส่งไปยังผู้ใช้คนอื่น (ถ้ามี)

4. **อ่านประวัติ**:
   - เมื่อเปิดแอปพลิเคชัน จะโหลดประวัติการแชตทั้งหมดจากฐานข้อมูล

---

## 🔄 วิธีการทำงาน (Workflow)

### ขั้นตอนการส่งข้อความ:

```
┌─────────────┐
│   Client 1  │ (พิมพ์ข้อความ)
└──────┬──────┘
       │
       ├─→ WebSocket: ws://localhost:8000/ws
       │
       ├─→ FastAPI Backend
       │   ├─→ นำข้อความไปส่ง (Broadcast) ให้คลายเอนต์อื่น ๆ
       │   └─→ บันทึกข้อความลงตาราง messages
       │
       ├─→ MySQL Database
       │   └─→ INSERT INTO messages (content, time) VALUES (...)
       │
       └─→ ตัวอักษรข้อความจะปรากฏบนหน้าจอ Client ทั้งหมด
```

### ขั้นตอนการโหลดประวัติ:

```
┌─────────────┐
│   Client    │ (เปิดแอป)
└──────┬──────┘
       │
       ├─→ GET: http://localhost:8000/history
       │
       ├─→ FastAPI Backend
       │   └─→ SELECT content, time FROM messages
       │
       ├─→ MySQL Database
       │   └─→ ดึงข้อมูลทั้งหมดมาเรียงลำดับ
       │
       └─→ แสดงประวัติการแชตบนหน้าจอ
```

---

## 🎨 UI/UX Features

- **Design**: Modern Gradient Background (Purple to Blue)
- **Chat Container**: 400px × 600px (Responsive-friendly)
- **Message Bubble**:
  - ข้อความของฉัน: (ด้านขวา สีม่วง)
  - ข้อความอื่น: (ด้านซ้าย สีขาว)
- **Auto-scroll**: จอแชตเลื่อนลงโดยอัตโนมัติเมื่อมีข้อความใหม่

---

## 📝 File Descriptions

### `docker-compose.yml`
รวมทั้ง 4 Services:
- `backend`: FastAPI Application
- `db`: MySQL Database
- `phpmyadmin`: Database Management
- `frontend`: Nginx Static Serve

### `Dockerfile`
- Base Image: `python:3.10`
- Copy backend folder
- Install requirements
- Run: `uvicorn main:app --host 0.0.0.0 --port 8000`

### `backend/main.py`
FastAPI Application ที่มี:
- WebSocket Endpoint: `/ws`
- GET Endpoint: `/history`
- CORS Middleware

### `backend/requirements.txt`
```
fastapi          - Web framework
uvicorn          - ASGI server
mysql-connector-python - Database connector
```

### `database/init.sql`
สร้างฐานข้อมูลและตาราง

### `frontend/index.html` + `frontend/style.css`
Web Interface สำหรับการแชต

---

## 🛠️ การ Debug และ Troubleshooting

### ❌ ปัญหา: ไม่สามารถเชื่อมต่อกับฐานข้อมูล

**สาเหตุ**: MySQL ยังไม่พร้อม
```bash
# วิธีแก้ไข: รอสักครู่แล้ว refresh หน้าเบราว์เซอร์
# หรือ ดูว่า Container ทำงานหรือไม่
docker-compose ps
```

### ❌ ปัญหา: WebSocket Connection Failed

**สาเหตุ**: Backend ไม่ได้รัน
```bash
# วิธีแก้ไข: ตรวจสอบ logs
docker-compose logs backend
```

### ❌ ปัญหา: Frontend ไม่โหลด

**สาเหตุ**: Nginx ไม่ได้ serve ไฟล์
```bash
# วิธีแก้ไข: ตรวจสอบ logs
docker-compose logs frontend
```

### 📊 ดูสถานะของทุก Containers

```bash
docker-compose ps
```

### 🔍 ดู Logs ของ Service ใดนึ่ง

```bash
docker-compose logs backend          # Backend logs
docker-compose logs db               # MySQL logs
docker-compose logs frontend         # Nginx logs
docker-compose logs phpmyadmin       # PhpMyAdmin logs
```

---

## 🔐 ข้อมูลเข้าสู่ระบบ

| Service | Username | Password |
|---------|----------|----------|
| MySQL | root | root |
| PhpMyAdmin | root | root |

> ⚠️ **หมายเหตุ**: สำหรับการใช้งานการพัฒนา (Development) เท่านั้น ⚠️

---

## 🗑️ การปิดแอปพลิเคชัน

### ปิด Services พร้อมลบ Containers

```bash
docker-compose down
```

### ปิด Services แต่เก็บ Volumes (ข้อมูลยังอยู่)

```bash
docker-compose down -v
```

### ปิด Services เพียงเท่านั้น (Containers ยังอยู่)

```bash
docker-compose stop
```

### เริ่มต้อม Services ใหม่

```bash
docker-compose start
```

---

## 📚 Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| Backend | FastAPI (Python) |
| Real-time | WebSocket |
| Database | MySQL 8 |
| Container Orchestration | Docker Compose |
| Admin Panel | PhpMyAdmin |
| Web Server | Nginx |

---

## 🎯 Features

✅ Real-time Messaging via WebSocket  
✅ Chat History Persistence  
✅ Multi-client Support  
✅ Automatic Retry (Database Connection)  
✅ CORS Middleware Enabled  
✅ Docker Containerized  
✅ Database Management UI (PhpMyAdmin)  
✅ Responsive Design  
✅ Auto-scroll Chat  
✅ Enter Key to Send Message  

