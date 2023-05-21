from abc import ABC, abstractmethod


class AbstractProjector(ABC):
    """AbstractProjector class

    This class represents an abstract projector with common properties for all projectors.
    """

    def __init__(self, model: str = None, resolution: str = None, connected_device: str = None):
        self.model = model
        self.resolution = resolution
        self.connected_device = connected_device

    def add_input_device(self, device: str):
        self.connected_device = device

    def disconnect_device(self):
        self.connected_device = None

    @abstractmethod
    def get_remaining_working_hours(self) -> int:
        pass

    def __str__(self):
        return f"model={self.model}, resolution={self.resolution}, connnected_device={self.connected_device}"
