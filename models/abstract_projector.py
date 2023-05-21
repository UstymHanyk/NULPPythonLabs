from abc import ABC, abstractmethod


class AbstractProjector(ABC):
    """
    AbstractProjector class

    This class represents an abstract projector with common properties for all projectors.

    Attributes:
        model (str): The model of the projector.
        resolution (str): The resolution of the projector.
        connected_device (str): The currently connected device.

    Methods:
        add_input_device: Adds an input device to the projector.
        disconnect_device: Disconnects the current input device.
        get_remaining_working_hours: Abstract method to get the remaining working hours of the projector.
    """

    def __init__(self, model: str = None, resolution: str = None, connected_device: str = None):
        self.model = model
        self.resolution = resolution
        self.connected_device = connected_device

    def add_input_device(self, device: str):
        """
        Adds an input device to the projector.

        Args:
            device (str): The input device to be added.
        """
        self.connected_device = device

    def disconnect_device(self):
        """
        Disconnects the current input device.
        """
        self.connected_device = None

    @abstractmethod
    def get_remaining_working_hours(self) -> int:
        """
        Abstract method to get the remaining working hours of the projector.

        Returns:
            int: The remaining working hours of the projector.
        """
        pass

    def __str__(self):
        return f"model={self.model}, resolution={self.resolution}, connnected_device={self.connected_device}"
