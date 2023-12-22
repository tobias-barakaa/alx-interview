#!/usr/bin/python3
"""
Log parsing
"""

import sys


def initialize_stats() -> dict:
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    return {k: 0 for k in codes}


def parse_line(line: str) -> tuple:
    try:
        data = line.split()
        status_code = data[-2]
        file_size = int(data[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None, 0


def print_stats(stats: dict, file_size: int) -> None:
    print("File size: {:d}".format(file_size))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


def main():
    filesize, count = 0, 0
    stats = initialize_stats()

    try:
        for line in sys.stdin:
            count += 1
            status_code, file_size = parse_line(line)
            if status_code in stats:
                stats[status_code] += 1
            filesize += file_size
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise


if __name__ == '__main__':
    main()
