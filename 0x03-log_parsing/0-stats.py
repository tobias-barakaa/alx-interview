#!/usr/bin/python3

import sys
import re
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            match = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)', line)
            if match:
                _, status_code, file_size = match.groups()
                total_size += int(file_size)
                status_counts[int(status_code)] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
