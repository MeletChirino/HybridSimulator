# local modules
from adder import Adder4x1 as Adder
from step import Step
from tools import connect
from simulator import Simulator

# python modules
import matplotlib.pyplot as plt

if __name__ == "__main__":
    adder = Adder(
            "Adder4x1",
            in_ports = 4,
            out_ports = 1,
            )
    step1 = Step(
            "Step_1",
            out_ports = 1
            )
    step2 = Step(
            "Step_2",
            out_ports = 1
            )
    step3 = Step(
            "Step_3",
            out_ports = 1
            )
    step4 = Step(
            "Step_4",
            out_ports = 1
            )
    # connect components
    connect(
            step1,
            adder,
            step1.output[0],
            [adder.input[0], ]
            )
    connect(
            step2,
            adder,
            step2.output[0],
            [adder.input[1], ]
            )
    connect(
            step3,
            adder,
            step3.output[0],
            [adder.input[2], ]
            )
    connect(
            step4,
            adder,
            step4.output[0],
            [adder.input[3], ]
            )
    component_list = [
            step1, step2, step3, step4,
            adder
            ]
    #set step values
    step1.set_values(1, 0, 1)
    step2.set_values(4, 0, 1)
    step3.set_values(1, 0, 1)
    step4.set_values(3, 0, 2)

    simulator = Simulator(
            7,
            component_list = component_list
            )
    simulator.add_graph_trace(
            {
                "name": "final_value",
                "port": "output[0]",
                "index": 4
                }
            )
    simulator.add_graph_trace(
            {
                "name": "step2",
                "port": "output[0]",
                "index": 1
                }
            )

    simulator.run()
    draw_data = simulator.get_graph_data()

    plt.stem(draw_data[0].data, draw_data[1].data)
    plt.show()


