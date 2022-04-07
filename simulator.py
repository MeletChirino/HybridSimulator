import cowsay
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
        print("Component init finished")

        while(t < self.t_end):
            cowsay.milk(F"Time {t}")

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
            print(F"inminent component list => {inmi_components}")

            # update outputs
            external_events = []
            external_comp = []
            for component in inmi_components:
                impact_list = component.generate_output()
                print(F"impact list {impact_list}")
                #import pdb; pdb.set_trace()
                if impact_list:
                    for impact_port in impact_list:
                        external_events.append(impact_port)
                        external_comp.append(
                                impact_port.target
                                )

            print(F"extern component list => {external_comp}")
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
