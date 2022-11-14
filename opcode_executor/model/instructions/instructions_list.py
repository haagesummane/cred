from dataclasses import dataclass
from typing import List, Optional, Dict
import logging

from opcode_executor.model.instructions.instruction_set import AVAILABLE_INST
from opcode_executor.model.instructions.instruction_set.instructions_parent import InstructionsParent
from opcode_executor.model.register_state import RegisterState


@dataclass
class IllegalInstruction:
    FAIL = 1
    SKIP = 2


class InstructionsList:
    def __init__(self, disallowed_instructions: Optional[Dict[str, InstructionsParent]] = dict({}),
                 sep: Optional[str] = ' ',
                 illegal_inst: IllegalInstruction = IllegalInstruction.SKIP):
        self.disallowed_inst = disallowed_instructions
        self.separator = sep
        self.on_illegal_instruction = illegal_inst
        self.parsed_instructions = None
        self.instruction_objs = {a: AVAILABLE_INST[a]() for a in AVAILABLE_INST}

    def parse_inst(self, inst_str: str) -> [InstructionsParent, List]:
        args = list(map(lambda s: s.strip(), inst_str.split(self.separator)))
        inst = args[0].upper()
        if inst in self.disallowed_inst or inst not in self.instruction_objs:
            if self.on_illegal_instruction == IllegalInstruction.FAIL:
                raise Exception("Instruction not found in allowed instruction set!")
            if self.on_illegal_instruction == IllegalInstruction.SKIP:
                logging.warning(f'skipping illegal instruction {inst_str}')
                return None

        return self.instruction_objs[inst], args[1:]

    def parse_instructions(self, instructions: List[str]) -> [InstructionsParent, List]:
        self.parsed_instructions = list(filter(None, list(map(self.parse_inst, instructions))))
        return self.parsed_instructions

    def execute(self, registers: RegisterState):
        inst_lst = self.parsed_instructions  # if parsed_inst_lst is None else parsed_inst_lst
        for inst in inst_lst:
            # print(inst)
            inst[0].execute(params=inst[1], registers=registers)
