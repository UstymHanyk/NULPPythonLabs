from itertools import chain
from ua.lviv.iot.algo.part1.lab7.manager.projector_manager import ProjectorManager
from ua.lviv.iot.algo.part1.lab7.models.display_mode import DisplayMode
from ua.lviv.iot.algo.part1.lab7.models.home_theater import HomeTheater
from ua.lviv.iot.algo.part1.lab7.models.lamp_projector import LampProjector
from ua.lviv.iot.algo.part1.lab7.models.laser_projector import LaserProjector
from ua.lviv.iot.algo.part1.lab7.models.portable_projector import PortableProjector


class ProjectorSetManager:
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
