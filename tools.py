from classes import Component

def exist(list_, element):
    for element_ in list_:
        if element_ == element:
            return True
    return False

def connect(source, target, out_port, in_ports):
    for port in in_ports:
        port.def_source(source)
        port.def_target(target)
        out_port.attach(port)

class Data:
    def __init__(self, name, data):
        self.name = name
        self.data = data
