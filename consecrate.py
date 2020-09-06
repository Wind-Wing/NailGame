from activityFramework import ActivityFramework
from common import *


class ConsecrateActivity(ActivityFramework):
    def __init__(self):
        super().__init__()
        # Constant
        self.actPointRequirement = [60, 90, 120, 150, 180, 240]
        self.actCoinReward = [150, 150, 160, 180, 210, 250]
        self.wishCoinReward = [1, 1, 2, 2, 2, 0]
        self.baseActCoin = 400 * 4 + 1200

        self.baseTime = Time(7, 0, 0) - Time(0, 10, 0)

    def _get_act_type(self):
        return ActivityType.CONSECRATE

    def act_daily_special_package(self, res):
        if Common.is_enough(res.whiteTadpole, 1):
            res.whiteTadpole -= 1
            self.actCoin += 100
            res.consecrateTime += Time(0, 0, 30)
        return res

    def _act_one_time_special_package(self, res):
        if Common.is_enough(res.whiteTadpole, 200):
            res.whiteTadpole -= 200
            self.actCoin += 100
            res.consecrateTime += Time(0, 9, 0)
            res.drawVoucher += 1
        return res

        # TODO: special package
        #     elif activity_type == ActivityType.WISH:
        #         act_coin += 100
        #         res.wishCoin += 1
        #         res.whiteTadpole += 20

    def _calc_act_point(self, res):
        total_hours = (self.baseTime + res.consecrateTime) / res.consecrateTimeSpeedUpRatio
        total_hours = math.floor(res.preAccumulateTime + total_hours)
        res.consecrateTime = Time(0, 0, 0)
        return res, total_hours
