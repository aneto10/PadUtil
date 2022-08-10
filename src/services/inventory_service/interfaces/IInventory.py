import sys
from typing import Any
sys.path.append(r"C:/Users/tc.kcosta/PadUtil/src")

from abc import ABC, abstractmethod

class IInventoryService(ABC):
    
    @abstractmethod
    def __updateColumnsNames__(columns):
        pass
    
    @abstractmethod
    def __updateColumnsNames__(series_number: str) -> str:
        pass
    
    @abstractmethod
    def readInventory(filePath: str, tag: str) -> Any:
        pass