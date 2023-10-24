"""Simple tools for working with time.

Classes:
- Time: a simple representation of time
"""
import re

class Time:
    """Simple representation of time at a scale from milliseconds to hours.
    
    Formatted as "HH:MM:SS,mmm" as a string.

    Addition between Time objects is supported. Additionally, given a Time `t`
    and an integer `n`, `t + n` is equivalent to `t + Time(milliseconds=n)`.
    
    Attributes:
    - h: hours
    - min: minutes
    - s: seconds
    - ms: milliseconds
    """
    __MS_MAX = 1000
    __S_MAX = __MIN_MAX = 60

    @classmethod
    def all_from_string(
        cls,
        string: str,
        pattern: str | re.Pattern[str] = r"(\d+):(\d+):(\d+),(\d+)"
    ):
        """Find all valid Times in a given string and return them in a list.

        Parameters:
        - string: the string that will be parsed
        - pattern: a regex pattern containing capture groups for hours, minutes,
        seconds, and milliseconds, in that order
        """
        return [Time(*(int(i) for i in r)) for r in re.findall(pattern, string)]

    def __init__(
            self,
            hours: int = 0,
            minutes: int = 0,
            seconds: int = 0,
            milliseconds: int = 0
    ) -> None:
        self.__h = hours
        self.__min = minutes
        self.__s = seconds
        self.__ms = milliseconds
        self.__standardise()

    @property
    def h(self):
        """hours"""
        return self.__h
    
    @h.setter
    def h(self, new: int):
        self.__h = new
        self.__standardise()

    @property
    def min(self):
        """minutes"""
        return self.__min
    
    @min.setter
    def min(self, new: int):
        self.__min = new
        self.__standardise()

    @property
    def s(self):
        """seconds"""
        return self.__s
    
    @s.setter
    def s(self, new: int):
        self.__s = new
        self.__standardise()

    @property
    def ms(self):
        """milliseconds"""
        return self.__ms
    
    @ms.setter
    def ms(self, new: int):
        self.__ms = new
        self.__standardise()
    
    def __standardise(self) -> None:
        if self.ms >= Time.__MS_MAX:
            self.__s += self.ms // Time.__MS_MAX
            self.__ms %= Time.__MS_MAX
        if self.s >= Time.__S_MAX:
            self.__min += self.s // Time.__S_MAX
            self.__s %= Time.__S_MAX
        if self.min >= Time.__MIN_MAX:
            self.__h += self.min // Time.__MIN_MAX
            self.__min %= Time.__MIN_MAX

    def __str__(self) -> str:
        return f"{self.h:02}:{self.min:02}:{self.s:02},{self.ms:03}"
    
    def __repr__(self) -> str:
        return f"Time({self.h}h, {self.min}min, {self.s}s, {self.ms}ms)"
    
    def __add__(self, other):
        try:
            return Time(
                self.h + other.h,
                self.min + other.min,
                self.s + other.s,
                self.ms + other.ms
            )
        except AttributeError:
            return Time(
                self.h,
                self.min,
                self.s,
                self.ms + int(other)
            )
    