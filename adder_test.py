# local modules
from adder import Adder4x1 as Adder
from step import Step
from tools import connect
from simulator import Simulator
from integrateur import Integrateur

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
    integrateur = Integrateur("Integrator", in_ports = 1, out_ports = 1)
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
    connect(
            adder,
            integrateur,
            adder.output[0],
            [integrateur.input[0], ]
            )
    component_list = [
            step1, step2, step3, step4,
            adder, integrateur
            ]
    #set step values
    step1.set_values(1, 1, 2)
    step2.set_values(2, 0, -3)
    step3.set_values(3, 0, -2)
    step4.set_values(4, 0, 10)
    integrateur.set_values(1/1000)

    simulator = Simulator(
            5,
            component_list = component_list
            )
    simulator.add_graph_trace(
            {
                "name": "step_data",
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
    simulator.add_graph_trace(
            {
                "name": "integrateur",
                "port": "output[0]",
                "index": 5
                }
            )

    simulator.run()
    draw_data = simulator.get_graph_data()
    time_data = simulator.get_graph_data(
            trace_name = 'time'
            )
    step_data = simulator.get_graph_data(
            trace_name = 'step_data'
            )

    plt.plot(time_data.data, step_data.data)
    plt.savefig("fig1.png")
    plt.plot(time_data.data, draw_data[3].data)
    plt.savefig("fig2.png")



