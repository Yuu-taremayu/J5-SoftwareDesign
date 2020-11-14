import random
import tkinter

class FIELD():
    # init field and properties
    def __init__(self):
        self.x, self.y = self.set_field()
        self.num_shop, self.num_jobchange = self.set_events()

        self.field = self.init_field(self.x, self.y, self.num_shop, self.num_jobchange)

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

    # init field array internally
    # initialize all by Normal
    # add shop and job change piont
    def init_field(self, x, y, num_shop, num_jobchange):
        field = [["Normal" for i in range(x)] for j in range(y)]
        cnt = 0
        while cnt < num_shop:
            randX = random.randrange(0, x-1)
            randY = random.randrange(0, y-1)
            if field[randX][randY] == "Normal":
                field[randX][randY] = "Shop"
                cnt += 1
        cnt = 0
        while cnt < num_jobchange:
            randX = random.randrange(0, x-1)
            randY = random.randrange(0, y-1)
            if field[randX][randY] == "Normal":
                field[randX][randY] = "JobChange"
                cnt += 1
        return field

    def print_field(self, x, y, field):
        l_field = [[None for i in range(x)] for j in range(y)]
        for i in range(x):
            for j in range(y):
                l_field[i][j] = tkinter.Label(text=field[i][j], background="red")

    # run some events on field
    # add any more events
    def event1():
        pass

f = FIELD()
print(f.field)
