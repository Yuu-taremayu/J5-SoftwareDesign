class FIELD():
    # init field and properties
    def __init__(self):
        self.x, self.y = self.set_field()
        print('test')

    # set field size
    def set_field(self):
        x = int(input('input x'))
        y = int(input('input y'))
        return x, y

    # run some events on field
    # add any more events
    def event1():
        pass
