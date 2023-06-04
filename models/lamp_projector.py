from models.abstract_projector import AbstractProjector


class LampProjector(AbstractProjector):
    """
    LampProjector class

    This class represents a lamp-based projector device.

    Attributes:
        model (str): The model of the lamp projector.
        resolution (str): The resolution of the projector.
        connected_device (str): The currently connected device.
        lamp_hours (int): The total lamp hours used.
        mode (str): The display mode of the projector.
        max_lamp_hours (int): The maximum lamp hours supported by the projector.

    Methods:
        increase_lamp_hours: Increases the lamp hours of the projector.
        get_remaining_working_hours: Gets the remaining lamp hours of the projector.
    """
    features_set = {"High brightness"}

    def __init__(self, model=None, resolution=None, connected_device=None, lamp_hours=0, mode='Active',
                 max_lamp_hours=10000):
        super().__init__(model, resolution, connected_device)
        self.lamp_hours = lamp_hours
        self.mode = mode
        self.max_lamp_hours = max_lamp_hours

    def increase_lamp_hours(self, hours):
        """
        Increases the lamp hours of the projector.

        Args:
            hours (int): The number of hours to increase the lamp hours.
        """
        self.lamp_hours += hours

    def get_remaining_working_hours(self):
        """
        Gets the remaining lamp hours of the projector.

        Returns:
            int: The remaining lamp hours of the projector.
        """
        return self.max_lamp_hours - self.lamp_hours

    def __str__(self):
        return f"LampProjector({super().__str__()}, lamp_hours={self.lamp_hours}, mode={self.mode}, " \
               f"max_lamp_hours={self.max_lamp_hours})"

    def __repr__(self):
        return f"LampProjector({super().__str__()}, lamp_hours={self.lamp_hours}, mode={self.mode}, " \
               f"max_lamp_hours={self.max_lamp_hours})"
