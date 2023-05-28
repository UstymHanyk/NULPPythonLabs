from models.lamp_projector import LampProjector, DisplayMode
from models.home_theater import HomeTheater
from models.portable_projector import PortableProjector
from models.laser_projector import LaserProjector


class ProjectorManager:
    """
    ProjectorManager class

    This class manages a collection of projectors and provides methods to add projectors and perform searches.

    Attributes:
        projectors (list): A list of projectors managed by the ProjectorManager.

    Methods:
        add_projector: Adds a projector to the collection.
        find_all_projectors_with_connection_device: Finds all projectors with a specified connected device.
        find_all_projectors_with_resolution_higher_than: Finds all projectors with resolution higher than specified.
    """

    def __init__(self):
        self.projectors = []

    def add_projector(self, projector):
        """
        Add a projector to the collection.

        Args:
            projector: The projector object to be added.
        """
        self.projectors.append(projector)

    def find_all_projectors_with_connection_device(self, connected_device):
        """
        Find all projectors with a specified connected device.

        Args:
            connected_device (str): The connected device to search for.

        Returns:
            list: A list of projectors that have the specified connected device.
        """
        return list(filter(lambda projector: projector.connected_device == connected_device, self.projectors))

    def find_all_projectors_with_resolution_higher_than(self, width_in_pixels, height_in_pixels):
        """
        Find all projectors with resolution higher than specified.

        Args:
            width_in_pixels (int): The minimum width in pixels.
            height_in_pixels (int): The minimum height in pixels.

        Returns:
            list: A list of projectors that have resolution higher than the specified dimensions.
        """
        return list(filter(lambda projector: int(projector.resolution.split('x')[0]) > width_in_pixels and int(
            projector.resolution.split('x')[1]) > height_in_pixels, self.projectors))


if __name__ == "__main__":
    projector_manager = ProjectorManager()

    projector_manager.add_projector(LampProjector("Sony X-232", "1920x1080", "USB", 2, DisplayMode.ACTIVE))
    projector_manager.add_projector(HomeTheater("Samsung HT-500", "3840x2160", "HDMI", 2023, 65, "2.0", 3))
    projector_manager.add_projector(PortableProjector("LG P1", "1280x720", "Wi-Fi", 10000, 5000, 1.2))
    projector_manager.add_projector(LaserProjector("Epson L-500", "1920x1080", "HDMI", 50000, 3000))

    print("All projectors:")
    for projector in projector_manager.projectors:
        print(projector)

    print("\nProjectors that connect via HDMI:")
    hdmi_projectors = projector_manager.find_all_projectors_with_connection_device("HDMI")
    for projector in hdmi_projectors:
        print(projector)

    print("\nProjectors with resolution higher than 1920x1080:")
    high_resolution_projectors = projector_manager.find_all_projectors_with_resolution_higher_than(1920, 1080)
    for projector in high_resolution_projectors:
        print(projector)
