#!/usr/bin/env python3
"""
Split all_files.txt into 10 parts for parallel processing.
"""

import os
from pathlib import Path

# Read all file paths
with open('all_files.txt', 'r') as f:
    files = [line.strip() for line in f if line.strip()]

print(f"Total files: {len(files)}")

# Split into 10 parts
num_parts = 10
part_size = len(files) // num_parts
remainder = len(files) % num_parts

parts = []
start = 0
for i in range(num_parts):
    end = start + part_size + (1 if i < remainder else 0)
    parts.append(files[start:end])
    start = end

# Write each part to a separate file
for i, part in enumerate(parts):
    filename = f'files_part_{i+1}.txt'
    with open(filename, 'w') as f:
        for file_path in part:
            f.write(file_path + '\n')
    print(f"Part {i+1}: {len(part)} files -> {filename}")

print(f"\nCreated {num_parts} file lists")