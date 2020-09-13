from resources import Resources
from activity.draw import DrawActivity
from activity.wish import WishActivity
from activity.consecrate import ConsecrateActivity
from shop import Shop
from common import *
import numpy as np

if __name__ == "__main__":
    res = Resources()
    res.whiteTadpole = 10000
    res.drawVoucher = 350
    res.wishCoin = 90
    res.consecrateTime = time(6, 0, 0)
    res.consecrateTimeSpeedUpRatio = time(0, 6, 30) / time(0, 8, 0)

    shop = Shop()
    drawAct = DrawActivity()
    wishAct = WishActivity()
    consecrateAct = ConsecrateActivity()

    activities = [drawAct, wishAct, consecrateAct]

    # DP
    dp_dict = dict() # code -> (res, score)

    idx = 0
    for act in activities:
        idx += 1
        print("--------------------------", idx, "--------------------------")

        res.reset()
        for i in range(ActivityDays):
            res.add_daily_resources()
            res = act.act_daily_special_package(res)
            res = shop.operate(res, [])

        res = act.operate(res, 100)
        res.show()

# TODO: use DP to resolve feedback problem
# TODO: check the source of every critical resources and total amount

