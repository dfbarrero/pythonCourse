class Time:
    """Represents the time of day

    attributes: hour, minute, second
    """

    def print_time(self):
	    print('{0:}:{1:}:{2:}'.format(self.hour, self.minute, self.second))

time = Time()
time.hour = 11
time.minute = 59
time.second = 33
time.print_time()
