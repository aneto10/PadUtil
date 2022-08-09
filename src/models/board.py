class Board:
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

    def __init__(
        self,
        name,
        model,
        series_number,
        product_code,
        serial,
        ne,
        slot,
        rack_position,
        sub_rack,
        firmware_version,
        hardware_version,
        description,
        chassis_id,
        inibido,
        in_test,
        platform, 
    ):
        self.name = name
        self.model = model
        self.series_number = series_number
        self.product_code = product_code
        self.serial = serial
        self.ne = ne
        self.slot = slot
        self.sub_rack = sub_rack
        self.rack_position = rack_position
        self.hardware_version = hardware_version
        self.firmware_version = firmware_version
        self.description = description
        self.chassis_id = chassis_id
        self.inibido = inibido
        self.in_test = in_test
        self.platform = platform