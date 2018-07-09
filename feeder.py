import time
import datetime as dt
#import RPi.GPIO as GPIO


class Feeder:
    def __init__(self,schedule=None):
        if not schedule:
            self.schedule = {}
        else:
            self.schedule = schedule
        self.feeder_GPIO = None
        self.feeder_running = False
        print("Feeder created")
        print("Schedule:")
        print("Start\tEnd")
        for key,value in self.schedule.iteritems():
            print("{}\t{}".format(key,value))

    def add_value(self,given_time=None,end_time=None):
        print("Adding value to schedule")
        if not given_time == None:
            self.schedule[given_time] = end_time
        else:
            now = dt.datetime.now()
            then = dt.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second+5)
            self.schedule[now] = then

    def clear(self):
        self.schedule = {}

    def run_feeder(self,value):
        print("Starting feeder")
        self.start_feeder
        while True:
            now = dt.datetime.now()
            if (now.hour == value.hour) and (now.minute == value.minute) and (now.second == value.second):
                print("End time reached")
                break
            time.sleep(1)
        print("End of feeder function")

    def start_feeder(self):
        if self.feeder_running:
            return
        self.feeder_running = True
        print("started feeder")
        time.sleep(1)

    def stop_feeder(self):
        if not self.feeder_running:
            return
        self.feeder_running = False
        print("stopped feeder")
        time.sleep(1)

    def update(self):
        time_now = dt.datetime.now()
        for time_then in self.schedule.keys():
            if (time_then.hour == time_now.hour) and (time_then.minute == time_now.minute) and (time_then.second == time_now.second):
                self.run_feeder(self.schedule[time_then])


