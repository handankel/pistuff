import RPi.GPIO as GPIO

pin = 5 # GPIO pin
debug = True


def button_callback(channel):
    if (debug):
        print("Button was pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) 
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(pin,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up
