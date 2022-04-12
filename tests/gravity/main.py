# local modules
from components.arithmetics import Adder4x1 as Adder
from components.signals import Step, Constant
from components.ode import Integrateur
from components.conditions import Switch
from kernel.tools import connect, Log
from kernel.simulator import Simulator

# python modules
import matplotlib.pyplot as plt
import os
from math import inf

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
    # constants 
    constant2 = Constant(
            "Constant2",
            out_ports = 1,
            )
    constant4 = Constant(
            "Constant4",
            out_ports = 1,
            )
    constant6 = Constant(
            "Constant6",
            out_ports = 1,
            )
    switch = Switch(
            "Switch",
            in_ports = 4,
            out_ports = 1
            )
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
            (switch, 0)
            )
    connect(
            (constant2, 0),
            (switch, 1),
            )
    connect(
            (constant4, 0),
            (switch, 2),
            )
    connect(
            (constant6, 0),
            (switch, 3),
            )

    component_list = [
            step1, step2, step3, step4,
            adder, constant2, constant4,
            constant6, switch
            ]
    #set step values
    # IMPORTANT values must be set after connection
    step1.set_values(1, 0, 2)
    step2.set_values(2, 0, 23)
    step3.set_values(4, 2, -22)
    step4.set_values(6, 0, 10)
    constant2.set_values(2)
    constant4.set_values(4)
    constant6.set_values(6)
    switch.set_intervals(
           (inf, 10),
           (10, 0),
           (0, -inf),
           )
    # log object
    log_ = Log(
            debug_mode = False
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
                "index": 4
                }
            )
    simulator.add_graph_trace(
            {
                "name": "switch",
                "port": "output[0]",
                "index": 8
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
            trace_name = 'switch'
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

