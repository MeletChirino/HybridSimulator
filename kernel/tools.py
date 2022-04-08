def exist(list_, element):
    for element_ in list_:
        if element_ == element:
            return True
    return False

def connect(source_connection, *target_connections):
    # (source_component, port_index)
    source_component = source_connection[0]
    port_index = source_connection[1]
    out_port = source_component.output[port_index]
    if not out_port.type == 'Out':
        raise Exception(F'{source_component.name}.{out_port.name} is not output port')

    for tuple_ in target_connections:
        target_component = tuple_[0]
        port_index = tuple_[1]
        in_port = target_component.input[port_index]
        if not in_port.type == 'In':
            raise Exception(F'{target_component.name}.{in_port.name} is not input port')
        in_port.def_source(source_component)
        in_port.def_target(target_component)
        out_port.attach(in_port)


def connect1(source, target, out_port, in_ports):
    for port in in_ports:
        port.def_source(source)
        port.def_target(target)
        out_port.attach(port)

class Data:
    def __init__(self, name, data):
        self.name = name
        self.data = data
