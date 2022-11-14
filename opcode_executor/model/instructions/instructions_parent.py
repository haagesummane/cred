from typing import List


class InstructionsParent:
    def __init__(self, ins_str:str):
        self.instruction_str = ins_str

        self.separator:str = None
        self.instruction = None
        self.num_inp_params = None
        self.instr_name = None # ideally this should be equal to self.__class__.__name__

    def parse(self):
        inputs = self.instruction_str.split(self.separator)
        if inputs[0].strip()!=self.instr_name:


    @property
    def instruction(self,ins_str:str):
        self.instruction=self.parse(ins_str)


    def validate(self, params:List):
        raise Exception("instruction_parent.validate must be implemented!")

    def execute(self, params:List):
        raise Exception("instruction_parent.execute must be implemented!")



