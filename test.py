import time
from component import Buffer, Generator, Proc
from simulator import Simulator

def connect(out_port, in_ports):
    for port in in_ports:
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
            generator.output[0],
                [buffer.input[0],]
                )
    connect(
            buffer.output[0],
            [processor.input[0],]
            )
    connect(
            processor.output[1],
            [buffer.input[1],]
            )
    component_list = [
            generator,
            buffer,
            processor
            ]
    simulator = Simulator(10, component_list)
    simulator.run()

