import time
from component import Buffer, Generator, Proc
from simulator import Simulator

def connect(source, target, out_port, in_ports):
    for port in in_ports:
        port.def_source(source)
        port.def_target(target)
        out_port.attach(port)

if __name__ == "__main__":
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
            generator,
            buffer,
            generator.output[0],
                [buffer.input[0],]
                )
    connect(
            buffer,
            processor,
            buffer.output[0],
            [processor.input[0],]
            )
    connect(
            processor,
            buffer,
            processor.output[0],
            [buffer.input[1],]
            )
    component_list = [
            generator,
            buffer,
            processor
            ]
    simulator = Simulator(
            13,
            component_list = component_list
            )
    simulator.run()

