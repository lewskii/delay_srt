from argparse import ArgumentParser
from .delay_srt import delay_srt

parser = ArgumentParser(
    prog="delay_srt",
    description="delay everything in an SRT file by a given amount"
)
parser.add_argument(
    "path",
    help="the path to the file you want to delay",
    type=str
)
parser.add_argument(
    "delay",
    help="delay in milliseconds, negative values work too",
    type=int
)

args = parser.parse_args()
delay_srt(args.path, args.delay)
