class Time:
    """ Represents the time of day

    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print(f"H: {self.hour}, M: {self.minute}, S: {self.second}")

time1 = Time()
time1.print_time()

time2 = Time(10, 30, 5)
time2.print_time()
