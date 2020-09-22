from gpiozero import LED

class connection_controller(object):
    def __init__(self, enable_pin, index_pins):
        self.enable_pin = LED(enable_pin)
        for index in index_pins
            self.index_pins.append(LED(index))
        
    def connect(self, index):
        self.enable_pin.on()
        
        pins_values = bin(index)[2:]
        # Walk on all the bin values
       for index in range(len(self.index_pins)):
            if (pins_values[index] == '1'):
                self.index_pins[index].on()
            else:
                self.index_pins[index].off()

    def release(self):
        self.enable_pin.off()
