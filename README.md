# ASL CTR2000 Python Logger

**Read temperature from the ASL CTR2000 precision thermometer via RS-232 and save CSV logs using Python**

## Features

- Real-time acquisition of channel 1 temperature  
- Parse raw serial response like `1,24.288,"CEL"` into a human-readable `24.288 °C`  
- Append timestamp, channel number, temperature value and unit to a CSV file named with the script’s start time  

## Requirements

- Python 3.7 or newer  
- [pyserial](https://pypi.org/project/pyserial/)

```bash
pip install -r requirements.txt
