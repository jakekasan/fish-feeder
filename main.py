#!/bin/usr/env python3

from feeder import Feeder
import datetime as dt
import random
import time
    
now = dt.datetime.now()
default_schedule = {
    dt.datetime(2015,12,1,now.hour,now.minute+1,1):dt.datetime(2015,12,1,now.hour,now.minute+1,5),
    dt.datetime(2015,12,1,now.hour,now.minute+1,7):dt.datetime(2015,12,1,now.hour,now.minute+1,10),
    dt.datetime(2015,12,1,now.hour,now.minute+1,12):dt.datetime(2015,12,1,now.hour,now.minute+1,15),
    dt.datetime(2015,12,1,now.hour,now.minute+1,20):dt.datetime(2015,12,1,now.hour,now.minute+1,21)
}



def main():
    feeder = Feeder(schedule = None)

    while True:
        if random.random() < 0.01:
            feeder.button_is_pressed = True
        feeder.update()
        time.sleep(1)

if "__main__" == __name__:
    main()

