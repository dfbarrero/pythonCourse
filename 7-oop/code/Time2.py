class Time:
    """Represents the time of day

    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print('{0:}:{1:}:{2:}'.format(self.hour, self.minute, self.second))

time1 = Time()
time1.print_time()
time2 = Time(11, 40, 23)
time2.print_time()
