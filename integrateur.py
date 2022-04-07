from math import inf
from classes import Component
from scipy import integrate

class Integrateur(Component):
    def set_values(self, hstep):
        self.hstep = hstep

    def init(self):
        self.current_state = 0
        self.tr = self.hstep

    def internal(self):
        if self.current_state == 0:
            self.x += self.dx * self.hstep

    def external(self, port):
        if(self.current_state == 0 and port == self.input[0]):
            self.dx = self.input[0]
            self.x += self.dx * self.te 

    def avance(self):
        pass

    def generate_output(self):
        if (self.current_state == 0):
            return self.output[0].update_value(self.x)

    def conflict(self):
        self.external()