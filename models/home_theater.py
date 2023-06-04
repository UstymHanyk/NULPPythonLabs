from models.abstract_projector import AbstractProjector

WORKING_HOURS_PER_YEAR = 3650


class HomeTheater(AbstractProjector):
    """
    HomeTheater class

    This class represents a home theater projector device.

    Attributes:
        model (str): The model of the home theater projector.
        resolution (str): The resolution of the projector.
        connected_device (str): The currently connected device.
        sales_year (int): The year the home theater projector was sold.
        screen_size (int): The screen size in inches.
        smart_tv_version (str): The version of the smart TV software.
        warranty_years (int): The number of years the warranty is valid.

    Methods:
        get_remaining_working_hours: Gets the remaining working hours based on the warranty.
    """
    features_set = {"Long working hours", "Big screen size"}

    def __init__(self, model=None, resolution=None, connected_device=None, sales_year=2023, screen_size=55,
                 smart_tv_version='1.0', warranty_years=5):
        super().__init__(model, resolution, connected_device)
        self.sales_year = sales_year
        self.screen_size = screen_size
        self.smart_tv_version = smart_tv_version
        self.warranty_years = warranty_years

    def get_remaining_working_hours(self):
        """
        Gets the remaining working hours based on the warranty.

        Returns:
            int: The remaining working hours based on the warranty.
        """
        return self.warranty_years * WORKING_HOURS_PER_YEAR

    def __str__(self):
        return f"HomeTheater({super().__str__()}, sales_year={self.sales_year}, screen_size={self.screen_size}, " \
               f"smart_tv_version={self.smart_tv_version}, warranty_years={self.warranty_years})"

    def __repr__(self):
        return f"HomeTheater({super().__str__()}, sales_year={self.sales_year}, screen_size={self.screen_size}, " \
               f"smart_tv_version={self.smart_tv_version}, warranty_years={self.warranty_years})"
