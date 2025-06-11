#!/usr/bin/env python3
"""
Simple metric that measures the size of hello.cpp file.
Returns the file size in bytes as the fitness value.
For size optimization, magpie will try to minimize this value.
"""

import os
import sys

def measure_file_size():
    """Measure the size of hello.cpp file in bytes."""
    file_path = "hello.cpp"
    
    try:
        # Get file size in bytes
        file_size = os.path.getsize(file_path)
        return file_size
    except FileNotFoundError:
        print(f"Error: {file_path} not found", file=sys.stderr)
        return float('inf')  # Return infinity if file not found
    except Exception as e:
        print(f"Error measuring file size: {e}", file=sys.stderr)
        return float('inf')

if __name__ == "__main__":
    size = measure_file_size()
    print(f"MAGPIE_FITNESS: {size}")
