from common import Time


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
        self.consecrateTime += Time(0, 2, 0)
        self.drawVoucher += 1
        self.whiteTadpole += 280

