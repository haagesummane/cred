from typing import List

from opcode_executor.model.register_state import RegisterState


class MOV:
    def __init__(self):
        self.NUM_INP_PARAMS = 2
        self.INSTR_NAME = self.__class__.__name__
        self.DISALLOWED_REGISTERS = {}

    def inst_specific_checks(self, params: List) -> bool:
        return True  # come back later

    def execute(self, params: List, registers: RegisterState):
        r1 = registers.get_register(params[0])
        r2 = registers.get_register(params[1])
        r1.set_value(r2.value)
        registers.update_state(r1)
