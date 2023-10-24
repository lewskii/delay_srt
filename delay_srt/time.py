"""Simple tools for working with time.

Classes:
- Time: a simple representation of time
"""

class Time:
    """Simple representation of time at a scale from milliseconds to hours.
    
    Supports addition. Formatted as "HH:MM:SS,mmm" as a string.
    
    Attributes:
    - h: hours
    - min: minutes
    - s: seconds
    - ms: milliseconds
    """
    ms_max = 1000
    s_max = min_max = 60

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
        if self.ms >= Time.ms_max:
            self.__s += self.ms // Time.ms_max
            self.__ms %= Time.ms_max
        if self.s >= Time.s_max:
            self.__min += self.s // Time.s_max
            self.__s %= Time.s_max
        if self.min >= Time.min_max:
            self.__h += self.min // Time.min_max
            self.__min %= Time.min_max

    def __str__(self) -> str:
        return f"{self.h:02}:{self.min:02}:{self.s:02},{self.ms:03}"
    
    def __repr__(self) -> str:
        return f"Time({self.h}h, {self.min}min, {self.s}s, {self.ms}ms)"
    
    def __add__(self, other):
        return Time(
            self.h + other.h,
            self.min + other.min,
            self.s + other.s,
            self.ms + other.ms
        )
    