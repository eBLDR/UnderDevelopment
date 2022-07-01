from computing.components import logicgates


class DerivedLogicGate:
    def __init__(self, name):
        self.name = 'DerivedLogicGate-{}'.format(name)
        self.input = []
        self.output = None
        self.structure = None


class NOR(DerivedLogicGate):
    def __init__(self):
        super().__init__('NOR')
        # self.structure = 
