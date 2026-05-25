import pyads
import sqlite3
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse, JSONResponse
from config import AMS_NET_ID, DB_PATH

app = FastAPI()

# PLC connection
plc = pyads.Connection(AMS_NET_ID, pyads.PORT_TC3PLC1)
plc.open()

# HTML dashboard served at http://localhost:8000
@app.get('/')
def dashboard():
    with open('dashboard.html') as f:
        return HTMLResponse(f.read())

# WebSocket endpoint — browser connects here for live data
@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Read from PLC
            conveyor_running = plc.read_by_name('MachineData.ConveyorRunning', pyads.PLCTYPE_BOOL)
            motor_temp       = plc.read_by_name('MachineData.MotorTemp',       pyads.PLCTYPE_REAL)
            part_count       = plc.read_by_name('MachineData.PartCount',       pyads.PLCTYPE_INT)

            # Send as JSON to browser
            await websocket.send_json({
                'ConveyorRunning': conveyor_running,
                'MotorTemp':       round(motor_temp, 2),
                'PartCount':       part_count
            })

            await asyncio.sleep(1)
    except:
        pass


@app.get('/history')
def history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM MachineData ORDER BY Id DESC LIMIT 10')
    rows = cursor.fetchall()
    conn.close()

    result = []
    for row in rows:
        result.append({
            'Id':              row[0],
            'Timestamp':       row[1],
            'ConveyorRunning': row[2],
            'MotorTemp':       round(row[3], 2),
            'PartCount':       row[4]
        })

    return JSONResponse(result)