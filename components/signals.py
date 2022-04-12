# python modules
from math import inf

# local modules
from components.base_classes import Component

class Constant(Component):
    def set_values(self, x0):
        self.x0 = x0

    def init(self):
        input_ports = len(self.input)
        if not input_ports == 0:
            raise Exception("Input Port not Required")
        output_ports = len(self.output)
        if not output_ports == 1:
            raise Exception("1 Output Port Required")
        self.output[0].update_value(self.x0)
        self.tr = inf

    def avance(self):
        return inf
    def internal(self):
        pass

    def external(self):
        pass
    def generate_output(self):
        pass


class Step(Component):
    def set_values(self, ts, x0, xf):
        self.ts = ts
        self.x0 = x0
        self.xf = xf

    def init(self):
        input_ports = len(self.input)
        if not input_ports == 0:
            raise Exception("Input Port not Required")
        output_ports = len(self.output)
        if not output_ports == 1:
            raise Exception("1 Output Port Required")
        self.current_state = 0
        self.tr = self.ts
        self.output[0].update_value(self.x0)

    def avance(self):
        if self.current_state == 0:
            return self.ts
        if self.current_state == 1:
            return inf

    def internal(self):
        if(self.current_state == 0):
            print(F"{self.name}: state 1 => 2")
            self.current_state = 1

    def external(self):
        pass

    def generate_output(self):
        if self.current_state == 0:
            print(F"{self.name}: update value to {self.xf}")
            return self.output[0].update_value(self.xf)



