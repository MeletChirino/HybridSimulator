# local modules
from components.arithmetics import Adder4x1 as Adder
from components.signals import Step
from components.ode import Integrateur
from kernel.tools import connect, Log
from kernel.simulator import Simulator

# python modules
import matplotlib.pyplot as plt
import os

def main():
    #initialize components
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
            # out port
            (step1, 0),
            #in ports
            (adder, 0)
            )
    connect(
            # out port
            (step2, 0),
            (adder, 1)
            )
    connect(
            # out port
            (step3, 0),
            (adder, 2)
            )
    connect(
            # out port
            (step4, 0),
            (adder, 3)
            )
    connect(
            # out port
            (adder, 0),
            (integrateur, 0)
            )
    component_list = [
            step1, step2, step3, step4,
            adder, integrateur
            ]
    #set step values
    # IMPORTANT values must be set after connection
    step1.set_values(1, 1, 2)
    step2.set_values(2, 0, -9)
    step3.set_values(7, 2, -2)
    step4.set_values(4, 0, 10)
    integrateur.set_values(1/1000)
    # log object
    log_ = Log(
            debug_mode = True
            )

    # --- Starting simulator ---
    simulator = Simulator(
            10,
            log = log_,
            component_list = component_list
            )
    simulator.add_graph_trace(
            {
                "name": "step_data",
                "port": "output[0]",
                "component": adder,
                }
            )
    simulator.add_graph_trace(
            {
                "name": "integrateur",
                "port": "output[0]",
                "component": integrateur,
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
    integrated_data = simulator.get_graph_data(
            trace_name = 'integrateur'
            )

    plt.plot(
            time_data.data,
            step_data.data,
            label = 'Added steps'
            )
    plt.plot(
            time_data.data,
            integrated_data.data,
            label = 'Integrated Data'
            )
    plt.title('Hybrid Simulator')
    plt.legend()
    test_path = os.path.dirname(__file__)
    file_name = 'fig.png'
    file_path = F'{test_path}/img/{file_name}'
    plt.savefig(file_path)
    plt.show()

