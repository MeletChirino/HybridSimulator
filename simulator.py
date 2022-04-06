from math import inf

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
        for component in self.component_list:
            component.init()
        while(t < self.t_end):
            #find slowest tr
            tr = inf
            for component in self.component_list:
                if component.tr < tr:
                    tr = component.tr

            #create inminent components list
            inmi_components = []
            for component in self.component_list:
                if component.tr == tr:
                    inmi_components.append(component)

            t += tr
            #tr update
            for component in self.component_list:
                component.tr -= t

            # update outputs
            external_events = []
            for component in self.component_list:
                impact_list = component.generate_output()
                print(F"impact list {impact_list}")
                for impact in impact_list:
                    external_events.append(impact)

            for component in self.component_list:
                both = exist(inmi_components, component) and exist(external_events, component)
                if both:
                    component.conflict()
                elif exits(inmi_components, component):
                    component.internal()
                elif exist(external_events, component):
                    event = external_events.index(component)
                    component.external(component)











