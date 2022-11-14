from typing import List

from opcode_executor.model.register import Register


class RegisterState:
    def __init__(self, registers: List[Register]):
        self.__registers__ = {register.name: register for register in registers}

    def update_state(self, register: Register):
        if register.name not in self.__registers__.keys():
            raise Exception("The register: {} is not present".format(register.name))
        self.__registers__[register.name] = register

    def get_register(self, register_name) -> Register:
        if register_name not in self.__registers__.keys():
            raise Exception("The register: {} is not present".format(register_name))
        return self.__registers__.get(register_name)

    def reset(self):
        self.__registers__ = {name: Register(name) for name, register in self.__registers__.items()}
