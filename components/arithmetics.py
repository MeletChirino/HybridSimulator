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
                raise Exception("InputConnectionError")
        self.current_state = 0
        self.tr = inf
        self.sum = 0
        for port in self.input:
            self.sum += port.value
        self.output[0].update_value(self.sum)

    def internal(self):
        if self.current_state == 1:
            self.current_state = 0

    def external(self, port_list):
        if self.current_state == 0:
            self.current_state = 1
            self.sum = 0
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


