from abstract_projector import AbstractProjector

from enum import Enum


class DisplayMode(Enum):
    SPORT = 1
    ACTIVE = 2
    PRESENTATION = 3


class LampProjector(AbstractProjector):
    """
    Represents a LampProjector device
    """

    def __init__(self, model=None, resolution=None, connected_device=None, lamp_hours=0, mode='Active',
                 max_lamp_hours=10000):
        super().__init__(model, resolution, connected_device)
        self.lamp_hours = lamp_hours
        self.mode = mode
        self.max_lamp_hours = max_lamp_hours

    def increase_lamp_hours(self, hours):
        self.lamp_hours += hours

    def get_remaining_working_hours(self):
        return self.max_lamp_hours - self.lamp_hours

    def __str__(self):
        return f"LampProjector({super().__str__()}, lamp_hours={self.lamp_hours}, mode={self.mode}," \
               f" max_lamp_hours={self.max_lamp_hours})"
