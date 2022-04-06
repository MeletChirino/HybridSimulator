from classes import Component
from tools import *
from math import inf

class Proc(Component):
    def init(self):
        self.current_state = 0

    def internal(self):
        if(self.current_state == 1):
            self.current_state = 0

    def external(self, port):
        if(self.current_state == 0):
            self.current_state = 1

    def avance(self):
    #time advance
        if self.current_state == 0:
            return inf
        elif self.current_state == 1:
            return 3.0
        return -1
    def generate_output(self):
        if (self.current_state == 1):
            self.output[0].update_value(1)
            self.tr = self.avance()
    
    def conflict(self):
        pass

class Generator(Component):
    def init(self):
        self.current_state = 0
        self.tr = 2.0
    def avance(self):
        return 2.0
    def internal(self):
        pass
    def external(self):
        pass
    def generate_output(self):
        self.output[0].update_value = 1
        self.tr = self.avance()
    
    def conflict(self):
        pass

class Buffer(Component):
    def init(self):
        self.current_state = 0
        self.q = 0

    def internal(self):
        if(self.current_state == 1):
            self.current_state = 2
            self.q -= 1

    def external(self, port):
        import pdb; pdb.set_trace()
        if(self.current_state == 0 and port == self.input[0]):
            self.current_state = 1
            self.q += 1

        if(self.current_state == 1 and port == self.input[0]):
            self.q += 1
        
        if(self.current_state == 2 and port == self.input[0]):
            self.q += 1
        
        if(self.current_state == 2 and self.q > 0 and port == self.input[1]):
            self.current_state = 1

        if(self.current_state == 2 and self.q == 0 and port == self.input[1]):
            self.current_state = 0
    
    def avance(self):
        if self.current_state == 0:
            return inf
        elif self.current_state == 1:
            return 0
        if self.current_state == 2:
            return inf
        return -1
    
    def generate_output(self):
        if (self.current_state == 1):
            self.output[0].update_value(1)
        self.tr = self.avance()
    
    def conflict(self):
        self.external

