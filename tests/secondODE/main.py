 # local modules
from components.arithmetics import Adder4x1 as Adder
from components.signals import Constant
from components.ode import Integrateur
from components.ode import Integrateur_ed
from kernel.tools import connect, Log
from kernel.simulator import Simulator

# python modules
import matplotlib.pyplot as plt
import os

def main():
    constant_g = Constant("gravity", out_ports = 1)
    constant_h = Constant("height", out_ports = 1)
    #initialize components
    #integrateur_v = Integrateur("Integrator dv", in_ports = 1, out_ports = 1)
    #integrateur_h = Integrateur("Integrator dh", in_ports = 2, out_ports = 1)

    integrateur_v = Integrateur_ed("Integrator dv", in_ports = 1, out_ports = 1)
    integrateur_h = Integrateur_ed("Integrator dh", in_ports = 2, out_ports = 1)

    # connect components
    connect(
            # out port
            (constant_g, 0),
            #in ports
            (integrateur_v, 0)
            )
    connect(
            # out port
            (integrateur_v, 0),
            #in ports
            (integrateur_h, 0)
            )
    connect(
            # out port
            (constant_h, 0),
            #in ports
            (integrateur_h, 1)
            )
    component_list = [constant_g, constant_h, 
                    integrateur_v, integrateur_h]
    #set step values
    # IMPORTANT values must be set after connection
    constant_g.set_values(-9.8)
    constant_h.set_values(10.0)
    integrateur_v.set_values(1/1000)
    integrateur_h.set_values(1/1000)
    # log object
    log_ = Log(
            debug_mode = False
            )

    # --- Starting simulator ---
    simulator = Simulator(
            5,
            log = log_,
            component_list = component_list
            )
    simulator.add_graph_trace(
            {
                "name": "integrateur_h_out",
                "port": "output[0]",
                "index": 3
                }
            )
    simulator.add_graph_trace(
            {
                "name": "integrateur_h_in",
                "port": "input[0]",
                "index": 3
                }
            )
    
    simulator.add_graph_trace(
            {
                "name": "integrateur_h_in1",
                "port": "input[1]",
                "index": 3
                }
            )

    simulator.run()
    time_data = simulator.get_graph_data(
            trace_name = 'time'
            )
    integrated_hdata = simulator.get_graph_data(
            trace_name = 'integrateur_h_out'
            )
    integrated_vdata = simulator.get_graph_data(
            trace_name = 'integrateur_h_in'
            )
    plt.plot(
            time_data.data,
            integrated_hdata.data,
            label = 'Integrated_h Data'
            )
    plt.plot(
            time_data.data,
            integrated_vdata.data,
            label = 'Integrated_v Data'
            )
    plt.title('Hybrid Simulator')
    plt.legend()
    test_path = os.path.dirname(__file__)
    file_name = 'fig.png'
    file_path = F'{test_path}/img/{file_name}'
    plt.savefig(file_path)
    plt.show()
