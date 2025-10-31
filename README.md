# Open Ports Grabber

A simple and efficient multithreaded port scanner written in Python.

## Description

This tool allows you to scan a range of ports on a target host to identify which ones are open. It uses multithreading to scan multiple ports concurrently, making the process faster. The output is color-coded for easy readability.

## Features

- **Multithreaded Scanning:** Scans multiple ports at once for faster results.
- **Color-Coded Output:** Easily distinguish between open and closed ports.
- **Command-Line Arguments:** Simple and easy-to-use command-line interface.
- **Error Handling:** Gracefully handles common network errors.

## Requirements

- Python 3.x
- `colorama` library

You can install the required library using pip:

```bash
pip install colorama
```

## Usage

To use the port scanner, run the script from your terminal with the following arguments:

```bash
python open_ports_grabber.py -H <host> -I <initial_port> -F <final_port>
```

### Arguments

- `-H`, `--host`: The IP address or hostname of the target you want to scan.
- `-I`, `--initial`: The starting port of the scan range.
- `-F`, `--final`: The ending port of the scan range.

### Example

```bash
python open_ports_grabber.py -H 127.0.0.1 -I 1 -F 100
```

This command will scan ports from 1 to 100 on the localhost.

## Output

The script will print the status of each port as it's being scanned:

- **Green:** The port is open.
- **Blue/Yellow:** The port is closed or not responding.
- **Red:** An error occurred during the scan.

At the end of the scan, it will display a list of all the open ports found.

### Example Output

```
80 is open
22 is open
443 is open
...
The list of open ports is:
22
80
443
```

## How It Works

The script uses Python's `socket` library to attempt a connection to each port in the specified range. If a connection is successful, the port is marked as open. Multithreading is implemented using the `threading` library to speed up the scanning process by checking multiple ports simultaneously.

## Disclaimer

This tool is intended for educational purposes and ethical use only. Do not use it to scan networks or hosts without explicit permission.
