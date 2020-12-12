import random
import tkinter as tk

class FIELD():
    # init field and properties
    def __init__(self,w,h,mag):
        self.x, self.y = self.set_field()
        self.WIDTH = w
        self.HEIGHT = h
        self.MAG = mag
        self.num_shop, self.num_jobchange,self.num_money = self.set_events()

        self.shop_flag = 0
        self.select_item = 0

        self.field_array = self.init_field(self.x, self.y, self.num_shop, self.num_jobchange, self.num_money)
    # set field size
    def set_field(self):
        x = 5
        y = 4
        return x, y

    # set any event num
    def set_events(self):
        num_shop = 4
        num_jobchange = 2
        num_money = 2
        return num_shop, num_jobchange, num_money

    # init field array internally
    # initialize all by Normal
    # add shop and job change piont
    def init_field(self, x, y, num_shop, num_jobchange, num_money):
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
        cnt = 0
        while cnt < num_money:
            randX = random.randrange(0, x-1)
            randY = random.randrange(0, y-1)
            if field_array[randX][randY] == "Normal":
                field_array[randX][randY] = "Money"
                cnt += 1
        return field_array

    # run some events on field
    # add any more events
    def event_increasemoney(self,player):
        before_money = player.money

        if player.job == 'Teacher':
            player.money = before_money + 500
        elif player.job == 'Engineer':
            player.money = before_money + 600
        elif player.job == 'SportsMan':
            player.money = before_money + 700
        else:
            player.money = before_money + 0
        
        msg = str(before_money) + "->" + str(player.money)
        label = tk.Label(text=msg, font=("Menlo", int(self.MAG/6)), background="yellow")
        label.place(x=self.HEIGHT/8,y=self.HEIGHT/2,anchor=tk.W)

    def event_jobchange(self,player):
        before_job = player.job
        r = random.randrange(4)
        if r == 0:
            player.job = 'Teacher'
        elif r == 1:
            player.job = 'Engineer'
        elif r == 2:
            player.job = 'SportsMan'
        else:
            player.job = 'NoJob'

        msg = before_job + "->" + player.job
        label = tk.Label(text=msg, font=("Menlo", int(self.MAG/6)), background="green")
        label.place(x=self.HEIGHT/8,y=self.HEIGHT/2,anchor=tk.W)

    def event_battle(self):
        pass

    def print_shop(self,player,pressed):
        canvas = tk.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
        canvas.place(x=0, y=0)
        l_shop = [None for i in range(player.item_num)]
        for i in range(player.item_num):
            POS = "possession:" + str(player.item[i][0]) + "\n"
            ITM = "item:" + player.item[i][1] + "\n"
            PRC = "price:" + str(player.item[i][2])
            l_shop[i] = tk.Label(text=POS+ITM+PRC, font=("Menlo", int(self.MAG/6)), background="spring green", relief="groove", borderwidth=self.MAG/10)
            l_shop[i].place(x=self.WIDTH/2+(i-2)*self.MAG*5/2,y=self.HEIGHT*3/2, width=self.MAG*3/2, height=self.MAG*3/2, anckor=tk.CENTER)

        if "Up" in pressed:
            self.select_item += 1
            self.select_item = self.select_item % (player.item_num+1)
        elif "Down" in pressed:
            self.select_item -= 1
            if self.select_item == -1:
                self.select_item = player.item_num
        elif "Return" in pressed:
            if self.select_item != player.item_num:
                player.item[self.select_item][0] += 1
            else:
                self.shop_flag = 0
        
        l_select = [None for i in range(player.item_num+1)]
        for i in range(player.item_num):
            if self.select_item == i:
                l_select[i] = tk.Label(text=player.item[i][1], font=("Menlo", int(self.MAG/6)), background="yellow")
            else:
                l_select[i] = tk.Label(text=player.item[i][1], font=("Menlo", int(self.MAG/6)), background="blue")
        if self.select_item == player.item_num:
            l_select[player.item_num] = tk.Label(text="exit", font=("Menlo", int(self.MAG/6)), background="yellow")
        else:
            l_select[player.item_num] = tk.Label(text="exit", font=("Menlo", int(self.MAG/6)), background="blue")
        

    def selct_shop(self,player):
        pass

    def event_run(self, player):
        coodinate = self.field_array[player.x][player.y]
        if coodinate == 'Money':
            self.event_increasemoney(player)
        if coodinate == 'Job\nChange':
            self.event_jobchange(player)
        if coodinate == 'Shop':
            self.shop_flag = 1
