import datetime as dt

class Feeder:
    def __init__(self):
        self.schedule = {}
        self.feederGPIO = None

    def add_value(self,amount,given_time=None):
        if time not None:
            self.schedule[given_time] = amount
        else:
            self.schedule[dt.datetime.now()]

    def clear(self):
        self.schedule = {}

    def run_feeder(self,value):
        self.feederGPIO = True
        time.sleep(value)
        self.feederGPIO = False

    def 
        

    def update(self):
        time_now = dt.datetime.now()
        for time_then in self.schedule.keys:
            if time_then.hour == time_now.hour:
                self.runFeeder(self.schedule[time_then])


    

    