from models.lamp_projector import LampProjector, DisplayMode


class ProjectorManager:
    def __init__(self):
        self.projectors = []

    def add_projector(self, projector):
        self.projectors.append(projector)

    def find_all_projectors_with_connection_device(self, connected_device):
        return list(filter(lambda projector: projector.connected_device == connected_device, self.projectors))

    def find_all_projectors_with_resolution_higher_than(self, width_in_pixels, height_in_pixels):
        return list(filter(lambda projector: int(projector.resolution.split('x')[0]) > width_in_pixels and int(
            projector.resolution.split('x')[1]) > height_in_pixels, self.projectors))


if __name__ == "__main__":
    projector_manager = ProjectorManager()

    # Add projectors
    # For the sake of example, we assume that LampProjector, HomeTheater, etc., are subclasses of Projector
    # The constructors for these classes are not provided, so you'll have to define them
    projector_manager.add_projector(LampProjector("Sony X-232", "1920x1080", "USB", 2, DisplayMode.ACTIVE))
    # ...

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
