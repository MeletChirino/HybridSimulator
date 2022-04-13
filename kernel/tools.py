# python modules
import os
import time

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

class Log:
    def __init__(self, **kwargs):
        local_t = time.localtime()
        date = F"{local_t.tm_year}_{local_t.tm_mon}_{local_t.tm_mday}"
        hour = F'{local_t.tm_hour}_{local_t.tm_min}_{local_t.tm_sec}'
        file_name = F"logs/{date}-{hour}.log"
        self.debug_mode = kwargs['debug_mode']
        self.file_name = file_name

    def print(self, logs):
        if self.debug_mode:
            f = open(self.file_name, 'a')
            f.write(f'{logs}\n')
            f.close()

class Data:
    def __init__(self, name, data):
        self.name = name
        self.data = data
