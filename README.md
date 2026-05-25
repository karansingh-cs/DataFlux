# DataFlux

An open-source industrial edge automation platform built on Beckhoff TwinCAT 3.

Bridges real-time PLC data to databases, web dashboards, and CI/CD deployment pipelines — 
without expensive middleware or SCADA licensing.

---

## What This Project Builds

This project is built in phases, each adding a new capability on top of the last:

- **Phase 1 — Data Pipeline**: Extract live PLC data via ADS protocol into a local database
- **Phase 2 — Database Storage**: Store and query historical machine data using SQLite
- **Phase 3 — Live Dashboard**: Web-based real-time HMI using FastAPI and WebSockets
- **Phase 4 — Code Generation**: Auto-generate TwinCAT Function Blocks from a device spreadsheet
- **Phase 5 — CI/CD Pipeline**: Git-managed automated deployment for TwinCAT projects (upcoming)
- **Phase 6 — Docker**: Containerize all Python services for deployment on real IPCs (upcoming)
- **Phase 7 — OPC-UA**: Industry standard data exchange protocol (upcoming)
- **Phase 8 — MQTT**: Edge-to-cloud messaging (upcoming)

---

## Tech Stack
- TwinCAT 3 (IEC 61131-3 Structured Text)
- Python (pyads, FastAPI, SQLite/PostgreSQL)
- Docker
- GitHub Actions

---

## Project Structure
DataFlux/
├── DataFluxPLC/              # TwinCAT project
└── python/                   # Python services
├── config.py             # Central config — AmsNetId, DB path, folder paths
├── database.py           # Creates the SQLite database and table
├── logger.py             # Reads PLC data every second and writes to database
├── query.py              # Quick terminal viewer for last 10 database rows
├── server.py             # FastAPI server — serves dashboard and WebSocket
├── dashboard.html        # Live browser dashboard — real-time + history
├── generate.py           # Generates TwinCAT Function Blocks from CSV
├── devices.csv           # Device I/O list — source of truth for code generation
├── templates/            # Jinja2 XML templates for TwinCAT POUs
│   └── MotorControl.tcpou
└── generated/            # Output folder — generated .TcPOU files ready to import

---

## Dependencies
- pyads — ADS protocol communication with TwinCAT
- fastapi — web server and WebSocket backend
- uvicorn — runs the FastAPI server
- websockets — WebSocket support
- jinja2 — XML templating for code generation
- openpyxl — Excel file reading (upcoming)

Install all at once:
pip install pyads fastapi uvicorn websockets jinja2 openpyxl

---

## How to Run

**First time only — create the database:**
python database.py

**Start the data logger** (keep this running in its own terminal):
python logger.py

**Start the web server** (open a second terminal):
python -m uvicorn server:app --reload

**Open the dashboard in your browser:**
http://localhost:8000

**Generate TwinCAT Function Blocks from device list:**
python generate.py
Then import the files from `python/generated/` into your TwinCAT POUs folder.

---

## Why Each File Exists
- **config.py** — single place to change AmsNetId or DB path, no hunting through files
- **database.py** — sets up the table structure before anything else runs
- **logger.py** — the core data pipeline, runs continuously in background
- **query.py** — quick sanity check to verify data is actually being logged
- **server.py** — exposes the data over HTTP and WebSocket for the browser
- **dashboard.html** — zero-framework UI, no React or Node needed
- **generate.py** — reads devices.csv and generates TwinCAT Function Blocks automatically
- **devices.csv** — the I/O list, single source of truth for all device definitions
- **templates/MotorControl.tcpou** — Jinja2 XML template, defines the structure of every generated Motor FB
- **generated/** — output folder, copy these .TcPOU files directly into TwinCAT

---

## Status
- [x] Phase 1 — Data Pipeline
- [x] Phase 2 — Database Storage
- [x] Phase 3 — Live Dashboard
- [x] Phase 4 — Code Generation
- [ ] Phase 5 — CI/CD Pipeline
- [ ] Phase 6 — Docker
- [ ] Phase 7 — OPC-UA
- [ ] Phase 8 — MQTT