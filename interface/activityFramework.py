from abc import abstractmethod
from interface.operational import Operational
import math


class ActivityFramework(Operational):
    def __init__(self):
        self.actPointRequirement = None
        self.actCoinReward = None
        self.wishCoinReward = [0] * 100
        self.drawVoucherReward = [0] * 100
        self.consecrateTimeReward = [0] * 100
        self.whiteTadpoleReward = [0] * 100

        self.baseActCoin = 0
        self.actCoinRequirement = [500, 1000, 1500, 3000, 5000]
        self.maxLoop = 5

    def operate(self, res, cmd):
        res = self._act_one_time_special_package(res)
        res = self._calc_act_coin(res, cmd)
        res = self._calc_act_level(res)
        return res

    def get_cmd_length(self):
        return len(self.actPointRequirement) * self.maxLoop

    @abstractmethod
    def _get_act_type(self): pass

    @abstractmethod
    def _try_use_act_point(self, res, num): pass

    def _calc_act_coin(self, res, limit):
        count = 0
        idx = 0
        l = len(self.actPointRequirement)
        while count < limit:
            idx = count % l

            req = self.actPointRequirement[idx]
            res, is_enough = self._try_use_act_point(res, req)
            if not is_enough:
                break

            res.actCoin += self.actCoinReward[idx]
            res.wishCoin += self.wishCoinReward[idx]
            res.drawVoucher += self.drawVoucherReward[idx]
            res.consecrateTime += self.consecrateTimeReward[idx]
            res.whiteTadpole += self.whiteTadpoleReward[idx]

            count += 1

        res.actCoin += self.baseActCoin
        print("%s action loop: %d - %d" % (self._get_act_type(), math.floor(count / l), idx))

        return res

    def _calc_act_level(self, res):
        # TODO: Add level coin and voucher reward
        # TODO: Can get several reward at the same time
        # TODO: Calculate final score
        level = 0
        print("%s action coin: %d" % (self._get_act_type(), res.actCoin))
        for i in self.actCoinRequirement:
            if res.actCoin < i:
                break
            level += 1
            res.actCoin -= i
        print("%s reward: level %d" % (self._get_act_type(), level))
        return res

    @abstractmethod
    def _act_one_time_special_package(self, res): pass

    @abstractmethod
    def act_daily_special_package(self, res): pass

