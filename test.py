import serial
import time
import csv
import os
from datetime import datetime

# serial setting
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

start_ts = datetime.now().strftime('%Y%m%d_%H%M%S')
csv_filename = f'temperature_log_{start_ts}.csv'
interval_time = 1



if not os.path.exists(csv_filename):
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'channel', 'temperature', 'unit'])


while 1:
    # read channal 1
    ser.write(b'MEAS:CHANnel? 1\r')
    time.sleep(interval_time)
    raw = ser.readline()  # 读取一行 bytes

    # get data
    decoded = raw.decode('ascii', errors='ignore').strip()      # '1,24.288,"CEL"'
    channel_str, temp_str, unit_str = decoded.split(',')
    unit_code = unit_str.strip('"')                            # 'CEL'
    unit_map = {'CEL':'°C', 'FAR':'°F', 'KEL':'K'}
    unit_symbol = unit_map.get(unit_code, unit_code)

    # get time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # print
    print(f'{timestamp} — channel {channel_str} temp：{temp_str} {unit_symbol}')

    # writ to CSV
    with open(csv_filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, channel_str, temp_str, unit_symbol])

