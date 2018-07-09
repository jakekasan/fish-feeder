import datetime as dt
import RPi.GPIO as GPIO


class Feeder:
    def __init__(self):
        self.schedule = {}
        self.feeder_GPIO = None
        self.feeder_running = False

    def add_value(self,amount,given_time=None):
        if time not None:
            self.schedule[given_time] = amount
        else:
            self.schedule[dt.datetime.now()]

    def clear(self):
        self.schedule = {}

    def run_feeder(self,value):
        self.feeder_GPIO = True
        time.sleep(value)
        self.feeder_GPIO = False

    def start_feeder(self):
        if self.feeder_running:
            return
        print("starting feeder")
        self.feeder_running = True

    def stop_feeder(self):
        if not self.feeder_running:
            return
        print("stopping feeder")
        self.feeder_running = False

    def update(self):
        time_now = dt.datetime.now()
        for time_then in self.schedule.keys:
            if time_then.hour == time_now.hour:
                self.runFeeder(self.schedule[time_then])


    

    