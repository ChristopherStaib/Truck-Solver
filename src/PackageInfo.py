import TrackTime


class Package:
    def __init__(self, array: [str]):
        self.pkg_id = array[0]
        self.address = array[1]
        self.city = array[2]
        self.state = array[3]
        self.zip = array[4]
        self.deadline = array[5]
        self.mass = array[6]
        self.spc_note = array[7] if len(array) == 8 else ""
        self.status = "At Hub"
        self.key = int(self.pkg_id) - 1
        self.time_loaded = None
        self.time_delivered = None

    # getters/accessors
    def get_pkg_id(self):
        return self.pkg_id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip

    def get_deadline(self):
        return self.deadline

    def get_mass(self):
        return self.mass

    def get_spc_note(self):
        return self.spc_note

    def get_status(self):
        return self.status

    def get_key(self):
        return self.key

    def get_time_delivered(self):
        return self.time_delivered

    def get_time_loaded(self):
        return self.time_loaded

    # setters/mutators
    def set_pkg_id(self, pkg_id: str):
        self.pkg_id = pkg_id

    def set_address(self, address: str):
        self.address = address

    def set_city(self, city: str):
        self.city = city

    def set_state(self, state: str):
        self.state = state

    def set_zip(self, zip_code: str):
        self.zip = zip_code

    def set_deadline(self, deadline: str):
        self.deadline = deadline

    def set_mass(self, mass: str):
        self.mass = mass

    def set_spc_note(self, spc_note: str):
        self.spc_note = spc_note

    def set_status(self, status: str):
        self.status = status

    def set_key(self, key: int):
        self.key = key

    def set_time_delivered(self, time_delivered: TrackTime):
        self.time_delivered = time_delivered

    def set_time_loaded(self, time_loaded: TrackTime):
        self.time_loaded = time_loaded

    def update_time_delivered(self, float_time: float):
        # aux variable
        temp_time_loaded = TrackTime.TrackTime(self.time_loaded.get_time())
        # create a new TrackTime Object using time attribute from time_loaded
        self.time_delivered = temp_time_loaded
        self.time_delivered.add_time(float_time)

    def print_time_loaded(self):
        print("Time Loaded:", self.get_time_loaded().get_time())

    def print_time_delivered(self):
        print("Time Delivered:", self.get_time_delivered().get_time())

    def print_all_information(self):
        print("*****Package Information*****")
        print("Package Id:", self.get_pkg_id())
        print("Address:", self.get_address())
        print("City:", self.get_city())
        print("State:", self.get_state())
        print("Zip:", self.get_zip())
        print("Deadline:", self.get_deadline())
        print("Mass:", self.get_mass())
        print("Special Note:", self.get_spc_note())
        print("Status:", self.get_status())
        print("Key:", self.get_key())
        self.print_time_loaded()
        self.print_time_delivered()
        print("*****************************")
