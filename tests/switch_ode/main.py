 
 # local modules
from components.arithmetics import Adder4x1 as Adder
from components.signals import Constant
from components.conditions import MoonlightSwitch
from components.ode import Integrateur
from kernel.tools import connect, Log
from kernel.simulator import Simulator

# python modules
import matplotlib.pyplot as plt
import os

def main():
    constant_g = Constant("gravity", out_ports = 1)
    constant_h = Constant("height", out_ports = 1)
    constant_0 = Constant("threshold", out_ports = 1)
    #initialize components
    integrateur_v = Integrateur("Integrator dv", in_ports = 2, out_ports = 1)
    integrateur_h = Integrateur("Integrator dh", in_ports = 2, out_ports = 1)
    switch = MoonlightSwitch(
            "ConditionalSwitch",
            in_ports = 3,
            out_ports = 1
            )

    # connect components
    connect(
            (constant_0, 0),
            (switch, 1)
            )
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
            (integrateur_h, 0),
            (switch, 2)
            )
    connect(
            # out port
            (constant_h, 0),
            #in ports
            (integrateur_h, 1)
            )
    connect(
            (integrateur_h, 0),
            (switch, 0)
            )
    connect(
            (switch, 0),
            (integrateur_v, 1)
            )
    component_list = [constant_g, constant_h,
                    integrateur_v, integrateur_h,
                    switch]
    #set step values
    # IMPORTANT values must be set after connection
    constant_g.set_values(-9.8)
    constant_h.set_values(10.0)
    constant_0.set_values(0)
    switch.set_coeff(-0.8)
    switch.set_init_val(0)

    integrateur_v.set_values(7/1000)
    integrateur_h.set_values(7/1000)
    # log object
    log_ = Log(
            debug_mode = True
            )

    # --- Starting simulator ---
    simulator = Simulator(
            12,
            log = log_,
            component_list = component_list
            )
    simulator.add_graph_trace(
            {
                "name": "integrateur_h_out",
                "port": "output[0]",
                "component": integrateur_h,
                }
            )
    simulator.add_graph_trace(
            {
                "name": "integrateur_h_in",
                "port": "input[0]",
                "component": integrateur_h,
                }
            )

    simulator.add_graph_trace(
            {
                "name": "integrateur_h_in1",
                "port": "input[1]",
                "component": integrateur_h,
                }
            )
    simulator.add_graph_trace(
            {
                "name": "switch_out",
                "port": "output[0]",
                "component": switch,
                }
            )
    simulator.add_graph_trace(
            {
                "name": "switch_in0",
                "port": "input[0]",
                "component": switch,
                }
            )
    simulator.add_graph_trace(
            {
                "name": "switch_in1",
                "port": "input[1]",
                "component": switch,
                }
            )
    simulator.add_graph_trace(
            {
                "name": "switch_in2",
                "port": "input[2]",
                "component": switch,
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
    switch_data = simulator.get_graph_data(
            trace_name = 'switch_out'
            )
    switch_in_data = simulator.get_graph_data(
            trace_name = 'switch_in0'
            )
    switch_in1_data = simulator.get_graph_data(
            trace_name = 'switch_in1'
            )
    switch_in2_data = simulator.get_graph_data(
            trace_name = 'switch_in2'
            )
    plt.plot(
            time_data.data,
            integrated_hdata.data,
            label = 'Integrated_h Data'
            )
    plt.title('Height Vs Time')
    plt.legend()
    test_path = os.path.dirname(__file__)
    file_name = 'height.png'
    file_path = F'{test_path}/img/{file_name}'
    plt.savefig(file_path)
    plt.show()
    plt.plot(
            time_data.data,
            integrated_hdata.data,
            label = 'Height'
            )
    plt.plot(
            time_data.data,
            integrated_vdata.data,
            label = 'Velocity'
            )
    plt.plot(
            time_data.data,
            switch_data.data,
            label = 'Out Switch Data'
            )
    '''
    plt.plot(
            time_data.data,
            switch_in1_data.data,
            label = 'In1 Switch Data'
            )
    plt.plot(
            time_data.data,
            switch_in_data.data,
            label = 'In0 Switch Data'
            )
    plt.plot(
            time_data.data,
            switch_in2_data.data,
            label = 'In2 Switch Data'
            )
             '''
    plt.title('Hybrid Simulator')
    plt.legend()
    test_path = os.path.dirname(__file__)
    file_name = 'fig.png'
    file_path = F'{test_path}/img/{file_name}'
    plt.savefig(file_path)
    plt.show()
