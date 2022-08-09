import sys
sys.path.append(r"C:/Users/tc.kcosta/PadUtil/src")

from models.board import Board

class BoardBuilder:
    name: str
    model: str
    series_number: str
    product_code: str
    serial: str
    ne: str
    slot: str
    rack_position: int
    sub_rack: str
    firmware_version: float
    hardware_version: float
    description: str
    chassis_id: int
    inibido: bool
    in_test: bool
    platform: str

    def builder(self):
        return self

    def withName(self, name: str):
        self.name = name
        return self

    def withModel(self, model: str):
        self.model = model
        return self

    def withSeriesNumber(self, series_number: str):
        self.series_number = series_number
        return self

    def withProductCode(self, product_code: str):
        self.product_code = product_code
        return self

    def withSerial(self, serial: str):
        self.serial = serial
        return self

    def withNE(self, ne: str):
        self.ne = ne
        return self

    def withSlot(self, slot: str):
        self.slot = slot
        return self

    def withRackPosition(self, rack_position: int):
        self.rack_position = rack_position
        return self

    def withSubRack(self, sub_rack: str):
        self.sub_rack = sub_rack
        return self

    def withFirmwareVersion(self, firmware_version: float):
        self.firmware_version = firmware_version
        return self

    def withHardwareVersion(self, hardware_version: float):
        self.hardware_version = hardware_version
        return self

    def withDescription(self, description: str):
        self.description = description
        return self

    def withChassisId(self, chassis_id: int):
        self.chassis_id = chassis_id
        return self

    def withInibido(self, inibido: bool):
        self.inibido = inibido
        return self

    def withInTest(self, in_test: bool):
        self.in_test = in_test
        return self

    def withPlatform(self, platform: str):
        self.platform = platform
        return self

    def build(self):
        return Board(
            self.name,
            self.model,
            self.series_number,
            self.product_code,
            self.serial,
            self.ne,
            self.slot,
            self.rack_position,
            self.sub_rack,
            self.firmware_version,
            self.hardware_version,
            self.description,
            self.chassis_id,
            self.inibido,
            self.in_test,
            self.platform,
        )

board = BoardBuilder().builder().withName("board").withPlatform("platform").withSlot("slot").withDescription("Board for the board").withChassisId(1).withFirmwareVersion(1.5).withHardwareVersion(1.3).withInibido(True).withInTest(True).withNE("NE").withProductCode("code").withRackPosition(42).withModel("board model").withSerial("serial").withSeriesNumber("12354235").withSubRack("sub_rack").build()
print(board)