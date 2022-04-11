# python modules
from math import inf
from scipy import integrate

# local modules
from components.base_classes import Component

class Integrateur(Component):
    def set_values(self, hstep):
        self.hstep = hstep

    def init(self):
        input_ports = len(self.input)
        if not input_ports > 0 and input_ports < 3:
            raise Exception("Input Port not Required")
        output_ports = len(self.output)
        if not output_ports == 1:
            raise Exception("1 Output Port Required")
        self.current_state = 0
        self.tr = self.hstep
        self.x = 0.0
        if input_ports == 2:
            self.x = self.input[1].value
        self.dx = float(self.input[0].value)

    def internal(self):
        if self.current_state == 0:
            self.x += float(self.dx * self.hstep)
            #import pdb; pdb.set_trace()

    def external(self, port):
        if(self.current_state == 0 and port == self.input[0]):
            self.x += self.dx * self.te
            self.dx = float(self.input[0].value)

    def avance(self):
        return self.hstep

    def generate_output(self):
        if (self.current_state == 0):
            return self.output[0].update_value(self.x + self.dx * self.hstep)

    def conflict(self):
        self.external()
