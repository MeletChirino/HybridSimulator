from classes import Component
from tools import *
from math import inf

class Proc(Component):
    def init(self):
        self.current_state = 0

    def internal(self):
        if(self.current_state == 1):
            self.current_state = 0

    def external(self):
        if(self.current_state and exist(self.event_list.exist()):
            self.current_state = 1

    def avance(self):
    #time advance
        if self.current_state == 0:
            return inf
        elif self.current_state == 1:
            return 3.0
        return -1
    def generate_output(self):
        if self.current_state == 1):
            self.output[0].update_value(1)

class Generator(Component):
    def init(self):
        self.current_state = 0
    def avance(self):
        return 2.0
    def internal(self):
        pass
    def external(self):
        pass
    def generate_output(self):
        self.output[0].update_value = 1

