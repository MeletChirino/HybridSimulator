# local modules
from components.test_components import Buffer, Generator, Proc
from kernel.simulator import  Simulator
from kernel.tools import connect, Log

def main():
    generator = Generator(
            "Generator",
            out_ports = 1
            )
    buffer = Buffer(
            "Buffer",
            in_ports = 2,
            out_ports = 1
            )
    processor = Proc(
            "Processor",
            in_ports = 1,
            out_ports = 1
            )
    connect(
            (generator, 0),
            (buffer, 0)
            )
    connect(
            (buffer, 0),
            (processor, 0)
            )
    connect(
            (processor, 0),
            (buffer, 1)
            )
    component_list = [
            generator,
            buffer,
            processor
            ]
    log_ = Log(
            debug_mode = True
            )
    simulator = Simulator(
            13,
            log = log_,
            component_list = component_list
            )
    simulator.run()
