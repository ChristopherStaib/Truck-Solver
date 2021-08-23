import TrackTime


class Truck:
    def __init__(self, truck_id: int, start_time: TrackTime):
        self.truck_id = truck_id
        self.route = []
        self.start_time = start_time
        self.speed = 18
        self.mileage = 0

    def get_route(self):
        return self.route

    def get_start_time(self):
        return self.start_time

    def get_truck_id(self):
        return self.truck_id

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_route(self, route):
        self.route = route

    def set_truck_id(self, truck_id):
        self.truck_id = truck_id

    def set_start_time(self, start_time):
        self.start_time = start_time

    def update_load_time_on_packages(self):
        package_load_time = TrackTime.TrackTime(self.get_start_time().get_time())
        for package in self.get_route():
            package.set_time_loaded(package_load_time)

    def print_start_time(self):
        self.start_time.print_time()
