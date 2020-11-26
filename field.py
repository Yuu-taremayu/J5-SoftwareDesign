import random
import tkinter

class FIELD():
    # init field and properties
    def __init__(self,w,h):
        self.x, self.y = self.set_field()
        self.WIDTH = w
        self.HEIGHT = h
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
        field_array = [["Normal" for j in range(y)] for i in range(x)]
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
                field_array[randX][randY] = "Job\nChange"
                cnt += 1
        return field_array

    # run some events on field
    # add any more events
    def event_increasemoney(self,money,job):
        before_money = money
        if job == 'Teacher':
            after_money = before_money + 500
        elif job == 'Engineer':
            after_money = before_money + 600
        elif job == 'SportsMan':
            after_money = before_money + 700
        else:
            after_money = before_money + 0

        l_before = tkinter.Label(text=str(before_money),background="yellow")
        l_after = tkinter.Label(text=str(after_money),background="yellow")
        l_right = tkinter.Label(text="=>",background="yellow")
        l_right.place(x=self.WIDTH/2, y=self.HEIGHT/2-100, anchor=tkinter.N)
        l_before.place(x=self.WIDTH/2-40, y=self.HEIGHT/2-100, anchor=tkinter.N)
        l_after.place(x=self.WIDTH/2+40, y=self.HEIGHT/2-100, anchor=tkinter.N)
