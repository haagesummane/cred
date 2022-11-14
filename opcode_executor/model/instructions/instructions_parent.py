from typing import List


class InstructionsParent:
    def __init__(self, params: List):
        self.params = params
        self.num_inp_params = None
        self.instr_name = None  # ideally this should be equal to self.__class__.__name__

    def config_checks(self):
        if self.instr_name != self.instr_name.upper():
            raise Exception('Developer WARNING: All instruction names should be in upper case!')

    @property
    def instruction(self, ins_str: str):
        self.instruction = self.parse(ins_str)

    def validate(self, params: List):
        raise Exception("instruction_parent.validate must be implemented!")

    def execute(self, params: List):
        raise Exception("instruction_parent.execute must be implemented!")
