from typing import List

from opcode_executor.model.instructions.instruction_set.instructions_parent import InstructionsParent
from opcode_executor.model.register_state import RegisterState


class RST(InstructionsParent):
    def __init__(self):
        self.NUM_INP_PARAMS = 0
        self.INSTR_NAME = self.__class__.__name__
        self.DISALLOWED_REGISTERS = {}

    def inst_specific_checks(self, params: List) -> bool:
        return True  # come back later

    def execute(self, params: List, registers: RegisterState):
        self.validate(params)
        registers.reset()
