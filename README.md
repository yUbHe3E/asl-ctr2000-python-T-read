# ASL CTR2000 Python Logger

**Read temperature from the ASL CTR2000 precision thermometer via RS-232 and save CSV logs using Python**

## Features

- Real-time acquisition of channel 1 temperature  
- Parse raw serial response like `1,24.288,"CEL"` into a human-readable `24.288 °C`  
- Append timestamp, channel number, temperature value and unit to a CSV file named with the script’s start time

## How to Use

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Connect the ASL CTR2000 to your computer via RS-232 (e.g. USB-to-RS232 adapter).
    Find which port it appears on:
      Windows example: COM3
      Linux example: /dev/ttyUSB0
3. Open test.py and edit the serial config:
   ser = serial.Serial(
    port='COM3',          # change this to your port
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)
      Update port to match your system.
      Make sure baudrate / parity / stopbits match the CTR2000 settings.
4. Adjust logging settings:
    interval_time = 1  # seconds between reads
   ###Notice, 10 seconds may cause some error. Recommend is 1.
5. Run the logger:
    python test.py
    The script will:
      print timestamp + channel + temperature + unit to the console
      append the same data to a CSV file (created automatically)
6. Stop logging:
    Press Ctrl + C.
    The CSV file remains in the working directory.

## Requirements

- Python 3.7 or newer  
- [pyserial](https://pypi.org/project/pyserial/)

```bash
pip install -r requirements.txt
