class InPort:
    #observer
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.type = "In"
    def update(self, value):
        self.value = value
        print(F"{self.type}-{self.name}: updated to => {self.value}")

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
        for port in self.connections:
            port.update(self.value)
        print(F"{self.type}-{self.name}: updated to => {self.value}")

class Component:
    def __init__(self, name, **kwargs):
        self.name = name
        self.description = ""
        if kwargs.get('description'):
            self.description = kwargs['description']

        self.input = []
        if kwargs.get('in_ports'):
            number = kwargs['out_ports']
            print(F"Setting {number} input ports")
            for i in range(number):
                self.input.append(InPort(F"IN{i}"))

        self.output = []
        if kwargs.get('out_ports'):
            number = kwargs['out_ports']
            print(F"Setting {number} output ports")
            for i in range(number):
                self.output.append(OutPort(F"OUT{i}"))

            self.def_in_ports(kwargs['out_ports'])
        self.current_state = 0
        self.te = 0.0
        self.tr = 0.0
        self.tl = 0.0

    def def_in_ports(self, number):
        for i in range(number):
            self.input.append(InPort(F"IN{i}"))

