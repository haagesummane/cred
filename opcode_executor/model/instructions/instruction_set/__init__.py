from .add import ADD
from .adr import ADR
from .dcr import DCR
from .inr import INR
from .mov import MOV
from .rst import RST
from .set import SET

AVAILABLE_INST = {ADD.__name__: ADD, ADR.__name__: ADR, DCR.__name__: DCR,
                  INR.__name__: INR, MOV.__name__: MOV, RST.__name__: RST, SET.__name__: SET, }
