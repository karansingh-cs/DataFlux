# DataFlux

An open-source industrial edge automation platform built on Beckhoff TwinCAT 3.

Bridges real-time PLC data to databases, web dashboards, and CI/CD deployment pipelines — 
without expensive middleware or SCADA licensing.

## What This Project Builds
- Live PLC data extraction via ADS protocol
- Local database storage (SQLite → PostgreSQL)
- Web-based real-time HMI dashboard (FastAPI + WebSockets)
- Automated TwinCAT code generation from spreadsheets
- Git-managed CI/CD pipeline for industrial deployments

## Tech Stack
- TwinCAT 3 (IEC 61131-3 Structured Text)
- Python (pyads, FastAPI, SQLite/PostgreSQL)
- Docker
- GitHub Actions

## Project Structure
DataFlux/
├── DataFluxPLC/          # TwinCAT project
└── python/               # Python services
    ├── config.py         # Central config — AmsNetId, DB path
    ├── database.py       # Creates the SQLite database and table
    ├── logger.py         # Reads PLC data every second and writes to database
    ├── query.py          # Quick terminal viewer for last 10 database rows
    ├── server.py         # FastAPI server — serves dashboard and WebSocket
    └── dashboard.html    # Live browser dashboard — real-time + history

## How to Run
1. Open TwinCAT, activate configuration, run in simulation mode
2. Create the database (first time only):
   python database.py
3. Start the data logger (keep running):
   python logger.py
4. Start the web server (separate terminal):
   python -m uvicorn server:app --reload
5. Open browser at http://localhost:8000

## Why Each File Exists
- **config.py** — single place to change AmsNetId or DB path, no hunting through files
- **database.py** — sets up the table structure before anything else runs
- **logger.py** — the core data pipeline, runs continuously in background
- **query.py** — quick sanity check to verify data is actually being logged
- **server.py** — exposes the data over HTTP and WebSocket for the browser
- **dashboard.html** — zero-framework UI, no React or Node needed

## Status
🚧 In active development — learning project.