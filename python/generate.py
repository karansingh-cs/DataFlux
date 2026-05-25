import csv
import uuid
from jinja2 import Environment, FileSystemLoader
from config import DB_PATH

# Load templates from the templates folder
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('MotorControl.tcpou')

# Read devices from CSV
with open('devices.csv', newline='') as f:
    reader = csv.DictReader(f)
    devices = list(reader)

# Generate a Function Block for each device
for device in devices:
    # Only generate for Motor type for now
    if device['DeviceType'] == 'Motor':
        output = template.render(
            DeviceName = device['DeviceName'],
            GuidValue  = str(uuid.uuid4())
        )

        # Save the generated file
        filename = f"generated/{device['DeviceName']}.TcPOU"
        with open(filename, 'w', encoding='utf-8') as out:
            out.write(output)

        print(f"Generated: {filename}")

print('Done.')