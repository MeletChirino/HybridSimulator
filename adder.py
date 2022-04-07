from math import inf
from classes import Component

class Adder4x1(Component):
    def init(self):
        input_ports = len(self.input)
        if not input_ports == 4:
            raise Exception("IncorrectInputPortsQuantity")
        output_ports = len(self.input)
        if not output_ports == 1:
            raise Exception("IncorrectOutputPortsQuantity")
        #verify input conenctions
        for port in self.input:
            if not port.source:
                print(F"{port.target}.{port.name} not connected")
                raise Exception("InputConnectionError")
        self.current_state = 0
        self.tr = inf
        self.sum = 0
    def internal(self):
        if current_state == 1:
            print(F"{self.name}: state 1 => 0")
            self.current_state = 0
    def external(self, port_list):
        # aqui tienes que hacer las sumas
        if current_state == 0:
            print(F"{self.name}: state 0 => 1")
            self.current_state = 1
            self.sum = 0
            for value in self.input:
                self.sum += value
    def avance(self):
        if current_state == 0:
            return inf
        elif current_state == 1:
            return 0

    def generate_output(self):
        if current_state == 0:
            self.output[0].update_value(self.sum)


