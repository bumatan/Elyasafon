import RPi.GPIO as GPIO

class connection_controller(object):
    def __init__(self, enable_pin, index_pins):
        self.enable_pin = enable_pin
        self.index_pins = index_pins
        
        # Init all pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(enable_pin, GPIO.OUT)
        for pin in self.index_pins:
            GPIO.setup(pin, GPIO.OUT)

    def connect(self, index):
        # Enable connection
        GPIO.output(self.enable_pin, GPIO.HIGH)

        # Walk on all the bin values and set the correct index
        pins_values = bin(index-1)[2:].zfill(3)
        print(pins_values)
        for index in range(len(self.index_pins)):
            if (pins_values[index] == '1'):
                print('setting pin value ', self.index_pins[index])
                GPIO.output(self.index_pins[index], GPIO.HIGH)
            else:
                GPIO.output(self.index_pins[index], GPIO.LOW)

    def release(self):
        GPIO.output(self.enable_pin, GPIO.LOW)
