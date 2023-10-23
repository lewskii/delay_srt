from datetime import timedelta
import re
import argparse


def delay_timestamp(original: str, delay: int) -> str:
    h, m, s, ms = (int(i) for i in original)
    original_time = timedelta(hours=h, minutes=m, seconds=s, milliseconds=ms)
    new = original_time + timedelta(milliseconds=delay)
    print(str(new).replace('.', ','))
    return str(new)[:-3].replace('.', ',')

def delay_srt(path: str, delay_ms: int):
    with open(path) as file:
        lines = file.readlines()

    new_lines = []
    
    find_next = False
    for line in lines:
        if find_next:
            if not line.strip():
                find_next = False
            new_lines.append(line)
            continue
        
        timestamps = re.findall(
            r"(\d+):(\d+):(\d+),(\d+)",
            line
        )
        if timestamps:
            print(timestamps)
            start, end = timestamps
            start = delay_timestamp(start, delay_ms)
            end = delay_timestamp(end, delay_ms)
            new_lines.append(f"{start} --> {end}\n")
        else:
            new_lines.append(line)

    with open(path, 'w') as file:
        file.writelines(new_lines)
