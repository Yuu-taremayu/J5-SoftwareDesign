import random
import tkinter as tk
from field import FIELD
from player import PLAYER

class GAME():
    # Game config
    def __init__(self, w, h, mag, root):
        # Please add variables as appropriate
        # Variables of class
        self.WIDTH = w
        self.HEIGHT = h
        self.MAG = mag
        self.root = root
        self.scene_cnt = 0
        self.goal_order = []

        # Variables of function
        self.var_start_menu = (1, None)
        self.var_select_menu = (3, 2, None)
        self.var_shop_menu = (1, None)

        # Keyboard config
        self.frame = tk.Frame(self.root, width=w, height=h)
        self.frame.bind("<KeyPress>",self.key_pressed)
        self.frame.bind("<KeyRelease>",self.key_released)
        self.frame.focus_set()
        self.frame.pack()
        self.pressed = {}#pressed key

        # Create canvas
        canvas = tk.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
        canvas.place(x=0, y=0)

        # Array of field
        self.field = FIELD(w,h,mag)

        # Create instance
        self.player = [PLAYER(i) for i in range(4)]
        self.turn = 0
        self.old_turn = None

        self.start_menu()

    # Add pressed key
    def key_pressed(self, event):
        self.pressed[event.keysym] = True
        self.pos = (0,0)

        if self.scene_cnt == 0:#Call select_menu
            self.start_menu()
        elif self.scene_cnt == 1:
            self.select_menu()
        elif self.scene_cnt == 2:
            if self.field.shop_flag == 1:
                self.shop(self.player[self.turn])
            else:
                self.start()
        elif self.scene_cnt == 3:
            self.show_result()

    # Delete released key
    def key_released(self, event):
        self.pressed.pop(event.keysym, None)

    # when click button, focus self.frame
    def click_button(self, l_name):
        self.frame.focus_set()

        #write names
        for i in range(len(l_name)):
            self.player[i].name = l_name[i].get()

    # Disp start menu
    # TODO: Modify the design
    def start_menu(self):
        #define
        up = 1
        down = 2

        # Text config
        self.root.option_add("*font", ["MS Pゴシック", 15])

        # Disp process
        select, old_key = self.var_start_menu

        # Select process
        if "Up" in self.pressed and old_key != up:
            select = 1
            old_key = up
        elif "Down" in self.pressed and old_key != down:
            select = 2
            old_key = down
        elif "Return" in self.pressed:
            if select == 1:# End function
                # Execute start_menu 3ms later
                self.root.after(3, self.select_menu)
                self.scene_cnt = 1
                # Create canvas
                canvas = tk.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
                canvas.place(x=0, y=0)
                return 0
            else:# End game
                exit()
        elif self.pressed == {}:
            old_key = None

        # create label
        l_title = tk.Label(text="<---Title--->", font=("Menlo", int(self.MAG/3)))
        if select == 1:
            l_start = tk.Label(text="Game start", font=("Menlo", int(self.MAG/5)), background="yellow")
            l_exit = tk.Label(text="Exit", font=("Menlo", int(self.MAG/5)), background="blue")
        else:
            l_start = tk.Label(text="Game start", background="blue")
            l_exit = tk.Label(text="Exit", background="yellow")
        l_title.place(x=self.WIDTH/2, y=self.HEIGHT/10*2, width=self.MAG*8, height=self.MAG*3/2, anchor=tk.N)
        l_start.place(x=self.WIDTH/2, y=self.HEIGHT/10*6, width=self.MAG*2, height=self.MAG/2, anchor=tk.N)
        l_exit.place(x=self.WIDTH/2, y=self.HEIGHT/10*7, width=self.MAG*2, height=self.MAG/2, anchor=tk.N)

        self.var_start_menu = [select, old_key]

        # Update window
        self.root.update()


    # show select menu
    # TODO: fix UI
    def select_menu(self):
        # define
        up = 1
        down = 2
        left = 3
        right = 4

        # Fill black
        canvas = tk.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
        canvas.place(x=0, y=0)

        # 1:player 2:start 3:left 4:right
        select, player_num, old_key = self.var_select_menu

        # control select
        if "Up" in self.pressed and old_key != up:
            select = 1
            old_key = up
        elif "Down" in self.pressed and old_key != down:
            select = 2
            old_key = down
        elif "Left" in self.pressed and old_key != left:
            select = 3
            old_key = left
        elif "Right" in self.pressed and old_key != right:
            select = 4
            old_key = right
        elif "Return" in self.pressed:
            if select == 2:
                # Execute next function 300ms later
                self.root.after(100, self.start)
                self.pressed.clear()
                self.scene_cnt = 2
                # Fill black
                canvas = tk.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
                canvas.place(x=0, y=0)
                return 0
            elif select == 3:
                if player_num > 2:
                    player_num -= 1
                old_key = 0
            elif select == 4:
                if player_num < 4:
                    player_num += 1
                old_key = 0
        elif self.pressed == {}:
            old_key = None

        # generate label
        l_title = tk.Label(text="Select Menu", font=("Menlo", int(self.MAG/4)), background="green")
        l_player = tk.Label(text="Players", font=("Menlo", int(self.MAG/5)), background="green")
        l_num = tk.Label(text=str(player_num), font=("Menlo", int(self.MAG/4)), background="green")
        if select == 1:
            l_start = tk.Label(text="Start", font=("Menlo", int(self.MAG/5)), background="blue")
            l_left = tk.Label(text="<=", font=("Menlo", int(self.MAG/6)), background="yellow")
            l_right = tk.Label(text="=>", font=("Menlo", int(self.MAG/6)), background="blue")
        elif select == 2:
            l_start = tk.Label(text="Start", font=("Menlo", int(self.MAG/5)), background="yellow")
            l_left = tk.Label(text="<=", font=("Menlo", int(self.MAG/6)), background="blue")
            l_right = tk.Label(text="=>", font=("Menlo", int(self.MAG/6)), background="blue")
        elif select == 3:
            l_start = tk.Label(text="Start", font=("Menlo", int(self.MAG/5)), background="blue")
            l_left = tk.Label(text="<=", font=("Menlo", int(self.MAG/6)), background="yellow")
            l_right = tk.Label(text="=>", font=("Menlo", int(self.MAG/6)), background="blue")
        elif select == 4:
            l_start = tk.Label(text="Start", font=("Menlo", int(self.MAG/5)), background="blue")
            l_left = tk.Label(text="<=", font=("Menlo", int(self.MAG/6)), background="blue")
            l_right = tk.Label(text="=>", font=("Menlo", int(self.MAG/6)), background="yellow")
        l_title.place(x=self.WIDTH/10*5, y=self.HEIGHT/12*2, width=self.MAG*2, height=self.MAG, anchor=tk.CENTER)
        l_player.place(x=self.WIDTH/10*3, y=self.HEIGHT/10*3, width=self.MAG*3/2, height=self.MAG*2/3, anchor=tk.CENTER)
        l_start.place(x=self.WIDTH/10*5, y=self.HEIGHT/10*8, width=self.MAG*3/2, height=self.MAG/3,anchor=tk.CENTER)
        l_num.place(x=self.WIDTH/10*5, y=self.HEIGHT/10*3, width=self.MAG, height=self.MAG/2, anchor=tk.CENTER)
        l_left.place(x=self.WIDTH/14*6, y=self.HEIGHT/10*3, width=self.MAG/2, height=self.MAG/3, anchor=tk.CENTER)
        l_right.place(x=self.WIDTH/14*8, y=self.HEIGHT/10*3, width=self.MAG/2, height=self.MAG/3, anchor=tk.CENTER)

        # input player name
        l_name = [tk.Entry(width=10, font=("Menlo", int(self.MAG/6))) for i in range(4)]
        button = tk.Button(text="OK", font=("Menlo", int(self.MAG/6)), command=lambda: self.click_button(l_name))
        for i in range(player_num):
            lbl = tk.Label(text="Player "+str(i+1), font=("Menlo", int(self.MAG/6)))
            if self.MAG <= 60:
                l_name[i].place(x=self.WIDTH/10*5, y=self.HEIGHT/10*4+(i*30), width=100, height=25, anchor=tk.CENTER)
                button.place(x=self.WIDTH/10*7, y=self.HEIGHT/10*4+(i*30), width=40, height=30, anchor=tk.CENTER)
                lbl.place(x=self.WIDTH/10*3, y=self.HEIGHT/10*4+(i*30), width=40, height=30, anchor=tk.CENTER)
            else:
                l_name[i].place(x=self.WIDTH/10*5, y=self.HEIGHT/10*4+(i*self.MAG/2), width=self.MAG*2, height=self.MAG/3, anchor=tk.CENTER)
                button.place(x=self.WIDTH/10*7, y=self.HEIGHT/10*4+(i*self.MAG/2), width=self.MAG/2, height=self.MAG/3, anchor=tk.CENTER)
                lbl.place(x=self.WIDTH/10*3, y=self.HEIGHT/10*4+(i*self.MAG/2), width=self.MAG*3/2, height=self.MAG*2/5, anchor=tk.CENTER)
            l_name[i].insert(0, self.player[i].name)

        self.var_select_menu = [select, player_num, old_key]

        if player_num == 2:
            self.player[0].x = 0
            self.player[0].y = 0
            self.player[1].x = 4
            self.player[1].y = 3
        elif player_num == 3:
            self.player[0].x = 0
            self.player[0].y = 0
            self.player[1].x = 4
            self.player[1].y = 0
            self.player[2].x = 0
            self.player[2].y = 3
        elif player_num == 4:
            self.player[0].x = 0
            self.player[0].y = 0
            self.player[1].x = 4
            self.player[1].y = 0
            self.player[2].x = 0
            self.player[2].y = 3
            self.player[3].x = 4
            self.player[3].y = 3

        # Update window
        self.root.update()

    # start game
    def start(self):
        if self.player[self.turn].goal_flag == False:
            self.print_field()
            if self.old_turn != self.turn:
                self.player[self.turn].dice = self.roll_dice()
                self.old_turn = self.turn

            if self.player[self.turn].dice != None:
                self.move_player()
            self.check_win_condition()
            self.check_exit_condition()
        else:
            self.turn = (self.turn + 1) % 4
            
    def print_field(self):
        # Fill black
        canvas = tk.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
        canvas.place(x=0, y=0)
        l_field = [[None for j in range(self.field.y)] for i in range(self.field.x)]
        for i in range(self.field.x):
            for j in range(self.field.y):
                l_field[i][j] = tk.Label(text=self.field.field_array[i][j], font=("Menlo", int(self.MAG/6)), background="red", relief="groove", borderwidth=self.MAG/10)
                l_field[i][j].place(x=self.WIDTH/2+(i-2)*self.MAG*5/2, y=self.HEIGHT/self.field.y*j+self.MAG*15/16, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tk.CENTER)
        l_stat = [None for i in range(self.var_select_menu[1])]
        for i in range(self.var_select_menu[1]):
            NAM = str(self.player[i].name) + "\n"
            JOB = "job:" + str(self.player[i].job) + "\n"
            MON = "money:" + str(self.player[i].money) + "\n"
            MUS = "muscle:" + str(self.player[i].muscle) + "\n"
            STR = "stress:" + str(self.player[i].stress) + "\n"
            DEX = "dexterity:" + str(self.player[i].dexterity)
            l_stat[i] = tk.Label(text=NAM+JOB+MON+MUS+STR+DEX, font=("Menlo", int(self.MAG/6)),  background="white", relief="ridge", borderwidth=self.MAG/20)
        if self.var_select_menu[1] == 2:
            l_stat[0].place(x=0, y=0, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tk.NW)
            l_stat[1].place(x=self.WIDTH, y=self.HEIGHT, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tk.SE)
        elif self.var_select_menu[1] == 3:
            l_stat[0].place(x=0, y=0, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tk.NW)
            l_stat[1].place(x=self.WIDTH, y=0, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tk.NE)
            l_stat[2].place(x=0, y=self.HEIGHT, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tk.SW)
        elif self.var_select_menu[1] == 4:
            l_stat[0].place(x=0, y=0, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tk.NW)
            l_stat[1].place(x=self.WIDTH, y=0, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tk.NE)
            l_stat[2].place(x=0, y=self.HEIGHT, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tk.SW)
            l_stat[3].place(x=self.WIDTH, y=self.HEIGHT, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tk.SE)

    # roll dice randomly
    def roll_dice(self):
        r = random.randint(1, 6)
        return r

    # check each player's winning condition
    def check_win_condition(self):
        if self.player[self.turn].goal_flag == True:
            print(self.player[self.turn].name, "は既に勝利条件を満たしています")
            return None

        # temporary lines
        self.player[self.turn].condition = 1
        #self.player[self.turn].money += 100

        if self.player[self.turn].condition == 1:# condition 1 : get 1,000 golds
            if self.player[self.turn].money >= 1000:
                print(self.player[self.turn].name, "が勝利条件を満たしました")
                self.player[self.turn].goal_flag = True
                self.goal_order.append(self.player[self.turn].name)
                self.turn = (self.turn + 1) % 4

        elif self.player[self.turn].condition == 2:# condition 1 : get 1,000 muscle
            if self.player[self.turn].muscle >= 1000:
                print(self.player[self.turn].name, "が勝利条件を満たしました")
                self.player[self.turn].goal_flag = True
                self.goal_order.append(self.player[self.turn].name)
                self.turn = (self.turn + 1) % 4



    # check game's exit condition
    def check_exit_condition(self):
        flag = True
        for i in range(4):
            if self.player[i].goal_flag == False:
                flag = False

        if flag == True:
            print("ゲーム終了条件が整いました")
            self.scene_cnt += 1
            self.root.after(200, self.show_result)
            self.pressed.clear()


    # move player by dice number
    def move_player(self):
        # define
        up = 1
        down = 2
        left = 3
        right = 4

        old_key = None
        l_player = [None for i in range(4)]
        if self.player[self.turn].dice > 0:
            if "Up" in self.pressed and old_key != up:
                if self.player[self.turn].y > 0:
                    self.player[self.turn].y -= 1
                    self.player[self.turn].dice -= 1
                old_key = up
            elif "Down" in self.pressed and old_key != down:
                if self.player[self.turn].y < 3:
                    self.player[self.turn].y += 1
                    self.player[self.turn].dice -= 1
                old_key = down
            elif "Left" in self.pressed and old_key != left:
                if self.player[self.turn].x > 0:
                    self.player[self.turn].x -= 1
                    self.player[self.turn].dice -= 1
                old_key = left
            elif "Right" in self.pressed and old_key != right:
                if self.player[self.turn].x < 4:
                    self.player[self.turn].x += 1
                    self.player[self.turn].dice -= 1
                old_key = right
            elif "Return" in self.pressed:
                self.field.event_run(self.player[self.turn])
                if self.field.shop_flag == 0:
                    self.turn = (self.turn+1) % 4
            elif self.pressed == {}:
                old_key = None
        else:
            self.field.event_run(self.player[self.turn])
            if self.field.shop_flag == 0:
                self.turn = (self.turn+1) % 4
        l_remain = tk.Label(text="Dice\n"+str(self.player[self.turn].dice), font=("Menlo", int(self.MAG/3)), background="blue")
        l_remain.place(x=self.WIDTH*9/10, y=self.HEIGHT/3, width=100, height=90)
        if self.var_select_menu[1] == 2:
            l_player[0] = tk.Label(text="1", font=("Menlo", int(self.MAG/6)), background="yellow", relief="ridge", borderwidth=self.MAG/60)
            l_player[0].place(x=self.player[0].x*self.MAG*5/2+self.MAG*76/32, y=self.player[0].y*self.MAG*9/4+self.MAG/3, width=self.MAG/3, height=self.MAG/3)
            l_player[1] = tk.Label(text="2", font=("Menlo", int(self.MAG/6)), background="yellow", relief="ridge", borderwidth=self.MAG/60)
            l_player[1].place(x=self.player[1].x*self.MAG*5/2+self.MAG*105/32, y=self.player[1].y*self.MAG*9/4+self.MAG*5/4, width=self.MAG/3, height=self.MAG/3)
        elif self.var_select_menu[1] == 3:
            l_player[0] = tk.Label(text="1", font=("Menlo", int(self.MAG/6)), background="yellow", relief="ridge", borderwidth=self.MAG/60)
            l_player[0].place(x=self.player[0].x*self.MAG*5/2+self.MAG*76/32, y=self.player[0].y*self.MAG*9/4+self.MAG/3, width=self.MAG/3, height=self.MAG/3)
            l_player[1] = tk.Label(text="2", font=("Menlo", int(self.MAG/6)), background="yellow", relief="ridge", borderwidth=self.MAG/60)
            l_player[1].place(x=self.player[1].x*self.MAG*5/2+self.MAG*105/32, y=self.player[1].y*self.MAG*9/4+self.MAG/3, width=self.MAG/3, height=self.MAG/3)
            l_player[2] = tk.Label(text="3", font=("Menlo", int(self.MAG/6)), background="yellow", relief="ridge", borderwidth=self.MAG/60)
            l_player[2].place(x=self.player[2].x*self.MAG*5/2+self.MAG*76/32, y=self.player[2].y*self.MAG*9/4+self.MAG*5/4, width=self.MAG/3, height=self.MAG/3)
        elif self.var_select_menu[1] == 4:
            l_player[0] = tk.Label(text="1", font=("Menlo", int(self.MAG/6)), background="yellow", relief="ridge", borderwidth=self.MAG/60)
            l_player[0].place(x=self.player[0].x*self.MAG*5/2+self.MAG*76/32, y=self.player[0].y*self.MAG*9/4+self.MAG/3, width=self.MAG/3, height=self.MAG/3)
            l_player[1] = tk.Label(text="2", font=("Menlo", int(self.MAG/6)), background="yellow", relief="ridge", borderwidth=self.MAG/60)
            l_player[1].place(x=self.player[1].x*self.MAG*5/2+self.MAG*105/32, y=self.player[1].y*self.MAG*9/4+self.MAG/3, width=self.MAG/3, height=self.MAG/3)
            l_player[2] = tk.Label(text="3", font=("Menlo", int(self.MAG/6)), background="yellow", relief="ridge", borderwidth=self.MAG/60)
            l_player[2].place(x=self.player[2].x*self.MAG*5/2+self.MAG*76/32, y=self.player[2].y*self.MAG*9/4+self.MAG*5/4, width=self.MAG/3, height=self.MAG/3)
            l_player[3] = tk.Label(text="4", font=("Menlo", int(self.MAG/6)), background="yellow", relief="ridge", borderwidth=self.MAG/60)
            l_player[3].place(x=self.player[3].x*self.MAG*5/2+self.MAG*105/32, y=self.player[3].y*self.MAG*9/4+self.MAG*5/4, width=self.MAG/3, height=self.MAG/3)

    # show result
    def show_result(self):
        # Fill black
        canvas = tk.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
        canvas.place(x=0, y=0)
        print(self.goal_order)

        player_num = 4
        title = tk.Label(text="結果発表", font=("Menlo", int(self.MAG/6)))
        for i in range(player_num):
            name = tk.Label(text=self.goal_order[i], font=("Menlo", int(self.MAG/6)))
            order = tk.Label(text=str(i+1)+"位", font=("Menlo", int(self.MAG/6)))
            if self.MAG <= 60:
                name.place(x=self.WIDTH/10*5, y=self.HEIGHT/10*4+(i*30), width=100, height=25, anchor=tk.CENTER)
                order.place(x=self.WIDTH/10*3, y=self.HEIGHT/10*4+(i*30), width=40, height=30, anchor=tk.CENTER)
                title.place(x=self.WIDTH/10*5, y=self.HEIGHT/10*2, width=100, height=25, anchor=tk.CENTER)
            else:
                name.place(x=self.WIDTH/10*5, y=self.HEIGHT/10*4+(i*self.MAG/2), width=self.MAG*2, height=self.MAG/3, anchor=tk.CENTER)
                order.place(x=self.WIDTH/10*3, y=self.HEIGHT/10*4+(i*self.MAG/2), width=self.MAG*3/2, height=self.MAG*2/5, anchor=tk.CENTER)
                title.place(x=self.WIDTH/10*5, y=self.HEIGHT/10*2, width=self.MAG*2, height=self.MAG/3, anchor=tk.CENTER)
    
    def shop(self,player):
        self.field.print_shop(player,self.pressed)
        if self.field.shop_flag == 0:
            self.turn = (self.turn + 1) % 4
