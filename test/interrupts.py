
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# GPIO 23 set up as input. It is pulled up to stop false signals
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
time_stamp1 = time.time()
time_stamp2 = time.time()


def my_callback1(channel):
    global time_stamp1
    time_now = time.time()
    if (time_now - time_stamp1) >= 0.3:
        print "1111111111111111"
    time_stamp1 = time_now


def my_callback2(channel):
    global time_stamp2
    time_now = time.time()
    if (time_now - time_stamp2) >= 0.3:
        print "                     222222222222222222"
    time_stamp2 = time_now


GPIO.add_event_detect(20, GPIO.RISING, callback=my_callback1)
GPIO.add_event_detect(21, GPIO.RISING, callback=my_callback2)

while True:
    pass


    # print "Make sure you have a button connected so that when pressed"
    # print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"
    # raw_input("Press Enter when ready\n>")
    #
    # print "Waiting for falling edge on port 23"
    # # now the program will do nothing until the signal on port 23
    # # starts to fall towards zero. This is why we used the pullup
    # # to keep the signal high and prevent a false interrupt
    #
    # print "During this waiting time, your computer is not"
    # print "wasting resources by polling for a button press.\n"
    # print "Press your button when ready to initiate a falling edge interrupt."
    # try:
    #     GPIO.wait_for_edge(20, GPIO.RISING)
    #     print "\nFalling edge detected. Now your program can continue with"
    #     print "whatever was waiting for a button press."
    # except KeyboardInterrupt:
    #     GPIO.cleanup()  # clean up GPIO on CTRL+C exit
    # GPIO.cleanup()  # clean up GPIO on normal exit
