class Computer:

    def __init__(self, tape=[], init_pos=0):
        self.tape = tape
        self.tape_position = init_pos

    def transition_table(self):
        self.tape_position += 1

    def read_bit(self):
        return self.tape[self.tape_position]

    def write_bit(self, new_bit):
        self.tape[self.tape_position] = new_bit
