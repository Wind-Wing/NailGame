from abc import abstractmethod
import math


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
        print("%s action point: %d" % (self._get_act_type(), act_point))

        m = max(self.actPointRequirement)
        loop = math.floor(act_point / m)
        remain_point = act_point % m
        idx = 0
        if loop < self.maxLoop:
            for i in self.actPointRequirement:
                if i > remain_point:
                    break
                idx += 1

        self.actCoin += self.baseActCoin
        self.actCoin += ActivityFramework._calc_reward(self.actCoinReward, loop, idx)
        res.wishCoin += ActivityFramework._calc_reward(self.wishCoinReward, loop, idx)
        res.drawVoucher += ActivityFramework._calc_reward(self.drawVoucherReward, loop, idx)
        res.consecrateTime += ActivityFramework._calc_reward(self.consecrateTimeReward, loop, idx)
        res.whiteTadpole += ActivityFramework._calc_reward(self.whiteTadpoleReward, loop, idx)

        print("%s action loop: %d - %d" % (self._get_act_type(), loop, idx))

        return res

    @staticmethod
    def _calc_reward(reward_list, loop, idx):
        return sum(reward_list) * loop + sum(reward_list[:idx])

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

