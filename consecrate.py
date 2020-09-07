from activityFramework import ActivityFramework
from common import *
import math
from resources import Resources
from shop import Shop


class ConsecrateActivity(ActivityFramework):
    def __init__(self):
        super().__init__()
        # Constant
        self.actPointRequirement = [60, 90, 120, 150, 180, 240]
        self.actCoinReward = [150, 150, 160, 180, 210, 250]
        self.wishCoinReward = [1, 1, 2, 2, 2, 0]
        self.baseActCoin = 400 * 4 + 1200

        self.baseTime = time(7, 0, 0) - time(0, 10, 0)

    def _get_act_type(self):
        return ActivityType.CONSECRATE

    def act_daily_special_package(self, res):
        if Common.is_enough(res.whiteTadpole, 1):
            res.whiteTadpole -= 1
            self.actCoin += 100
            res.consecrateTime += time(0, 0, 30)
        return res

    def _act_one_time_special_package(self, res):
        if Common.is_enough(res.whiteTadpole, 200):
            res.whiteTadpole -= 200
            self.actCoin += 100
            res.consecrateTime += time(0, 9, 0)
            res.drawVoucher += 1
        return res

    def _calc_act_point(self, res):
        total_hours = (self.baseTime + res.consecrateTime) / res.consecrateTimeSpeedUpRatio
        total_hours = math.floor(res.preAccumulateTime + total_hours)
        res.consecrateTime = time(0, 0, 0)
        return res, total_hours


if __name__ == "__main__":
    res = Resources()
    res.whiteTadpole = 16000
    res.consecrateTime = time(6, 0, 0)
    res.consecrateTimeSpeedUpRatio = time(0, 6, 30) / time(0, 8, 0)
    res.preAccumulateTime = time(8, 0, 0)
    res.undergroundPoint = 600

    act = ConsecrateActivity()
    act.reset()
    for i in range(ActivityDays):
        res.add_daily_resources()
        res = act.act_daily_special_package(res)
        res = Shop.buy_one_day(res)
    res = act.calc_act_coin(res)
    res = act.calc_act_level(res)
