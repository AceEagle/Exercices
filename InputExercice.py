class ChInput:
    def __init__(self):
        import datetime as dt
        self.TimeNow = int(dt.now())


    def rien(self, date):
        print(self.TimeNow)


Omg = ChInput
Omg.rien(1, 52)