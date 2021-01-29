import random
import tkinter as tk


class FIELD:
    # init field and properties
    def __init__(self, w, h, mag):
        self.x, self.y = self.set_field()
        self.WIDTH = w
        self.HEIGHT = h
        self.MAG = mag
        self.num_shop, self.num_jobchange, self.num_work = self.set_events()

        self.shop_flag = 0
        self.useitem_flag = 0
        self.select_item = 0
        self.cantbuy_flag = 0
        self.donthave_flag = 0

        self.field_array = self.init_field(
            self.x, self.y, self.num_shop, self.num_jobchange, self.num_work
        )

    # set field size
    def set_field(self):
        x = 5
        y = 4
        return x, y

    # set any event num
    def set_events(self):
        num_shop = 3
        num_jobchange = 2
        num_work = 4
        return num_shop, num_jobchange, num_work

    # init field array internally
    # initialize all by Normal
    # add shop and job change piont
    def init_field(self, x, y, num_shop, num_jobchange, num_work):
        field_array = [["Normal" for j in range(y)] for i in range(x)]

        cnt = 0
        while cnt < num_shop:
            randX = random.randrange(0, x - 1)
            randY = random.randrange(0, y - 1)
            if field_array[randX][randY] == "Normal":
                field_array[randX][randY] = "Shop"
                cnt += 1

        cnt = 0
        while cnt < num_jobchange:
            randX = random.randrange(0, x - 1)
            randY = random.randrange(0, y - 1)
            if field_array[randX][randY] == "Normal":
                field_array[randX][randY] = "Job\nChange"
                cnt += 1

        cnt = 0
        while cnt < num_work:
            randX = random.randrange(0, x - 1)
            randY = random.randrange(0, y - 1)
            if field_array[randX][randY] == "Normal":
                field_array[randX][randY] = "Work"
                cnt += 1

        return field_array

    # run some events on field
    # add any more events
    def event_work(self, player):
        before_money = player.money
        before_stress = player.stress

        updown = random.randint(0, 1)
        if updown == 0:
            if player.job == "Teacher":
                player.money = before_money + 500
                player.stress = before_stress + 50
            elif player.job == "Engineer":
                player.money = before_money + 600
                player.stress = before_stress + 100
            elif player.job == "SportsMan":
                player.money = before_money + 700
                player.stress = before_stress + 150
            else:
                player.money = before_money + 0
        else:
            down = random.randint(1, 3) * 50
            if player.money >= down:
                player.money -= down
                player.stress = before_stress + 200
            else:
                player.money = 0
            player.bad_event += 1

        m_msg = str(before_money) + "->" + str(player.money)
        s_msg = str(before_stress) + "->" + str(player.stress)
        label = tk.Label(
            text=m_msg + "\n" + s_msg, font=("Menlo", int(self.MAG / 6)), background="yellow"
        )
        label.place(x=self.HEIGHT / 8, y=self.HEIGHT / 2, anchor=tk.W)

    def event_jobchange(self, player):
        before_job = player.job

        r = random.randrange(4)
        if r == 0:
            player.job = "Teacher"
        elif r == 1:
            player.job = "Engineer"
        elif r == 2:
            player.job = "SportsMan"
        else:
            player.job = "NoJob"

        msg = before_job + "->" + player.job
        label = tk.Label(
            text=msg, font=("Menlo", int(self.MAG / 6)), background="green"
        )
        label.place(x=self.HEIGHT / 8, y=self.HEIGHT / 2, anchor=tk.W)

    # print shop event
    def print_shop(self, player):
        canvas = tk.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
        canvas.place(x=0, y=0)

        l_title = tk.Label(
            text="SHOP", font=("Menlo", int(self.MAG / 4)), background="green"
        )
        l_title.place(x=self.WIDTH / 2, y=0, width=self.MAG * 2, height=self.MAG / 3)

        # money of player
        msg = "your money : " + str(player.money)
        l_money = tk.Label(
            text=msg, font=("Menlo", int(self.MAG / 6)), background="yellow"
        )
        l_money.place(
            x=self.WIDTH / 10 * 8,
            y=self.HEIGHT / 10,
            width=self.MAG * 2,
            height=self.MAG / 3,
        )

        # item information
        l_shop = [None for i in range(player.item_num)]
        for i in range(player.item_num):
            ITM = "item:" + player.item[i][1] + "\n"
            POS = "possession:" + str(player.item[i][0]) + "\n"
            PRC = "price:" + str(player.item[i][2])
            l_shop[i] = tk.Label(
                text=POS + ITM + PRC,
                font=("Menlo", int(self.MAG / 6)),
                background="spring green",
            )
            l_shop[i].place(
                x=self.WIDTH / 2 + (i - 2) * self.MAG * 5 / 2,
                y=self.HEIGHT / 10 * 2,
                width=self.MAG * 2,
                height=self.MAG,
                anchor=tk.CENTER,
            )

        # print select item
        l_select = [None for i in range(player.item_num + 1)]
        for i in range(player.item_num):
            if self.select_item == i:
                l_select[i] = tk.Label(
                    text=player.item[i][1],
                    font=("Menlo", int(self.MAG / 6)),
                    background="yellow",
                )
            else:
                l_select[i] = tk.Label(
                    text=player.item[i][1],
                    font=("Menlo", int(self.MAG / 6)),
                    background="blue",
                )
        if self.select_item == player.item_num:
            l_select[player.item_num] = tk.Label(
                text="exit", font=("Menlo", int(self.MAG / 6)), background="yellow"
            )
        else:
            l_select[player.item_num] = tk.Label(
                text="exit", font=("Menlo", int(self.MAG / 6)), background="blue"
            )

        # print "Can't buy"
        if self.cantbuy_flag == 1:
            l_cannot = tk.Label(
                text="Can't buy it", font=("Menlo", int(self.MAG / 5)), background="red"
            )
            l_cannot.place(
                x=self.WIDTH / 10 * 7,
                y=self.HEIGHT / 2,
                width=self.MAG * 2,
                height=self.MAG / 2,
                anchor=tk.CENTER,
            )
            self.cantbuy_flag = 0

        for i in range(player.item_num + 1):
            l_select[i].place(
                x=self.WIDTH / 10 * 5,
                y=self.HEIGHT / 10 * 4 + (i * self.MAG / 2),
                width=self.MAG * 2,
                height=self.MAG / 3,
                anchor=tk.CENTER,
            )

    # buy item
    def select_shop(self, player, pressed):
        if "Down" in pressed:
            self.select_item += 1
            self.select_item = self.select_item % (player.item_num + 1)
        elif "Up" in pressed:
            self.select_item -= 1
            if self.select_item == -1:
                self.select_item = player.item_num
        elif "Return" in pressed:
            if self.select_item != player.item_num:
                if player.money >= player.item[self.select_item][2]:
                    player.item[self.select_item][0] += 1
                    player.money -= player.item[self.select_item][2]
                else:
                    self.cantbuy_flag = 1
            else:
                self.select_item = 0
                self.shop_flag = 0
                return 0

    def print_use_item(self, player):
        canvas = tk.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
        canvas.place(x=0, y=0)

        l_title = tk.Label(
            text="ITEM", font=("Menlo", int(self.MAG / 4)), background="steel blue"
        )
        l_title.place(x=self.WIDTH / 2, y=0, width=self.MAG * 2, height=self.MAG / 3)

        # status of player
        NAM = str(player.name) + "\n"
        MUS = "muscle:" + str(player.muscle) + "\n"
        STR = "stress:" + str(player.stress) + "\n"
        DEX = "dexterity:" + str(player.dexterity)
        l_stat = tk.Label(
            text=NAM + MUS + STR + DEX,
            font=("Menlo", int(self.MAG / 6)),
            background="white",
        )
        l_stat.place(
            x=0, y=0, width=self.MAG * 3 / 2, height=self.MAG * 3 / 2, anchor=tk.NW
        )
        # item information
        l_item = [None for i in range(player.item_num)]
        for i in range(player.item_num):
            ITM = "item:" + player.item[i][1] + "\n"
            POS = "possession:" + str(player.item[i][0]) + "\n"
            DSC = "descripton:" + player.item[i][3]
            l_item[i] = tk.Label(
                text=ITM + POS + DSC,
                font=("Menlo", int(self.MAG / 6)),
                background="spring green",
            )
            l_item[i].place(
                x=self.WIDTH / 2 + (i - 2) * self.MAG * 6 / 2,
                y=self.HEIGHT / 10 * 2,
                width=self.MAG * 3,
                height=self.MAG,
                anchor=tk.CENTER,
            )
        # print select item
        l_select = [None for i in range(player.item_num + 1)]
        for i in range(player.item_num):
            if self.select_item == i:
                l_select[i] = tk.Label(
                    text=player.item[i][1],
                    font=("Menlo", int(self.MAG / 6)),
                    background="yellow",
                )
            else:
                l_select[i] = tk.Label(
                    text=player.item[i][1],
                    font=("Menlo", int(self.MAG / 6)),
                    background="blue",
                )
        if self.select_item == player.item_num:
            l_select[player.item_num] = tk.Label(
                text="exit", font=("Menlo", int(self.MAG / 6)), background="yellow"
            )
        else:
            l_select[player.item_num] = tk.Label(
                text="exit", font=("Menlo", int(self.MAG / 6)), background="blue"
            )
        # print "Can't buy"
        if self.donthave_flag == 1:
            l_cannot = tk.Label(
                text="Don't have it",
                font=("Menlo", int(self.MAG / 5)),
                background="red",
            )
            l_cannot.place(
                x=self.WIDTH / 10 * 7,
                y=self.HEIGHT / 2,
                width=self.MAG * 2,
                height=self.MAG / 2,
                anchor=tk.CENTER,
            )
            self.donthave_flag = 0
        for i in range(player.item_num + 1):
            l_select[i].place(
                x=self.WIDTH / 10 * 5,
                y=self.HEIGHT / 10 * 4 + (i * self.MAG / 2),
                width=self.MAG * 2,
                height=self.MAG / 3,
                anchor=tk.CENTER,
            )

    def use_item(self, player, pressed):
        if "Down" in pressed:
            self.select_item += 1
            self.select_item = self.select_item % (player.item_num + 1)
        elif "Up" in pressed:
            self.select_item -= 1
            if self.select_item == -1:
                self.select_item = player.item_num
        elif "Return" in pressed:
            if self.select_item != player.item_num:
                if player.item[self.select_item][0] != 0:
                    player.item[self.select_item][0] -= 1
                    if player.item[self.select_item][1] == "Protein":
                        player.muscle += 100
                    elif player.item[self.select_item][1] == "Energy Drink":
                        player.stress -= 50
                        if player.stress < 0:
                            player.stress = 0
                else:
                    self.donthave_flag = 1
            else:
                self.select_item = 0
                self.useitem_flag = 0
                return 0

    def event_run(self, player):
        coodinate = self.field_array[player.x][player.y]
        if coodinate == "Work":
            self.event_work(player)
        if coodinate == "Job\nChange":
            self.event_jobchange(player)
        if coodinate == "Shop":
            self.shop_flag = 1
