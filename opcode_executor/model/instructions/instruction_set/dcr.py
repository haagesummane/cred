from typing import List

from opcode_executor.model.register_state import RegisterState


class DCR:
    def __init__(self):
        self.NUM_INP_PARAMS = 1
        self.INSTR_NAME = self.__class__.__name__
        self.DISALLOWED_REGISTERS = {}

    def inst_specific_checks(self, params: List) -> bool:
        return True  # come back later

    def execute(self, params: List, registers: RegisterState):
        r = registers.get_register(params[0])
        r.set_value(r.value-1)
        registers.update_state(r)
