from enum import Enum
import math

ActivityDays = 7


class Common:
    @staticmethod
    def is_enough(own, need, name="white tadpole"):
        if own > need:
            return True
        else:
            print("%s is not enough, own %d, need %d", name, own, need)
            return False


class Time:
    def __init__(self, d, h, m):
        self.hours = 0
        self.hours += d * 24
        self.hours += h
        self.hours += m / 60.0

    def get_hours(self):
        math.floor(self.hours)

    def __add__(self, other):
        return self.hours + other.hours

    def __sub__(self, other):
        return self.hours - other.hours


class ActivityType(Enum):
    DRAW = 0,
    WISH = 1,
    CONSECRATE = 2

