from common import *


class Shop:
    @staticmethod
    def buy_one_day(res):
        res = Shop.fighting_shop(res)
        res = Shop.museum_shop(res)
        res = Shop.underground_shop(res)
        res = Shop.daily_shop(res)
        return res

    @staticmethod
    def daily_shop(res):
        if Common.is_enough(res.whiteTadpole, 600):
            res.whiteTadpole -= 600
            res.wishCoin += 1

        if Common.is_enough(res.whiteTadpole, 1500):
            res.whiteTadpole -= 1500
            res.drawVoucher += 8

        if Common.is_enough(res.whiteTadpole, 600):
            res.whiteTadpole -= 600
            res.consecrateTime += Time(0, 10, 0)
        return res

    @staticmethod
    def fighting_shop(res):
        res.drawVoucher += 1. / 3.
        return res

    @staticmethod
    def museum_shop(res):
        res.wishCoin += 1.
        return res

    @staticmethod
    def underground_shop(res):
        if Common.is_enough(res.whiteTadpole, 160):
            res.whiteTadpole -= 160
            res.undergroundPoint += 100
        if Common.is_enough(res.undergroundPoint, 100, "undergroundPoint"):
            res.undergroundPoint -= 100
            res.wishCoin += 1. / 3.
        if Common.is_enough(res.undergroundPoint, 300, "undergroundPoint"):
            res.undergroundPoint -= 300
            res.drawVoucher += 2
        return res

