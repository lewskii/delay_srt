# delay_srt

Delays the subtitles in a SubRip (.srt) file by a given amount of time.

## Installation

1. [Install Python](https://www.python.org/downloads/).

    Python 3.11 or later should work for sure; when in doubt, just get the latest version. Older versions may work as well, but you're on your own with those.

2. Install delay_srt

    The following command should work for most people:

        pip install delay_srt

    If you want/need something more specialised, I'm sure you already know what you need to do differently.

## Usage

Just run the program through Python (with the `-m` flag) in your command line of choice, and give it the path to the file you want to delay and the delay in milliseconds. For example, the following command will delay `example.srt` by 1 second:

    python -m delay_srt example.srt 1000

Note that depending on your environment, you may need to use the `python3` command instead.
