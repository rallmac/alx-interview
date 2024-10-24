#!/usr/bin/python3
"""Write a script that reads stdin line by line and
   computes metrics
"""

import sys
import signal

total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """Print the metrics: total file size and count
       of status codes.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) >= 7:
            try:
                status_code = parts[-2]
                file_size = int(parts[-1])

                total_size += file_size

                if status_code in status_counts:
                    status_counts[status_code] += 1

                line_count += 1
                if line_count % 10 == 0:
                    print_stats()
            except (ValueError, IndexError):
                continue
except KeyboardInterrupt:
    print_stats()
    raise
