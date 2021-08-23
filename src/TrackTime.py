class TrackTime:
    def __init__(self, time: str):
        self.time = time  # 8:30
        self.hour = int(time.split(':')[0])  # 8
        self.minute = int(time.split(':')[1])  # 30

    def __lt__(self, other):
        if self.hour < other.hour:
            return True
        if (self.hour == other.hour) and (self.minute < other.minute):
            return True
        else:
            return False

    def __gt__(self, other):
        if self.hour > other.hour:
            return True
        if (self.hour == other.hour) and (self.minute > other.minute):
            return True
        else:
            return False

    def __eq__(self, other):
        if (self.hour == other.hour) and (self.minute == other.minute):
            return True
        else:
            return False

    def get_time(self):
        return self.time

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def set_time(self, time):
        self.time = time

    def set_hour(self, hour):
        self.hour = hour

    def set_minute(self, minute):
        self.minute = minute

    def add_time(self, float_time: float):
        float_time = str(float_time)
        temp_hour = int(float_time.split('.')[0])  # 2.38
        temp_minute = float("0." + float_time.split('.')[1])
        temp_minute *= 60
        temp_minute = int(temp_minute)

        if temp_minute + self.minute >= 60:
            temp_hour += 1
            self.minute = (temp_minute + self.minute) % 60
        else:
            self.minute += temp_minute
        self.hour += temp_hour
        if len(str(self.minute)) == 1:
            self.time = str(self.hour) + ":0" + str(self.minute)
        else:
            self.time = str(self.hour) + ':' + str(self.minute)

    def print_time(self):
        print(self.time)
