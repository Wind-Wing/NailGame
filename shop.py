from interface.operational import Operational
from common import *


class Shop(Operational):
    def operate(self, res, cmd):
        operation_list = self._get_operation_list()
        assert(len(cmd) == len(operation_list))
        for i in range(len(cmd)):
            if cmd[i] == 1:
                res = operation_list[i](res)

    def get_cmd_length(self):
        return len(self._get_operation_list())

    def _get_operation_list(self):
        op_list = list()
        op_list.append(self.buy_wish_coin)
        op_list.append(self.buy_draw_voucher)
        op_list.append(self.buy_consecrate_time)
        return op_list

    @staticmethod
    def buy_wish_coin(res):
        if Common.is_enough(res.whiteTadpole, 600):
            res.whiteTadpole -= 600
            res.wishCoin += 1
        return res

    @staticmethod
    def buy_draw_voucher(res):
        if Common.is_enough(res.whiteTadpole, 1500):
            res.whiteTadpole -= 1500
            res.drawVoucher += 8
        return res

    @staticmethod
    def buy_consecrate_time(res):
        if Common.is_enough(res.whiteTadpole, 600):
            res.whiteTadpole -= 600
            res.consecrateTime += time(0, 10, 0)
        return res
