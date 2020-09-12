from interface.activityFramework import ActivityFramework
from common import *


class WishActivity(ActivityFramework):
    def __init__(self):
        super().__init__()
        # Constant
        self.actPointRequirement = [10, 20, 30, 40, 50, 60, 80]
        self.actCoinReward = [120, 120, 150, 150, 180, 180, 200]
        self.drawVoucherReward = [0, 5, 5, 5, 5, 0, 0]
        self.wishCoinReward = [0, 0, 0, 2, 0, 0, 0]

        self.baseActCoin = 750 + 900 + 900 + 250

    def _get_act_type(self):
        return ActivityType.WISH

    def act_daily_special_package(self, res):
        if Common.is_enough(res.whiteTadpole, 1):
            res.whiteTadpole -= 1
            self.actCoin += 100
            res.wishCoin += 1
            res.whiteTadpole += 20
        return res

    def _act_one_time_special_package(self, res):
        if Common.is_enough(res.whiteTadpole, 200):
            res.whiteTadpole -= 200
            self.actCoin += 100
            res.wishCoin += 2
        return res

    def _calc_act_point(self, res):
        total_wish_coin = res.wishCoin
        res.wishCoin = 0
        return res, total_wish_coin
