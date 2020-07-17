import datetime as dt

class ChInput:
    import datetime as dt
    def __init__(self):
        self.TimeNow = dt.datetime.today()

    def AgeIn100Years(self):
        print('What is your name?')
        name = input()
        print('How old are you?')
        age = input()
        print('How much times do do you want to know it?')
        times = input()

        YearNow = self.TimeNow.year
        YearNeeded = 100 - int(age)
        YearIn100 = YearNow + YearNeeded

        for x in range(0, int(times)):
            print("Vous aurez 100 ans en {} !".format(YearIn100))



oui = ChInput()
oui.AgeIn100Years()
