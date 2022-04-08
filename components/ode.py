# python modules
from math import inf
from scipy import integrate

# local modules
from components.base_classes import Component

class Integrateur(Component):
    def set_values(self, hstep):
        self.hstep = hstep

    def init(self):
        self.current_state = 0
        self.tr = self.hstep
        self.x = 0.0
        self.dx = 0.0

    def internal(self):
        if self.current_state == 0:
            self.x += float(self.dx * self.hstep)
            #import pdb; pdb.set_trace()

    def external(self, port):
        if(self.current_state == 0 and port == self.input[0]):
            self.x += self.dx * self.te 
            self.dx = float(self.input[0].value)
            #import pdb; pdb.set_trace()

    def avance(self):
        return self.hstep

    def generate_output(self):
        if (self.current_state == 0):
            return self.output[0].update_value(self.x + self.dx * self.hstep)

    def conflict(self):
        self.external()
