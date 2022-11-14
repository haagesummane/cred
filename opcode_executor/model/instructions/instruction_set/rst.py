from typing import List

from opcode_executor.model.register_state import RegisterState


class RST:
    def __init__(self):
        self.NUM_INP_PARAMS = 0
        self.INSTR_NAME = self.__class__.__name__
        self.DISALLOWED_REGISTERS = {}

    def execute(self, params: List, registers: RegisterState):
        registers.reset()
