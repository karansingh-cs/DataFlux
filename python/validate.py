import csv
import sys
import os
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Valid options
VALID_DEVICE_TYPES  = ['Motor', 'Valve']
REQUIRED_COLUMNS    = ['DeviceName', 'DeviceType', 'StartOutput', 'StopOutput', 'FaultInput']

errors_found = False

with open(f'{BASE_PATH}\\devices.csv', newline='') as f:
    reader = csv.DictReader(f)

    # Check all required columns exist
    for column in REQUIRED_COLUMNS:
        if column not in reader.fieldnames:
            print(f'ERROR: Missing column: {column}')
            errors_found = True

    # Check each row
    for i, row in enumerate(reader, start=2):

        # Check no empty values
        for column in REQUIRED_COLUMNS:
            if not row[column].strip():
                print(f'ERROR: Row {i} — {column} is empty')
                errors_found = True

        # Check device type is valid
        if row['DeviceType'] not in VALID_DEVICE_TYPES:
            print(f'ERROR: Row {i} — invalid DeviceType: {row["DeviceType"]}')
            errors_found = True

        # Check address format starts with % 
        for addr_col in ['StartOutput', 'StopOutput', 'FaultInput']:
            if not row[addr_col].startswith('%'):
                print(f'ERROR: Row {i} — {addr_col} invalid address: {row[addr_col]}')
                errors_found = True

if errors_found:
    print('Validation failed.')
    sys.exit(1)
else:
    print('Validation passed — all devices look good.')