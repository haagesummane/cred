from typing import List, Dict, Set

from opcode_executor.model.register import Register
from opcode_executor.model.register_state import RegisterState


class InstructionsParent:
    def __init__(self, ins_str: str, params: List):
        self.params = params
        self.ins_str = ins_str

        self.NUM_INP_PARAMS = None
        self.INSTR_NAME = None  # ideally this should be equal to self.__class__.__name__
        self.DISALLOWED_REGISTERS: Set[str] = None

    def inst_specific_checks(self, params: List) -> bool:
        raise Exception('Not implemented!')# must be implemented in child

    def validate(self, params: List):
        if len(params) == self.NUM_INP_PARAMS:
            if params[0] not in self.DISALLOWED_REGISTERS:
                if self.inst_specific_checks(params):
                    return True

    def config_checks(self):
        if None in {self.INSTR_NAME, self.NUM_INP_PARAMS}:
            raise Exception("Developer ERROR: INSTR_NAME and NUM_INP_PARAMS must be defined")
        if self.INSTR_NAME != self.INSTR_NAME.upper():
            raise Exception('Developer ERROR: All instruction names should be in upper case!')

    def execute(self, params: List, registers: RegisterState):
        raise Exception("instruction_parent.execute must be implemented!")
