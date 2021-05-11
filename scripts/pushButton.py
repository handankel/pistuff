import RPi.GPIO as GPIO

pin = 3 # GPIO pin
debug = True
uri = "http://%piholeIP%/admin/api.php?disable=%secondstodisable%&auth=%yourapikey%"


def button_callback(channel):
    if (debug):
        print("Button was pushed!")
    requests.get(uri)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.add_event_detect(pin, GPIO.RISING, callback=button_callback) # Setup event on pin 10 rising edge

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up
