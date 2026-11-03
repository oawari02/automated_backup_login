# Automated Backup Logger

A Python utility script that monitors server backup statuses and records backup logs to a file.

## Features

- Parses server backup results across multiple infrastructure nodes (Web Server, Database Server, Mail Server).
- Automatically writes timestamped/status logs into `backup_log.txt`.
- Includes error handling for file I/O operations.

## Requirements

- Python 3.7+

## Usage

Run the script directly:

```bash
python automated_backup_login.py
```

The script will write the status of each server to `backup_log.txt`.
