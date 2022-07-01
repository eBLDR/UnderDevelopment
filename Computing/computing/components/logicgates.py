from computing.helpers import exceptions


class LogicGate:
    def __init__(self, name):
        self.name = 'LogicGate-{}'.format(name)
        self.input = []
        self.output = None
        self.transition_table = {}

    def translate_input(self):
        return ''.join([str(i) for i in self.input])

    def operate(self):
        try:
            self.output = self.transition_table[self.translate_input()]
        except KeyError:
            raise exceptions.InputError


class NOT(LogicGate):
    def __init__(self):
        super().__init__('NOT')
        self.transition_table = {'0': 1,
                                 '1': 0}


class OR(LogicGate):
    def __init__(self):
        super().__init__('OR')
        self.transition_table = {'00': 0,
                                 '01': 1,
                                 '10': 1,
                                 '11': 1}


class AND(LogicGate):
    def __init__(self):
        super().__init__('AND')
        self.transition_table = {'00': 0,
                                 '01': 0,
                                 '10': 0,
                                 '11': 1}
