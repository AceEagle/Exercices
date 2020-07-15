class ChInput:
    def __init__(self):
        import time
        self.TimeNow = time.clock_gettime(time.CLOCK_REALTIME)
        print(self.TimeNow)
