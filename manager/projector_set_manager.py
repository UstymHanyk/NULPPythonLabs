from itertools import chain
from manager.projector_manager import ProjectorManager
from models.display_mode import DisplayMode
from models.home_theater import HomeTheater
from models.lamp_projector import LampProjector
from models.laser_projector import LaserProjector
from models.portable_projector import PortableProjector


class ProjectorSetManager:
    """
    ProjectorSetManager class

    This class manages a collection of projectors and provides methods to iterate over the features of all projectors.

    Attributes:
        projector_manager (ProjectorManager): The projector manager object that contains the projectors.

    Methods:
        __iter__: Returns an iterator to iterate over the features of all projectors.
        __len__: Returns the total number of features in all projectors.
        __getitem__: Returns the feature at the specified index.
        __next__: Returns the next feature in the iterator.
    """
    def __init__(self, projector_manager):
        self.projector_manager = projector_manager

    def __iter__(self):
        return chain.from_iterable(projector.features_set for projector in self.projector_manager.projectors)

    def __len__(self):
        return sum(len(projector.features_set) for projector in self.projector_manager.projectors)

    def __getitem__(self, index):
        return list(self.__iter__())[index]

    def __next__(self):
        if not hasattr(self, '_iter'):
            self._iter = iter(self.__iter__())
        return next(self._iter)


if __name__ == "__main__":
    projector_manager = ProjectorManager()

    projector_manager.add_projector(LampProjector("Sony X-232", "1920x1080", "USB", 2, DisplayMode.ACTIVE))
    projector_manager.add_projector(HomeTheater("Samsung HT-500", "3840x2160", "HDMI", 2023, 65, "2.0", 3))
    projector_manager.add_projector(PortableProjector("LG P1", "1280x720", "Wi-Fi", 10000, 5000, 1.2))
    projector_manager.add_projector(LaserProjector("Epson L-500", "1920x1080", "HDMI", 50000, 3000))

    projector_set_manager = ProjectorSetManager(projector_manager)

    print(f"ProjectorSetManager length: {len(projector_set_manager)}")

    print("Iterating over ProjectorSetManager:")
    for feature in projector_set_manager:
        print(feature)

    print("Accessing 2nd element in ProjectorSetManager: ", projector_set_manager[1])
