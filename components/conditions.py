# python modules
from math import inf

# local modules
from components.base_classes import Component

class Switch(Component):
    def set_intervals(self, *interval_list):
        # (inf, 3), (3, 0), (0, -inf)
        # [inf > x > 3], (3 > x > 0], (0 < x < -inf]
        self.interval_list = interval_list
        input_ports = len(self.input)
        n_intervals = len(interval_list)
        if not input_ports-1 == n_intervals:
            raise Exception("Input conditions does not match intervals")

    def interval_cond(self):
        i = 0
        for interval in self.interval_list:
            lim_inf = interval[1]
            lim_sup = interval[0]
            cond = self.input[0].value
            if cond < lim_sup and cond >= lim_inf:
                self.out_channel = i
                return self.out_channel

    def init(self):
        output_ports = len(self.output)
        if not output_ports == 1:
            raise Exception("1 Output Port Required")
        self.tr = inf
        self.current_state = 0
        self.interval_cond()
        i = self.out_channel
        out_val = self.input[i].value
        self.output[0].update_value(out_val)

    def avance(self):
        if self.current_state == 0:
            return inf
        elif self.current_state == 1:
            return 0

    def internal(self):
        if self.current_state == 1:
            self.current_state = 0

    def external(self, port):
        cond = self.interval_cond()
        if self.current_state == 0 and cond:
            self.current_state = 1

    def generate_output(self):
        if self.current_state == 1:
            i = self.interval_cond()
            val = self.input[i].value
            self.output[0].update_value(val)
