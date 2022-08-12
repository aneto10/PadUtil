import sys

sys.path.append(r"C:/Users/tc.kcosta/PadUtil/src")

from services.inventory_service.inventory_service_xls import InventoryServiceXLS
from controllers.inventory.inventory_controller import InventoryController

inventoryService = InventoryServiceXLS("FILEPATH", "TAG")

controller = InventoryController(inventoryService)
controller.read_inventory()
