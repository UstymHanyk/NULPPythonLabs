from models.abstract_projector import AbstractProjector


class PortableProjector(AbstractProjector):
    """
    PortableProjector class

    This class represents a portable projector device.

    Attributes:
        model (str): The model of the portable projector.
        resolution (str): The resolution of the projector.
        connected_device (str): The currently connected device.
        battery_capacity_in_mahs (int): The battery capacity in milliampere-hours (mAh).
        current_battery_charge_level_in_mahs (int): The current battery charge level in milliampere-hours (mAh).
        weight_in_kg (float): The weight of the portable projector in kilograms (kg).

    Methods:
        get_remaining_working_hours: Gets the remaining working hours based on the current battery charge level.
        charge_battery: Charges the battery of the portable projector.
    """
    features_set = {"Small projector size", "Portability"}

    def __init__(self, model: str, resolution: str, connected_device: str, battery_capacity_in_mahs: int,
                 current_battery_charge_level_in_mahs: int, weight_in_kg: float):
        super().__init__(model, resolution, connected_device)
        self.battery_capacity_in_mahs = battery_capacity_in_mahs
        self.current_battery_charge_level_in_mahs = current_battery_charge_level_in_mahs
        self.weight_in_kg = weight_in_kg

    def get_remaining_working_hours(self) -> int:
        """
        Gets the remaining working hours based on the current battery charge level.

        Returns:
            int: The remaining working hours based on the current battery charge level.
        """
        return int((self.current_battery_charge_level_in_mahs / self.battery_capacity_in_mahs) * 2)

    def charge_battery(self, charge_in_mahs: int):
        """
        Charges the battery of the portable projector.

        Args:
            charge_in_mahs (int): The amount of battery charge to add in milliampere-hours (mAh).
        """
        self.current_battery_charge_level_in_mahs += charge_in_mahs
        if self.current_battery_charge_level_in_mahs > self.battery_capacity_in_mahs:
            self.current_battery_charge_level_in_mahs = self.battery_capacity_in_mahs

    def __str__(self):
        return f"PortableProjector({super().__str__()}, " \
               f"battery_capacity_in_mahs={self.battery_capacity_in_mahs}, " \
               f"current_battery_charge_level_in_mahs={self.current_battery_charge_level_in_mahs}, " \
               f"weight_in_kg={self.weight_in_kg})"

    def __repr__(self):
        return f"PortableProjector({super().__str__()}, " \
               f"battery_capacity_in_mahs={self.battery_capacity_in_mahs}, " \
               f"current_battery_charge_level_in_mahs={self.current_battery_charge_level_in_mahs}, " \
               f"weight_in_kg={self.weight_in_kg})"
