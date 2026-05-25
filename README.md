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
├── DataFluxPLC/        # TwinCAT project
└── python/             # Python services
    ├── read_plc.py     # ADS data reader
    └── database.py     # Database setup

## Status
🚧 In active development — learning project.
