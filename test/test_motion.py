from GPIO_counter.counter import Motion
import datetime, time

motion = Motion()

while True:
    if motion.start_sensing(time.time()):
        print ('oooooooooooo')
        time.sleep(0.7)