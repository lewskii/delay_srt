from .time import Time
import re


def delay_timestamp(original: tuple[str], delay: int) -> str:
    original_time = Time(*(int(i) for i in original))
    new_time = original_time + Time(milliseconds=delay)
    return str(new_time)

def delay_srt(path: str, delay_ms: int):
    with open(path) as file:
        lines = file.readlines()

    new_lines = []
    
    waiting_for_next_subtitle = False
    for line in lines:
        if waiting_for_next_subtitle and not line.strip():
            waiting_for_next_subtitle = False
        else:
            timestamps = re.findall(
                r"(\d+):(\d+):(\d+),(\d+)",
                line
            )
            if len(timestamps) == 2:
                start = delay_timestamp(timestamps[0], delay_ms)
                end = delay_timestamp(timestamps[1], delay_ms)
                line = f"{start} --> {end}\n"
                waiting_for_next_subtitle = True
        
        new_lines.append(line)

    with open(path, 'w') as file:
        file.writelines(new_lines)
