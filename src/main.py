import sys

sys.path.append(r"C:/Users/tc.kcosta/PadUtil/src")

from services.inventory_service.inventory_service_xls import InventoryServiceXLS
from controllers.inventory.inventory_controller import InventoryController

filePath: str = input('Insira o caminho do arquivo: ')
tag: str = input('Insira a tag: ')

inventoryService = InventoryServiceXLS(filePath, tag)

controller = InventoryController(inventoryService)
controller.read_inventory()
