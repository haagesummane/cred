from abc import ABC, abstractmethod

from typing import List

from opcode_executor.model.instructions.instruction_set.instructions_parent import InstructionsParent
from opcode_executor.model.instructions.instructions_list import InstructionsList
from opcode_executor.model.register_state import RegisterState


class OpcodeSimulator(ABC):
    def __init__(self):
        self.allowed_instructions_ = []

    @abstractmethod
    def execute(self, instructions: List[str]) -> RegisterState:
        inst_list = InstructionsList()
        inst_list.parse_instructions(instructions)
        inst_list.execute()


