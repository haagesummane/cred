from dataclasses import dataclass
from typing import Set, List, Optional, Dict
import logging

from opcode_executor.model.instructions.instructions_parent import InstructionsParent


@dataclass
class IllegalInstruction:
    FAIL = 1
    SKIP = 2


class InstructionsList:
    def __init__(self, allowed_instructions: Dict[str, InstructionsParent], sep: Optional[str] = ' ',
                 illegal_inst: IllegalInstruction = IllegalInstruction.FAIL):
        self.allowed_inst = allowed_instructions
        self.separator = sep
        self.on_illegal_instruction = illegal_inst
        self.parsed_instructions = None

    def parse_inst(self, inst_str: str) -> InstructionsParent:
        args = list(map(lambda s: s.strip(), inst_str.split(self.separator)))
        inst = args[0].upper()
        if inst not in self.allowed_inst:
            if self.on_illegal_instruction == IllegalInstruction.FAIL:
                raise Exception("Instruction not found in allowed instruction set!")
            if self.on_illegal_instruction == IllegalInstruction.SKIP:
                logging.warning(f'skipping illegal instruction {inst} => {inst_str}')

        return self.allowed_inst[inst](args[1:])

    def parse_instructions(self, instructions: List[str]) -> List[InstructionsParent]:
        self.parsed_instructions = list(map(self.parse_inst, instructions))
        return self.parsed_instructions
