import pyads
import time
from config import AMS_NET_ID, DB_PATH

# Connect to local TwinCAT runtime
plc = pyads.Connection(AMS_NET_ID, pyads.PORT_TC3PLC1)
plc.open()

try:
    while True:
        # Read variables from MachineData GVL
        conveyor_running = plc.read_by_name('MachineData.ConveyorRunning', pyads.PLCTYPE_BOOL)
        motor_temp       = plc.read_by_name('MachineData.MotorTemp',       pyads.PLCTYPE_REAL)
        part_count       = plc.read_by_name('MachineData.PartCount',       pyads.PLCTYPE_INT)

        print(f'Conveyor Running : {conveyor_running}')
        print(f'Motor Temp       : {motor_temp}')
        print(f'Part Count       : {part_count}')
        print('------------')

        time.sleep(1)

except KeyboardInterrupt:
    print('Closed!')
    plc.close()