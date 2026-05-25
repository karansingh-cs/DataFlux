import sqlite3
from config import AMS_NET_ID, DB_PATH

# Create (or connect to) the database file
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS MachineData (
        Id              INTEGER PRIMARY KEY AUTOINCREMENT,
        Timestamp       DATETIME DEFAULT CURRENT_TIMESTAMP,
        ConveyorRunning BOOLEAN,
        MotorTemp       REAL,
        PartCount       INTEGER
    )
''')

conn.commit()
conn.close()

print('Database created successfully.')