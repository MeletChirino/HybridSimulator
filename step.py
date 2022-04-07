from math import inf
from classes import Component

class Step(Component):
    def set_values(self, ts, x0, xf):
        self.ts = ts
        self.x0 = x0
        self.xf = xf

    def init(self):
        input_ports = len(self.input)
        if not input_ports == 2:
            raise Exception("2 Input Ports Required")
        output_ports = len(self.input)
        if not output_ports == 1:
            raise Exception("1 Output Port Required")
        self.current_state = 0
        self.tr = self.ts
        self.output[0].update_value(self.x0)

    def avance(self):
        if current_state == 0:
            return self.ts
        if current_state == 1:
            return inf

    def internal(self):
        if(self.current_state == 0):
            print(F"{self.name}: state 1 => 2")
            self.current_state = 1
            return 0

    def external(self):
        pass

    def generate_output(self):
        if(self.current_state == 0):
            return self.output[0].update_value(self.x0)
        elif self.current_state == 1:
            return self.output[0].update_value(self.xf)



