from abc import abstractmethod


class Operational:
    @abstractmethod
    def operate(self, res, cmd):
        pass

    @abstractmethod
    def get_cmd_length(self):
        pass

    @abstractmethod
    def _get_operation_list(self):
        pass
