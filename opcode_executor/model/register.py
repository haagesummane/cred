from typing import Optional, List


class Register:
    def __init__(self, name: str):
        self.__name__ = name
        self.value = 0
        # self.__disabled_instructions__ = disabled_instructions

    @property
    def name(self):
        return self.__name__

    #
    # @property
    def get_value(self):
        return self.value

    # @value.setter
    def set_value(self, value):
        self.value = value
