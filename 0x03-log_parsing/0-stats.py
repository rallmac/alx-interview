#!/usr/bin/python3
"""This script reads stdin line by line and
   computes metrics
"""
import sys
import re

status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def print_stats():
    """Prints the accumulated metrics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


line_count = 0
total_file_size = 0

try:
    for line in sys.stdin:
        line_count += 1

        # Use regular expression to match the input format
        match = re.match(
            r'(\S+) - \[(.*?)\] '  # IP address and date
            r'"GET /projects/260 HTTP/1.1" '  # Request line
            r'(\d{3}) '  # Status code
            r'(\d+)',  # File size
            line
        )

        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            total_file_size += file_size

            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

    # Print the final stats when input ends
    print_stats()

except KeyboardInterrupt:
    # Print the final stats on keyboard interrupt (CTRL + C)
    print_stats()
    sys.exit()
