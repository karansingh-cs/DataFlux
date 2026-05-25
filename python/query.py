import sqlite3
from config import AMS_NET_ID, DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('SELECT * FROM MachineData ORDER BY Id DESC LIMIT 10')
rows = cursor.fetchall()

print(f'{"Id":<5} {"Timestamp":<25} {"Running":<10} {"Temp":<10} {"Parts":<10}')
print('-' * 60)

for row in rows:
    print(f'{row[0]:<5} {row[1]:<25} {str(row[2]):<10} {row[3]:<10.2f} {row[4]:<10}')

conn.close()