#!/usr/bin/python3
"""This script reads stdin line by line and
   computes matrics
"""
import sys

total_size = 0
status_codes_count = {
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
    """Prints the accumulated metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            file_size = int(parts[-1])
            status_code = parts[-2]

            total_size += file_size

            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            continue

except Exception:
    print_stats()
    raise
