from resources import Resources
from activity.draw import DrawActivity
from activity.wish import WishActivity
from activity.consecrate import ConsecrateActivity
from shop import Shop

if __name__ == "__main__":
    res = Resources()
    res.whiteTadpole = 16000
    res.drawVoucher = 350
    res.wishCoin = 90
    res.consecrateTime = time(6, 0, 0)
    res.consecrateTimeSpeedUpRatio = time(0, 6, 30) / time(0, 8, 0)
    res.preAccumulateTime = time(8, 0, 0)
    res.undergroundPoint = 600

    drawAct = DrawActivity()
    wishAct = WishActivity()
    consecrateAct = ConsecrateActivity()

    activities = [drawAct, wishAct, consecrateAct] * 5
    idx = 0
    for act in activities:
        idx += 1
        print("--------------------------", idx, "--------------------------")

        act.reset()
        for i in range(ActivityDays):
            res.add_daily_resources()
            res = act.act_daily_special_package(res)
            res = Shop.buy_one_day(res)

        res = act.calc_act_coin(res)
        res = act.calc_act_level(res)
        res.show()

# TODO: Allow input selective action for each act / shop
# TODO: do not set resource to zero for each activity
# TODO: use DP to resolve feedback problem

