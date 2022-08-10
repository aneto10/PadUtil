from typing import Type

from services.inventory_service.interfaces.IInventory import IInventoryService

class InventoryController:
    def __init__(self, service: Type[IInventoryService]):
        self.service = service
    
    def read_inventory(self, filePath: str, tag: str):
        self.service.readInventory(filePath, tag)