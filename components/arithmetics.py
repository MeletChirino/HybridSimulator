# python modules
from math import inf

# local modules
from components.base_classes import Component

class Adder4x1(Component):
    def init(self):
        input_ports = len(self.input)
        if not input_ports == 4:
            raise Exception("IncorrectInputPortsQuantity")
        output_ports = len(self.output)
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
        if self.current_state == 1:
            print(F"{self.name}: state 1 => 0")
            self.current_state = 0

    def external(self, port_list):
        if self.current_state == 0:
            print(F"{self.name}: state 0 => 1")
            self.current_state = 1
            self.sum = 0
            #import pdb; pdb.set_trace()
            for port in self.input:
                self.sum += port.value

    def avance(self):
        if self.current_state == 0:
            return inf
        elif self.current_state == 1:
            return 0

    def generate_output(self):
        if self.current_state == 1:
            return self.output[0].update_value(self.sum)


