#!/usr/bin/python3
import sys

# Initialize variables to store statistics
total_file_size = 0
status_code_counts = {}

try:
    for i, line in enumerate(sys.stdin, start=1):
        # Split the input line into components
        parts = line.split()
        
        if len(parts) != 10:
            # Skip lines that do not match the expected format
            continue
        
        # Extract relevant information
        status_code = parts[8]
        file_size = int(parts[9])
        
        # Update total file size
        total_file_size += file_size
        
        # Update status code counts
        if status_code.isnumeric():
            status_code = int(status_code)
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1
        
        # Print statistics every 10 lines
        if i % 10 == 0:
            print(f'Total file size: File size: {total_file_size}')
            for code in sorted(status_code_counts.keys()):
                print(f'{code}: {status_code_counts[code]}')
            print()
except KeyboardInterrupt:
    pass

