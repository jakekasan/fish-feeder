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
        self.button_is_pressed = False
        print("Feeder created")
        self.print_schedule()
        
    def print_schedule(self):
        print("Schedule:")
        print("Start\t\tEnd")
        for key,value in self.schedule.items():
            print("{}\t{}".format(key.strftime("%H:%M:%S"),value.strftime("%H:%M:%S")))


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
        print(dt.datetime.now().strftime("%H:%M:%S"),"Starting feeder")
        self.start_feeder()
        while True:
            now = dt.datetime.now()
            if (now.hour == value.hour) and (now.minute == value.minute) and (now.second == value.second):
                print(dt.datetime.now().strftime("%H:%M:%S"),"End time reached")
                break
            time.sleep(1)
        self.stop_feeder()
        print(dt.datetime.now().strftime("%H:%M:%S"),"End of feeder function")

    def start_feeder(self):
        if self.feeder_running:
            return
        self.feeder_running = True
        print(dt.datetime.now().strftime("%H:%M:%S"),"started feeder")
        time.sleep(1)

    def stop_feeder(self):
        if not self.feeder_running:
            return
        self.feeder_running = False
        print(dt.datetime.now().strftime("%H:%M:%S"),"stopped feeder")
        time.sleep(1)

    def update(self):
        time_now = dt.datetime.now()
        if self.button_is_pressed:
            self.start_feeder()
            while self.button_is_pressed:
                time.sleep(5)
                self.stop_feeder()
                time_finished = dt.datetime.now()
                self.schedule[time_now] = time_finished
                self.button_is_pressed = False
                return
        for time_then in self.schedule.keys():
            if (time_then.hour == time_now.hour) and (time_then.minute == time_now.minute) and (time_then.second == time_now.second):
                self.run_feeder(self.schedule[time_then])


