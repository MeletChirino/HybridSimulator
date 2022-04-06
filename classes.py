class InPort:
    #observer
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.type = "In"

    def def_source(self, component):
        self.source = component
    def def_target(self, component):
        self.target = component

    def update(self, value):
        self.value = value

class OutPort:
    #subject
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
        impacted_ports = []
        for port in self.connections:
            #import pdb; pdb.set_trace()
            port.update(self.value)
            impacted_ports.append(port)
        return impacted_ports

class Component:
    def __init__(self, name, **kwargs):
        self.name = name
        self.current_state = 0
        self.te = 0.0
        self.tr = 0.0
        self.tl = 0.0

        self.description = ""
        if kwargs.get('description'):
            self.description = kwargs['description']

        self.input = []
        if kwargs.get('in_ports'):
            number = kwargs['in_ports']
            print(F"Setting {number} input ports")
            for i in range(number):
                self.input.append(InPort(F"IN{i}"))

        self.output = []
        if kwargs.get('out_ports'):
            number = kwargs['out_ports']
            print(F"Setting {number} output ports")
            for i in range(number):
                self.output.append(OutPort(F"OUT{i}"))
