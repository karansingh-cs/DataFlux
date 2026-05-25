import pyads
import sqlite3
import time

# Connect to PLC
plc = pyads.Connection('192.168.1.10.1.1', pyads.PORT_TC3PLC1)
plc.open()

# Connect to database
conn = sqlite3.connect('dataflux.db')
cursor = conn.cursor()

print('DataFlux logger started...')

try:
    while True:
        # Read from PLC
        conveyor_running = plc.read_by_name('MachineData.ConveyorRunning', pyads.PLCTYPE_BOOL)
        motor_temp       = plc.read_by_name('MachineData.MotorTemp',       pyads.PLCTYPE_REAL)
        part_count       = plc.read_by_name('MachineData.PartCount',       pyads.PLCTYPE_INT)

        # Write to database
        cursor.execute('''
            INSERT INTO MachineData (ConveyorRunning, MotorTemp, PartCount)
            VALUES (?, ?, ?)
        ''', (conveyor_running, motor_temp, part_count))
        conn.commit()

        print(f'Logged — Temp: {motor_temp:.2f} | Parts: {part_count} | Running: {conveyor_running}')

        time.sleep(1)

except KeyboardInterrupt:
    print('Logger stopped.')
    plc.close()
    conn.close()