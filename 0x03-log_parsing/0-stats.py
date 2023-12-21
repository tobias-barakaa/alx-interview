#!/usr/bin/python3

import sys
from collections import defaultdict


def print_stats(total_size, status_counts):
    """Print statistics based on total size and status counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


def parse_line(line):
    """Parse a log line and extract relevant information."""
    parts = line.split()
    if len(parts) != 7:
        return None
    ip, _, _, status_code, file_size = parts[0], parts[3], parts[5], parts[6]
    if status_code.isdigit() and int(status_code) in {200, 301, 400, 401, 403, 404, 405, 500}:
        return int(status_code), int(file_size)
    return None


total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        parsed = parse_line(line)
        if parsed:
            status_code, file_size = parsed
            total_size += file_size
            status_counts[status_code] += 1
            line_count += 1

        if line_count == 10:
            print_stats(total_size, status_counts)
            line_count = 0

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    sys.exit(0)
