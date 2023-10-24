from argparse import ArgumentParser
from .delay_srt import delay_srt
from textwrap import dedent

parser = ArgumentParser(
    prog="delay_srt",
    description=dedent("""
        Delays every subtitle in a SubRip file by a given amount.
        The file is modified in place.
    """)
)
parser.add_argument(
    "file",
    help="the path to the file you want to delay",
    type=str
)
parser.add_argument(
    "delay",
    help="delay in milliseconds",
    type=int
)

args = parser.parse_args()
delay_srt(args.path, args.delay)
