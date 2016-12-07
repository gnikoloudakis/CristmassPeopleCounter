import platform
import time

from apscheduler.schedulers.background import BackgroundScheduler

if platform.system() == 'Linux':
    import RPi.GPIO as gpio
else:
    import gpio as gpio

scheduler = BackgroundScheduler()

# time_stamp1 = time.time()
motion_1 = False
motion_2 = False


class Motion(object):
    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.pir_pin_1 = 20
        self.pir_pin_2 = 21
        gpio.setup(self.pir_pin_1, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
        gpio.setup(self.pir_pin_2, gpio.IN)  # , pull_up_down=gpio.PUD_UP)

    def start_sensing(self, stamp):
        if gpio.input(self.pir_pin_1):
            time.sleep(0.7)
            if gpio.input(self.pir_pin_2):
                if (time.time() - stamp) >= 0.7:
                    time.sleep(1)
                    print ('222222')
