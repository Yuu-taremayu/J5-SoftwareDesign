class FIELD():
    # init field and properties
    def __init__(self):
        self.x, self.y = self.set_field()
        self.num_shop, self.num_jobchange = set_event()

    # set field size
    def set_field(self):
        x = int(input('input x'))
        y = int(input('input y'))
        return x, y

    # set any event num
    def set_events(self):
        num_shop = 4
        num_jobchange = 2
        return num_shop, num_jobchange

    # run some events on field
    # add any more events
    def event1():
        pass
