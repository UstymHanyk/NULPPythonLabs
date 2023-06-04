from abc import ABC, abstractmethod
from decorators.logged import logged
from exceptions.no_connected_device import NoConnectedDeviceException

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
    features_set = set()

    def __init__(self, model: str = None, resolution: str = None, connected_device: str = None):
        self.model = model
        self.resolution = resolution
        self.connected_device = connected_device
    def __iter__(self):
        return iter(self.features_set)
    def add_input_device(self, device: str):
        """
        Adds an input device to the projector.

        Args:
            device (str): The input device to be added.
        """
        self.connected_device = device

    @logged(NoConnectedDeviceException, mode="console")
    def disconnect_device(self):
        """
        Disconnects the current input device.
        """
        if self.connected_device is None:
            raise NoConnectedDeviceException
        else:
            self.connected_device = None

    @abstractmethod
    def get_remaining_working_hours(self) -> int:
        """
        Abstract method to get the remaining working hours of the projector.

        Returns:
            int: The remaining working hours of the projector.
        """
        pass

    def filter_attributes_by_type(self, attribute_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, attribute_type)}

    def __str__(self):
        return f"model={self.model}, resolution={self.resolution}, connnected_device={self.connected_device}"
