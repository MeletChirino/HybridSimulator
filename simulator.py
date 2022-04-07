# python modules
import cowsay
import matplotlib.pyplot as plt
from math import inf

# local modules
from tools import exist, Data

class Simulator:
    def __init__(self, t_end, **kwargs):
        self.t_end = t_end
        self.components_list = []
        if kwargs.get('component_list'):
            self.component_list = kwargs['component_list']
        self.graph_traces= []
        self.graph_values = []

    def add_component(self, component):
        self.component_list.append(component)

    def add_graph_trace(self, trace):
        self.graph_traces.append(trace)

    def draw_graph(self):
        print(self.graph_values)
        time = self.graph_values[0]
        values =self.graph_values[1]
        plt.stem(time, values)
        plt.show()

    def get_graph_data(self):
        data_list = []
        ind_data = Data('time', self.graph_values[0])

        data_list.append(ind_data)
        n_traces = len(self.graph_traces)
        for i in range(n_traces):
            data_list.append(
                Data(
                    self.graph_traces[i]['name'],
                    self.graph_values[i+1]
                    )
                )
        return data_list


    def run(self):
        t = 0
        print("Component init")
        for component in self.component_list:
            component.init()
        print("Component finish")

        time = []
        for trace in self.graph_traces:
            print(trace)
            exec(F"{trace['name']} = []")

        print("Component init finished")

        while(t < self.t_end):
            cowsay.milk(F"Time {t}")

            # append graph variables
            time.append(t)
            for trace in self.graph_traces:
                command = get_append_command(trace)
                exec(command)

            #find lowest tr
            print("finding lowest tr")
            tr = inf
            for component in self.component_list:
                #import pdb; pdb.set_trace()
                if component.tr < tr:
                    tr = component.tr
            print(F"lowest tr => {tr}")

            t += tr # time just increased
            #tr update
            print("Update component list")
            for component in self.component_list:
                component.tr -= tr
                component.te += tr
                print(F"{component.name}: new tr => {component.tr}")

            #create inminent components list
            print(F"Creating inminent component list")
            inmi_components = []
            for component in self.component_list:
                if component.tr == 0:
                    inmi_components.append(component)
            print(F"inmi compo = {inmi_components}")

            # update outputs
            external_events = []
            external_comp = []
            for component in inmi_components:
                impact_list = component.generate_output()
                if impact_list:
                    for impact_port in impact_list:
                        external_events.append(impact_port)
                        external_comp.append(
                                impact_port.target
                                )

            for port in external_events:
                print(F"{port.source.name} => {port.target.name}.{port.name}")

            #create ouputs and update tr
            for component in self.component_list:
                both = exist(inmi_components, component) and exist(external_events, component)
                if both:
                    component.conflict()
                    component.tr = component.avance()
                elif exist(inmi_components, component):
                    component.internal()
                    component.tr = component.avance()
                elif exist(external_comp, component):
                    index = external_comp.index(component)
                    port = external_events[index]
                    component.external(port)
                    component.tr = component.avance()
                else:
                    pass
        self.graph_values.append(time)
        for trace in self.graph_traces:
            exec(F"self.graph_values.append({trace['name']})")

    def plot_stem(self, time, values):
        plt.stem(time, values )
        plt.show()



def get_append_command(trace):
    command = F"{trace['name']}.append(self.component_list[{trace['index']}].{trace['port']}.value)"
    print(command)
    return command
