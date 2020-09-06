from enum import Enum

ActivityDays = 7


class Common:
    @staticmethod
    def is_enough(own, need, name="white tadpole"):
        if own > need:
            return True
        else:
            print("%s is not enough, own %d, need %d" % (name, own, need))
            return False


def time(d, h, m):
    hours = 0
    hours += d * 24
    hours += h
    hours += m / 60.0
    return hours


class ActivityType(Enum):
    DRAW = 0,
    WISH = 1,
    CONSECRATE = 2

