from classes import Component
import math

class Proc(Component):
    def __init__(self, name, **kwargs):
        Component.__init__.super(self, name)

def internal(self):
    if self.current_state == 1:
        self.current_state == 0

def external(self, req):
    if req == 1:
        self.current_state == 1

def avancement(self):
    if self.current_state == 0:
        return math.inf
    elif self.current_state == 1:
        return 3.0

def generate_output(self):
    if self.current_state == 1:
        done = True
