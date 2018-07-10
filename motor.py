# import l293d.driver as l293d

# GPIO Pins:
# pin 22
# pin 18
# pin 16

class Motor:
    def __init__(self,gpio_pin):
        self.gpio_pin = gpio_pin
        # self.motor = l293d.motor(22,18,16)
        # GPIO pin stuff

    def start_motor(self):
        # start motor
        return

    def stop_motor(self):
        # end motor
        return

    def cleanup(self):
        # to call at end of main event loop
        return
