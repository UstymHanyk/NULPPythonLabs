class Projector:
    instance = None

    def __init__(self, model=None, resolution=None, lamp_hours=0, connected_device=None):
        self.model = model
        self.resolution = resolution
        self.lamp_hours = lamp_hours
        self.connected_device = connected_device

    @staticmethod
    def get_instance():
        if Projector.instance is None:
            Projector.instance = Projector()
        return Projector.instance

    def add_input_device(self, device):
        self.connected_device = device

    def disconnect_device(self):
        self.connected_device = None

    def increase_lamp_hours(self, hours):
        self.lamp_hours += hours

    def __str__(self):
        return f"Projector(model={self.model}, resolution={self.resolution}, lamp_hours={self.lamp_hours}, connected_device={self.connected_device})"


if __name__ == "__main__":
    projectors = [
        Projector(),
        Projector("Model1", "1920x1080", 100, "HDMI"),
        Projector.get_instance(),
        Projector.get_instance()
    ]

    for projector in projectors:
        print(projector)
