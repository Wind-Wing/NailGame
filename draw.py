from activityFramework import ActivityFramework
from common import *
from resources import Resources
from shop import Shop


class DrawActivity(ActivityFramework):
    def __init__(self):
        super().__init__()
        # Constant
        self.actPointRequirement = [30, 60, 100, 150, 200, 300, 400, 500]
        self.actCoinReward = [120, 120, 120, 120, 120, 150, 150, 200]
        self.wishCoinReward = [3, 3, 3, 4, 4, 5, 0, 0]
        self.drawVoucherReward = [10, 10, 10, 10, 10, 0, 0, 0]
        self.baseActCoin = 450 + 750 + 1000 + 600

    def _get_act_type(self):
        return ActivityType.DRAW

    def act_daily_special_package(self, res):
        if Common.is_enough(res.whiteTadpole, 1):
            res.whiteTadpole -= 1
            self.actCoin += 100
            res.whiteTadpole += 20
            res.drawVoucher += 3
        return res

    def _act_one_time_special_package(self, res):
        if Common.is_enough(res.whiteTadpole, 200):
            res.whiteTadpole -= 200
            self.actCoin += 100
            res.drawVoucher += 3
        return res

    def _calc_act_point(self, res):
        total_draw_voucher = res.drawVoucher
        res.drawVoucher = 0
        return res, total_draw_voucher


if __name__ == "__main__":
    res = Resources()
    res.whiteTadpole = 16000
    res.drawVoucher = 350
    res.undergroundPoint = 600

    act = DrawActivity()
    act.reset()
    for i in range(ActivityDays):
        res.add_daily_resources()
        res = act.act_daily_special_package(res)
        res = Shop.buy_one_day(res)
    res = act.calc_act_coin(res)
    res = act.calc_act_level(res)
    res.show()
