from common import time


class Resources:
    def __init__(self):
        self.consecrateTime = 0
        self.wishCoin = 0
        self.drawVoucher = 0

        self.whiteTadpole = 0

        self.consecrateTimeSpeedUpRatio = 0.0
        self.preAccumulateTime = None

        self.undergroundPoint = 0

    def add_daily_resources(self):
        self.undergroundPoint += 800. / 3.
        # killer
        self.whiteTadpole += 243
        self.drawVoucher += 1
        # explore
        self.whiteTadpole += 200
        # daily task
        self.consecrateTime += time(0, 2, 0)
        self.drawVoucher += 1
        self.whiteTadpole += 280

    def show(self):
        print("white tadpole: %d" % self.whiteTadpole)
        print("draw voucher: %d" % self.drawVoucher)
        print("wish coin: %d" % self.wishCoin)
        print("consecrate time: %d" % self.consecrateTime)
        print("underground point: %d" % self.undergroundPoint)
