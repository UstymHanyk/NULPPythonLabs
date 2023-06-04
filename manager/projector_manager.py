from decorators.method_calls_logger import record_calls_decorator
from decorators.method_results_logger import write_result_decorator
from decorators.pylint_decorator import run_pylint
from models.lamp_projector import LampProjector
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

    def __len__(self):
        return len(self.projectors)

    def __getitem__(self, index):
        return self.projectors[index]

    def __iter__(self):
        return iter(self.projectors)

    def execute_method_on_all_projectors(self):

        return [projector.get_remaining_working_hours() for projector in self.projectors]

    def get_projectors_enumerated(self):
        return enumerate(self.projectors)

    def zip_projector_with_method_result(self):
        return list(zip(self.projectors, self.execute_method_on_all_projectors()))

    def check_condition_on_all_projectors(self):
        condition_results = [projector.resolution == "1920x1080" for projector in self.projectors]
        return {"all": all(condition_results), "any": any(condition_results)}

    @record_calls_decorator
    @write_result_decorator
    def add_projector(self, projector):
        """
        Add a projector to the collection.

        Args:
            projector: The projector object to be added.
        """
        self.projectors.append(projector)

    @record_calls_decorator
    @write_result_decorator
    def find_all_projectors_with_connection_device(self, connected_device):
        """
        Find all projectors with a specified connected device.

        Args:
            connected_device (str): The connected device to search for.

        Returns:
            list: A list of projectors that have the specified connected device.
        """
        return list(filter(lambda projector: projector.connected_device == connected_device, self.projectors))

    @record_calls_decorator
    @write_result_decorator
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
    @run_pylint(__file__)
    def execute_pylint(self):
        print("Pylint is running..")

if __name__ == "__main__":
    projector_manager = ProjectorManager()

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

    print("\nExecuting a method on all projectors:")
    method_results = projector_manager.execute_method_on_all_projectors()
    for result in method_results:
        print(result)

    print("\nGetting enumerate projector list:")
    enumerated_projectors = projector_manager.get_projectors_enumerated()
    for enumerated_projector in enumerated_projectors:
        print(enumerated_projector)

    print("\nZipping projectors with method results:")
    zip_result = projector_manager.zip_projector_with_method_result()
    for projector, result in zip_result:
        print(f"Projector: {projector}, Method Result: {result}")

    print("\nChecking a condition on all projectors:")
    condition_results = projector_manager.check_condition_on_all_projectors()
    print(f"All condition results: {condition_results['all']}")
    print(f"Any condition results: {condition_results['any']}")
    projector_manager.execute_pylint()
