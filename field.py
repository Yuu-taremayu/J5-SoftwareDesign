import random

class FIELD():
    # init field and properties
    def __init__(self):
        self.x, self.y = self.set_field()
        self.num_shop, self.num_jobchange = self.set_events()

        self.field_array = self.init_field(self.x, self.y, self.num_shop, self.num_jobchange)

    # set field size
    def set_field(self):
        x = 5
        y = 4
        return x, y

    # set any event num
    def set_events(self):
        num_shop = 4
        num_jobchange = 2
        return num_shop, num_jobchange

    # init field array internally
    # initialize all by Normal
    # add shop and job change piont
    def init_field(self, x, y, num_shop, num_jobchange):
        field_array = [["Normal" for i in range(x)] for j in range(y)]
        cnt = 0
        while cnt < num_shop:
            randX = random.randrange(0, x-1)
            randY = random.randrange(0, y-1)
            if field_array[randX][randY] == "Normal":
                field_array[randX][randY] = "Shop"
                cnt += 1
        cnt = 0
        while cnt < num_jobchange:
            randX = random.randrange(0, x-1)
            randY = random.randrange(0, y-1)
            if field_array[randX][randY] == "Normal":
                field_array[randX][randY] = "JobChange"
                cnt += 1
        return field_array

    # run some events on field
    # add any more events
    def event1():
        pass
