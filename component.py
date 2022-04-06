from classes import Component
<<<<<<< HEAD
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
=======
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

>>>>>>> 2e1ca9ff4b4875b7022af311e2bf842ecbd9ab72
