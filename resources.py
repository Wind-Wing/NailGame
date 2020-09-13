from common import time


class Resources:
    def __init__(self):
        # Act currency
        self.consecrateTime = 0
        self.wishCoin = 0
        self.drawVoucher = 0
        # Currency
        self.whiteTadpole = 0

        # Constant
        self.consecrateTimeSpeedUpRatio = 1. - (7.8 + 2.8 + 3.6 + 2.8 + 5.) / 100.
        # Act related
        self.actCoin = 0

    def reset(self):
        self.actCoin = 0

    def add_daily_resources(self):
        # tadpole pool
        self.whiteTadpole += 200
        # digger
        self.whiteTadpole += 80
        # killer
        self.whiteTadpole += 280
        self.drawVoucher += 1
        # explore
        self.whiteTadpole += 200
        # daily task
        self.consecrateTime += time(0, 2, 0)
        self.drawVoucher += 1
        self.whiteTadpole += 280

        # fighting shop
        self.drawVoucher += 1. / 3.
        # Museum shop
        self.wishCoin += 1.
        # Underground shop
        self.wishCoin += 1
        self.drawVoucher += 3

    def show(self):
        print("white tadpole: %d" % self.whiteTadpole)
        print("draw voucher: %d" % self.drawVoucher)
        print("wish coin: %d" % self.wishCoin)
        print("consecrate time: %d" % self.consecrateTime)
