import datetime as dt

class ChInput:
    import datetime as dt
    def __init__(self):
        self.TimeNow = dt.date.today()

    def AgeIn100Years(self):
        print('What is your name?')
        name = input()
        print('How old are you?')
        age = input()
        print('How much timea you want to know it?')
        times = input()

oui = ChInput()
oui.AgeIn100Years()