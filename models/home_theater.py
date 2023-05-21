from abstract_projector import AbstractProjector

WORKING_HOURS_PER_YEAR = 3650


class HomeTheater(AbstractProjector):
    """
    Represents a HomeTheater device
    """

    def __init__(self, model=None, resolution=None, connected_device=None, sales_year=2023, screen_size=55,
                 smart_tv_version='1.0', warranty_years=5):
        super().__init__(model, resolution, connected_device)
        self.sales_year = sales_year
        self.screen_size = screen_size
        self.smart_tv_version = smart_tv_version
        self.warranty_years = warranty_years

    def get_remaining_working_hours(self):
        return self.warranty_years * WORKING_HOURS_PER_YEAR

    def __str__(self):
        return f"HomeTheater({super().__str__()}, sales_year={self.sales_year}, screen_size={self.screen_size}," \
               f" smart_tv_version={self.smart_tv_version}, warranty_years={self.warranty_years})"
