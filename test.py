import time
from classes import InPort, OutPort, Component

def connect(out_port, in_ports):
    for port in in_ports:
        out_port.attach(port)

if __name__ == "__main__":
    generator = Component(
            "Generator",
            out_ports = 2
            )
    receiver = Component(
            "receiver",
            in_ports = 3,
            out_ports = 2
            )
    processor = Component(
            "Processor",
            in_ports = 2,
            out_ports = 2
            )
    connect(
            generator.output[0],
                [
                    receiver.input[0],
                    receiver.input[1],
                    processor.input[0]
                    ]
                )
    generator.output[0].update_value(5)

    '''
    o1 = OutPort("O1")
    o2 = OutPort("O2")
    o3 = OutPort("O3")
    i1 = InPort("I1")
    i2 = InPort("I2")
    i3 = InPort("I3")
    i4 = InPort("I4")
    i5 = InPort("I5")
    i6 = InPort("I6")

    connect(o1, (i1, i2, i3))
    connect(o2, (i4, i5))
    connect(o3, (i6,))

    o1.update_value(5)
    o2.update_value(2)
    time.sleep(2)
    o1.update_value(1)
    o3.update_value(2)
    time.sleep(2)
    connect(o1, (i4, i5))
    o1.update_value(7)
    '''

