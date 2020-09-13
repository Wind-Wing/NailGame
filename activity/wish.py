from interface.activityFramework import ActivityFramework
from common import *


class WishActivity(ActivityFramework):
    def __init__(self):
        super().__init__()
        # Constant
        self.actPointRequirement = [10, 10, 10, 10, 10, 10, 20]
        self.actCoinReward = [120, 120, 150, 150, 180, 180, 200]
        self.drawVoucherReward = [0, 5, 5, 5, 5, 0, 0]
        self.wishCoinReward = [0, 0, 0, 2, 0, 0, 0]

        self.baseActCoin = 750 + 900 + 900 + 250

    def _get_act_type(self):
        return ActivityType.WISH

    def act_daily_special_package(self, res):
        res.whiteTadpole -= 1
        res.actCoin += 100
        res.wishCoin += 1
        res.whiteTadpole += 20
        return res

    def _act_one_time_special_package(self, res):
        res.whiteTadpole -= 200
        res.actCoin += 100
        res.wishCoin += 2
        return res

    def _try_use_act_point(self, res, num):
        is_enough = False
        if res.wishCoin >= num:
            res.wishCoin -= num
            is_enough = True
        return res, is_enough
