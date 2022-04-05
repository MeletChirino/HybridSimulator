class InPort(Port):
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.type = "In"
    def update(self, value):
        self.value = value

class OutPort:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.type = "Out"
        self.connections = []

    def attach(self, in_port):
        self.connections.append(in_port)

    def dettach(self, in_port):
        self.connections.pop(in_port)

    def update_value(self, value):
        self.value = value
        for port in self.connections:
            port.update(self.value)

class Component:
    def __init__(self, name, in_ports, out_ports, **kwargs):
        self.name = name
        self.description = ""
        if kwargs.get('description'):
            self.description = kwargs['description']
        self.in_ports = in_ports
        self.out_ports = out_ports
        self.actual_state = 0
        self.te = 0.0
        self.tr = 0.0
    def delta_int(self, state):
        # returns next state if timeout event
        pass
    def delta_ext(self, state, event):
        # returns next state if discret event
        pass
    def ta(self, state):
        # returns timeout of certain state
        pass
    def lambda(self, state, output):
        # return new output value when timeout 
        pass