import setuptools

with open("./README.md") as readme:
    long_description = readme.read()

setuptools.setup(
    name = "delay_srt",
    version = "0.2.0",
    description = "Delays the subtitles in a SubRip (.srt) file.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/lewskii/delay_srt",
    author = "lewski",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities"
    ],
    keywords = "delay subtitles subrip srt",
    packages = setuptools.find_packages()
)
