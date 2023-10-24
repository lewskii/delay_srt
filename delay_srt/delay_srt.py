"""Tools for delaying SubRip files.

Functions:
- delay_srt: delay the subtitles in a SubRip file
"""
from .time import Time
import re


def delay_srt(path: str, delay_ms: int) -> None:
    """Delay every subtitle in a SubRip file by a given number of milliseconds.

    The file is modified in place.
    
    Parameters:
    - path: the path to the file
    - delay_ms: the delay to be applied, in milliseconds

    Exceptions:

    The function will probably raise all sorts of exceptions if the file that
    `path` points to is somehow malformed.
    """
    with open(path) as file:
        subtitle_blocks = [
            b.split('\n')
            for b
            # split on lines that are empty or only contain whitespace
            in re.split(r"\n\s*\n", file.read())
        ]

    new_lines = []
    for block in subtitle_blocks:
        # index 1 always has the line with the timestamps on it
        start, end = Time.all_from_string(block[1])
        block[1] = f"{start + delay_ms} --> {end + delay_ms}"
        new_lines.extend([s + '\n' for s in block])
        new_lines.append("\n")

    with open(path, 'w') as file:
        # idk why but there are always two extra newlines at the end
        file.writelines(new_lines[:-2])
