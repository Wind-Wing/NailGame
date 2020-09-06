from resources import Resources
from draw import DrawActivity
from wish import WishActivity
from consecrate import ConsecrateActivity
from common import *
from shop import Shop

if __name__ == "__main__":
    res = Resources()

    drawAct = DrawActivity()
    wishAct = WishActivity()
    consecrateAct = ConsecrateActivity()

    activities = [drawAct, wishAct, consecrateAct]
    for act in activities:
        act.reset()
        for i in range(ActivityDays):
            res.add_daily_resources()
            res = act.act_daily_special_package(res)
            res = Shop.buy_one_day(res)
        res = act.calc_act_coin(res)
        res = act.calc_act_level(res)


