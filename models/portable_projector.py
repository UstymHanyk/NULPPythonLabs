from abstract_projector import AbstractProjector


class PortableProjector(AbstractProjector):
    """PortableProjector class

    This class represents a PortableProjector projector.
    """

    def __init__(self, model: str, resolution: str, connected_device: str, battery_capacity_in_mahs: int,
                 current_battery_charge_level_in_mahs: int, weight_in_kg: float):
        super().__init__(model, resolution, connected_device)
        self.battery_capacity_in_mahs = battery_capacity_in_mahs
        self.current_battery_charge_level_in_mahs = current_battery_charge_level_in_mahs
        self.weight_in_kg = weight_in_kg

    def get_remaining_working_hours(self) -> int:
        # assuming that the battery lasts for 2 hours at full charge
        return int((self.current_battery_charge_level_in_mahs / self.battery_capacity_in_mahs) * 2)

    def charge_battery(self, charge_in_mahs: int):
        self.current_battery_charge_level_in_mahs += charge_in_mahs
        if self.current_battery_charge_level_in_mahs > self.battery_capacity_in_mahs:
            self.current_battery_charge_level_in_mahs = self.battery_capacity_in_mahs

    def __str__(self):
        return f"PortableProjector({super().__str__()}, battery_capacity_in_mahs={self.battery_capacity_in_mahs}, " \
               f"current_battery_charge_level_in_mahs={self.current_battery_charge_level_in_mahs}, " \
               f"weight_in_kg={self.weight_in_kg})"
