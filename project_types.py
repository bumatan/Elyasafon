
num_of_ports=8
commands=['connect', 'release']
connection_types=['bla1', 'bla2', 'bla3', 'bla4']

# "Pins definition"
connection_enable = dict()
connection_pins = dict()

# 'bla1' pins
connection_enable['bla1'] = 8
connection_pins['bla1'] = [10, 12, 16]

# 'bla2' pins
connection_enable['bla2'] = 18
connection_pins['bla2'] = [22, 24, 26]

# 'bla3' pins
connection_enable['bla3'] = 28
connection_pins['bla3'] = [32, 36, 38]

# 'bla4' pins
connection_enable['bla4'] = 40
connection_pins['bla4'] = [3, 5, 7]