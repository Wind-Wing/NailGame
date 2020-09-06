from abc import abstractmethod


class ActivityFramework:
    def __init__(self):
        self.actPointRequirement = None
        self.actCoinReward = None
        self.wishCoinReward = [0] * 10
        self.drawVoucherReward = [0] * 10
        self.consecrateTimeReward = [0] * 10
        self.whiteTadpoleReward = [0] * 10

        self.baseActCoin = 0
        self.actCoinRequirement = [500, 1000, 1500, 3000, 5000]
        self.maxLoop = 5

        self.actCoin = 0

    def reset(self):
        self.actCoin = 0

    @abstractmethod
    def _get_act_type(self): pass

    @abstractmethod
    def _calc_act_point(self, res): pass

    def calc_act_coin(self, res):
        res = self._act_one_time_special_package(res)
        res, act_point = self._calc_act_point(res)
        self.actCoin += self.baseActCoin
        print("%s action point: %d" % (self._get_act_type(), act_point))

        i = 0
        l = len(self.actPointRequirement)
        while True:
            idx = i % l

            req_act_target = self.actPointRequirement[idx]

            if act_point < req_act_target:
                break

            if i >= l * 5:
                break

            act_point -= req_act_target
            self.actCoin += self.actCoinReward[idx]
            res.wishCoin += self.wishCoinReward[idx]
            res.drawVoucher += self.drawVoucherReward[idx]
            res.consecrateTime += self.consecrateTimeReward[idx]
            res.whiteTadpole += self.whiteTadpoleReward[idx]
            i += 1

        print("%s action loop: %d - %d" % (self._get_act_type(), i / l, i % l))

        return res

    def calc_act_level(self, res):
        level = 0
        print("%s action coin: %d" % (self._get_act_type(), self.actCoin))
        for i in self.actCoinRequirement:
            if self.actCoin < i:
                break
            level += 1
            self.actCoin -= i
        print("%s reward: level %d" % (self._get_act_type(), level))
        return res

    @abstractmethod
    def _act_one_time_special_package(self, res): pass

    @abstractmethod
    def act_daily_special_package(self, res): pass

