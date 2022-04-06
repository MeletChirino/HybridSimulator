from math import inf
from tools import exist

class Simulator:
    def __init__(self, t_end, **kwargs):
        self.t_end = t_end
        self.components_list = []
        if kwargs.get('component_list'):
            self.component_list = kwargs['component_list']

    def add_component(self, component):
        self.component_list.append(component)

    def run(self):
        t = 0
        print("Component init")
        for component in self.component_list:
            component.init()
        print("Component finish")
        while(t < self.t_end):
            print(F"---- Time {t} ----")
            #find slowest tr
            print("finding lowest tr")
            tr = inf
            for component in self.component_list:
                if component.tr < tr:
                    tr = component.tr
            print(F"lowest tr => {tr}")

            #create inminent components list
            print(F"Creating inminent component list")
            inmi_components = []
            for component in self.component_list:
                if component.tr == tr:
                    inmi_components.append(component)
            print(F"component list => {self.component_list}")

            t += tr
            #tr update
            print("Update component list")
            for component in self.component_list:
                component.tr -= t
                print(F"{component}: new tr => {component.tr}")

            # update outputs
            external_events = []
            external_comp = []
            for component in self.component_list:
                impact_list = component.generate_output()
                print(F"impact list {impact_list}")
                #|import pdb; pdb.set_trace()
                if impact_list:
                    for impact_port in impact_list:
                        external_events.append(impact_port)
                        external_comp.append(
                                impact_port.target
                                )

            for component in self.component_list:
                both = exist(inmi_components, component) and exist(external_events, component)
                if both:
                    component.conflict()
                elif exist(inmi_components, component):
                    component.internal()
                elif exist(external_comp, component):
                    index = external_comp.index(component)
                    port = external_events[index]
                    #import pdb; pdb.set_trace()
                    component.external(port)











