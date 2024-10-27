#!/usr/bin/python3
import sys
import signal

# Initialize counters
total_file_size = 0
status_counts = {code: 0 for code in (200, 301, 400, 401, 403, 404, 405, 500)}
line_count = 0


def print_stats():
    """Prints the current statistics (file size and status counts)."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def process_line(line):
    """Processes a single line of input."""
    global total_file_size
    try:
        # Split line to extract IP, date, request, status code, and file size
        parts = line.split()
        if len(parts) < 7:
            return

        # Parse file size and status code
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Accumulate file size
        total_file_size += file_size

        # Count the status code if it's in our list
        if status_code in status_counts:
            status_counts[status_code] += 1
    except (ValueError, IndexError):
        # Ignore lines with incorrect format
        pass


def handle_interrupt(signal, frame):
    """Handles keyboard interruption (CTRL + C) by printing statistics."""
    print_stats()
    sys.exit(0)


# Attach the interrupt handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

# Main loop to read stdin line by line
for line in sys.stdin:
    process_line(line)
    line_count += 1

    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Final stats print at end of input
print_stats()
