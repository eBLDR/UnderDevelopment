"""
...
"""


# --- A PIECE OF CABLE ---

class Cable:

    def __init__(self, origin=None, *end_points):
        self.origin = origin                                # Cable's origin point
        self.end = [end_point for end_point in end_points]  # Cable's ending point/s
        self.value_transported = None

    def plug(self):
        for end_point in self.end:
            assert self.origin.level != end_point.level, "Cannot plug a cable from and to the same level."
        self.origin.cables_out.append(self)
        print("Origin of cable {0} plugged at {0.origin}.".format(self))
        for end_point in self.end:
            end_point.cables_in.append(self)
            print("End of cable {0} plugged at {1}.".format(self, end_point))

    def transport(self, value):
        self.value_transported = value
        print("Transporting value {0.value_transported} in cable {0}.".format(self))


# --- NPN TRANSISTOR ---

class Transistor:

    def __init__(self):
        self.collector = 1
        self.base = 0
        self.emitter = 0

    def activate(self):
        self.base = 1
        self.update()

    def deactivate(self):
        self.base = 0
        self.update()

    def update(self):
        self.emitter = self.base


# --- CIRCUIT ---

class Circuit:

    def __init__(self, name=''):
        self.name = "Circuit-" + name
        self.cables = []
        self.components = {}
        self.levels_used = set()

    def get_deeper_level(self):
        return max(self.levels_used)

    def assemble_components(self, *components):
        def insert_component(component):
            if component.level not in self.levels_used:
                self.levels_used.add(component.level)
                self.components[component.level] = []

            self.components[component.level].append(component)
            print("Placed {0} in {1}".format(component, self.name))

        collectors = []
        # Collectors are assembled last
        for component in components:
            if isinstance(component, Collector):
                collectors.append(component)
                continue

            insert_component(component)

        for collector in collectors:
            collector.set_level(self.levels_used)
            insert_component(collector)

    def assemble_cables(self, *cables):
        for cable in cables:
            cable.plug()
            self.cables.append(cable)

    def operate(self):
        for level in sorted(self.levels_used):
            for component in self.components[level]:
                component.operate()


# --- COMPONENT ---

class Component:

    def __init__(self, level=None):
        self.level = level
        self.name = ""
        self.structure = []  # Internal structure
        self.cables_in = []
        self.cables_out = []
        self.expected_inputs = 0   # Number of inputs needed to operate
        self.input = []
        self.output = None

    def __str__(self):
        return "{0.name} at level {0.level}".format(self)

    def receive_input(self):
        assert self.expected_inputs == len(self.cables_in),\
            "INVALID INPUT - {0} has {1} input/s - expected: {0.expected_inputs}".format(self, len(self.cables_in))
        self.input = [cable.value_transported for cable in self.cables_in]

    def send_output(self):
        for cable in self.cables_out:
            cable.transport(self.output)

    @staticmethod
    def operate(task):
        def wrapper(self):
            if len(self.cables_in) != 0:
                self.receive_input()

            task(self)

            if len(self.cables_out) != 0:
                self.send_output()

        return wrapper


# --- SOURCE ---

class Source(Component):

    def __init__(self):
        super().__init__()
        self.name = "Source-[{}]".format(str(self.output))
        self.level = 0  # Sources are always placed at circuit's level 0

    def set_value(self, value):
        # Value to be sent
        assert value == 0 or value == 1, "Source can only send {0, 1} values."
        self.output = value
        self.name = "Source-[{}]".format(str(self.output))

    @Component.operate
    def operate(self):
        # self.receive_input()
        print("Activated source of value {0.output} from {0}.".format(self))
        # self.send_output()


# --- OUTPUT COLLECTOR ---

class Collector(Component):

    def __init__(self):
        super().__init__()
        self.name = "Collector"
        self.expected_inputs = 1

    def set_level(self, levels):
        self.level = max(levels) + 1  # Collectors are always placed at circuit's last level

    @Component.operate
    def operate(self):
        print("Collected value {0.input} by {0}.".format(self))


# --- GATES ---

class LogicGate(Component):

    def __init__(self, level=None):
        super().__init__(level)
        self.name = "LogicGate-"
        self.transition_table = {}

    @Component.operate
    def operate(self):
        # self.receive_input()

        self.output = self.transition_table.get(
            ''.join([str(i) for i in self.input]), "INVALID INPUT")

        print("Operated output {0.output} with a given input {0.input} by {0}.".format(self))

        # self.send_output()


class SingleInputGate(LogicGate):

    def __init__(self, level=None):
        super().__init__(level)
        self.expected_inputs = 1


class DoubleInputGate(LogicGate):

    def __init__(self, level=None):
        super().__init__(level)
        self.expected_inputs = 2


# "BRIDGE Gate" - does nothing
class BRIDGE(SingleInputGate):

    def __init__(self):
        super().__init__()
        self.name += "Bridge"
        self.level = 0
        self.transition_table = {"0": 0,
                                 "1": 1}


# Negation
class NOT(SingleInputGate):

    def __init__(self, level=None):
        super().__init__(level)
        self.name += "NOT"
        self.structure = [Transistor()]
        self.transition_table = {"0": 1,
                                 "1": 0}


# Conjunction
class AND(DoubleInputGate):

    def __init__(self, level=None):
        super().__init__(level)
        self.name += "AND"
        self.structure = [Transistor(), Transistor()]
        self.transition_table = {"00": 0,
                                 "01": 0,
                                 "10": 0,
                                 "11": 1}


# Disjunction
class OR(DoubleInputGate):

    def __init__(self, level=None):
        super().__init__(level)
        self.name += "OR"
        self.structure = [Transistor(), Transistor()]
        self.transition_table = {"00": 0,
                                 "01": 1,
                                 "10": 1,
                                 "11": 1}


# # Exclusive disjunction
# class XOR(DoubleInputGate):
#
#     def __init__(self, level=None):
#         super().__init__(level)
#         self.name += "XOR"
#         self.structure = [Transistor(), Transistor()]
#         self.transition_table = {"00": 0,
#                                  "01": 1,
#                                  "10": 1,
#                                  "11": 0}

class DoubleNOT(Component):
    def __init__(self, level):
        super().__init__(level=level)
        self.name = "DoubleNot"
        self.expected_inputs = 1
        self.structure = self.assemble_intern_circuit()

    @staticmethod
    def assemble_intern_circuit():

        intern_circuit = Circuit("DoubleNot")
        p = Source()
        n1 = NOT(1)
        n2 = NOT(2)
        c1 = Cable(p, n1)
        c2 = Cable(n1, n2)
        e = Collector()
        c3 = Cable(n2, e)
        intern_circuit.assemble_components(p, n1, n2, e)
        intern_circuit.assemble_cables(c1, c2, c3)
        return intern_circuit

    @Component.operate
    def operate(self):
        for value, source in zip(self.input, self.structure.components[0]):
            source.set_value(value)

        self.structure.operate()

        self.output = self.structure.components[self.structure.get_deeper_level()][0].input[0]


MAIN = Circuit("MAIN")
s = Source()
s.set_value(1)
A = DoubleNOT(1)
cm = Cable(s, A)
n = NOT(2)
cm2 = Cable(A, n)
e = Collector()
ce = Cable(n, e)
MAIN.assemble_components(e, s, A, n)
MAIN.assemble_cables(cm, cm2, ce)
MAIN.operate()

"""
C = Circuit("XOR Gate")

A = Source()
B = Source()

a1 = AND(1)
o1 = OR(1)
n2 = NOT(2)
a2 = AND(3)

c01 = Cable(A, a1, o1)
c01_1 = Cable(B, a1, o1)
c12 = Cable(a1, n2)
c13 = Cable(o1, a2)
c23 = Cable(n2, a2)

C.assemble_components(A, B, a1, o1, n2, a2)
C.assemble_cables(c01, c01_1, c12, c13, c23)

A.set_value(1)
B.set_value(0)

C.operate()
"""
