from typing import List

from opcode_executor.model.instructions.instruction_set.instructions_parent import InstructionsParent
from opcode_executor.model.register_state import RegisterState


class SET(InstructionsParent):
    def __init__(self):
        self.NUM_INP_PARAMS = 2
        self.INSTR_NAME = self.__class__.__name__
        self.DISALLOWED_REGISTERS = {}

    def inst_specific_checks(self, params: List) -> bool:
        try:
            params[1] = int(params[1])
            return True
        except Exception as _:
            return False

    def execute(self, params: List, registers: RegisterState):
        self.validate(params)
        r = registers.get_register(params[0])
        r.set_value(int(params[1]))
        registers.update_state(r)
