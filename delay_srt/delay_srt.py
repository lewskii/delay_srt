from .time import Time
import re


def __delay_timestamp(timestamp_parts: tuple[str], delay_ms: int) -> Time:
    original_time = Time(*(int(i) for i in timestamp_parts))
    return original_time + delay_ms

def delay_srt(path: str, delay_ms: int):
    with open(path) as file:
        lines = file.readlines()

    new_lines = []
    
    waiting_for_next_subtitle = False
    for line in lines:
        if waiting_for_next_subtitle and not line.strip():
            waiting_for_next_subtitle = False
        else:
            timestamps = Time.all_from_string(line)
            if len(timestamps) == 2:
                start = timestamps[0] + delay_ms
                end = timestamps[1] + delay_ms
                line = f"{start} --> {end}\n"
                waiting_for_next_subtitle = True
        
        new_lines.append(line)

    with open(path, 'w') as file:
        file.writelines(new_lines)
