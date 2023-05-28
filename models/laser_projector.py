from models.abstract_projector import AbstractProjector


class LaserProjector(AbstractProjector):
    """
    LaserProjector class

    This class represents a laser projector device.

    Attributes:
        model (str): The model of the laser projector.
        resolution (str): The resolution of the projector.
        connected_device (str): The currently connected device.
        laser_lifespan_in_hours (int): The total lifespan of the laser in hours.
        laser_brightness_in_lumens (int): The brightness of the laser in lumens.

    Methods:
        get_remaining_working_hours: Gets the remaining working hours based on the laser lifespan.
    """

    def __init__(self, model: str, resolution: str, connected_device: str, laser_lifespan_in_hours: int,
                 laser_brightness_in_lumens: int):
        super().__init__(model, resolution, connected_device)
        self.laser_lifespan_in_hours = laser_lifespan_in_hours
        self.laser_brightness_in_lumens = laser_brightness_in_lumens

    def get_remaining_working_hours(self) -> int:
        """
        Gets the remaining working hours based on the laser lifespan.

        Returns:
            int: The remaining working hours based on the laser lifespan.
        """
        return self.laser_lifespan_in_hours

    def __str__(self):
        return f"LaserProjector({super().__str__()}, laser_lifespan_in_hours={self.laser_lifespan_in_hours}, " \
               f"laser_brightness_in_lumens={self.laser_brightness_in_lumens})"
