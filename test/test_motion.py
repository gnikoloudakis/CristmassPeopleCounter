from GPIO_counter.counter import Motion
import datetime, time

motion = Motion()

while True:
    motion.start_sensing(time.time())
    time.sleep(0.7)