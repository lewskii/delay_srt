from .time import Time
import re
import argparse


def delay_timestamp(original: tuple[str], delay: int) -> str:
    original_time = Time(*(int(i) for i in original))
    new_time = original_time + Time(milliseconds=delay)
    return str(new_time)

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
            start, end = timestamps
            start = delay_timestamp(start, delay_ms)
            end = delay_timestamp(end, delay_ms)
            new_lines.append(f"{start} --> {end}\n")
        else:
            new_lines.append(line)

    with open(path, 'w') as file:
        file.writelines(new_lines)
