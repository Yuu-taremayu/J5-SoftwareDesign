import random
import tkinter
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

        # Variables of function
        self.var_start_menu = (1, None)
        self.var_select_menu = (3, 2, None)

        # Keyboard config
        self.frame = tkinter.Frame(self.root, width=w, height=h)
        self.frame.bind("<KeyPress>",self.key_pressed)
        self.frame.bind("<KeyRelease>",self.key_released)
        self.frame.focus_set()
        self.frame.pack()
        self.pressed = {}#pressed key

        # Create canvas
        canvas = tkinter.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
        canvas.place(x=0, y=0)

        # Array of field
        self.field = FIELD(w,h)

        # Create instance
        self.player = [PLAYER(i) for i in range(4)]
        self.turn = 0

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
            self.start()

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
        if self.MAG <= 60:
            self.root.option_add("*font", ["MS Pゴシック", 15])
        else:
            self.root.option_add("*font", ["MS Pゴシック", int(self.MAG/5)])

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
                canvas = tkinter.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
                canvas.place(x=0, y=0)
                return 0
            else:# End game
                exit()
        elif self.pressed == {}:
            old_key = None

        # create label
        l_title = tkinter.Label(text="<---Title--->")
        if select == 1:
            l_start = tkinter.Label(text="Game start", background="yellow")
            l_exit = tkinter.Label(text="Exit", background="blue")
        else:
            l_start = tkinter.Label(text="Game start", background="blue")
            l_exit = tkinter.Label(text="Exit", background="yellow")
        l_title.place(x=self.WIDTH/2, y=self.HEIGHT/10*2, width=self.MAG*8, height=self.MAG*3/2, anchor=tkinter.N)
        l_start.place(x=self.WIDTH/2, y=self.HEIGHT/10*6, width=self.MAG*2, height=self.MAG/2, anchor=tkinter.N)
        l_exit.place(x=self.WIDTH/2, y=self.HEIGHT/10*7, width=self.MAG*2, height=self.MAG/2, anchor=tkinter.N)

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
        canvas = tkinter.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
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
                # Execute next function 3ms later
                self.root.after(3, self.start)
                self.scene_cnt = 2
                # Fill black
                canvas = tkinter.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
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
        l_title = tkinter.Label(text="Select Menu", background="green")
        l_player = tkinter.Label(text="Players", background="green")
        l_num = tkinter.Label(text=str(player_num), background="green")
        if select == 1:
            l_start = tkinter.Label(text="Start", background="blue")
            l_left = tkinter.Label(text="<=", background="yellow")
            l_right = tkinter.Label(text="=>", background="blue")
        elif select == 2:
            l_start = tkinter.Label(text="Start", background="yellow")
            l_left = tkinter.Label(text="<=", background="blue")
            l_right = tkinter.Label(text="=>", background="blue")
        elif select == 3:
            l_start = tkinter.Label(text="Start", background="blue")
            l_left = tkinter.Label(text="<=", background="yellow")
            l_right = tkinter.Label(text="=>", background="blue")
        elif select == 4:
            l_start = tkinter.Label(text="Start", background="blue")
            l_left = tkinter.Label(text="<=", background="blue")
            l_right = tkinter.Label(text="=>", background="yellow")
        l_title.place(x=self.WIDTH/10*5, y=self.HEIGHT/12*2, width=self.MAG*2, height=self.MAG, anchor=tkinter.CENTER)
        l_player.place(x=self.WIDTH/10*3, y=self.HEIGHT/10*3, width=self.MAG*3/2, height=self.MAG*2/3, anchor=tkinter.CENTER)
        l_start.place(x=self.WIDTH/10*5, y=self.HEIGHT/10*8, width=self.MAG*3/2, height=self.MAG/3,anchor=tkinter.CENTER)
        l_num.place(x=self.WIDTH/10*5, y=self.HEIGHT/10*3, width=self.MAG, height=self.MAG/2, anchor=tkinter.CENTER)
        l_left.place(x=self.WIDTH/14*6, y=self.HEIGHT/10*3, width=self.MAG/2, height=self.MAG/3, anchor=tkinter.CENTER)
        l_right.place(x=self.WIDTH/14*8, y=self.HEIGHT/10*3, width=self.MAG/2, height=self.MAG/3, anchor=tkinter.CENTER)

        # input player name
        l_name = [tkinter.Entry(width=10), tkinter.Entry(width=10), tkinter.Entry(width=10), tkinter.Entry(width=10)]
        button = tkinter.Button(text="OK", command=lambda: self.click_button(l_name))
        for i in range(player_num):
            lbl = tkinter.Label(text="Player "+str(i+1))
            lbl.place(x=self.WIDTH/10*3, y=self.HEIGHT/10*4+(i*self.MAG/2), width=self.MAG*3/2, height=self.MAG*2/5, anchor=tkinter.CENTER)
            if self.MAG <= 60:
                l_name[i].place(x=self.WIDTH/10*5, y=self.HEIGHT/10*4+(i*30), width=100, height=25, anchor=tkinter.CENTER)
                button.place(x=self.WIDTH/10*7, y=self.HEIGHT/10*4+(i*30), width=40, height=30, anchor=tkinter.CENTER)
            else:
                l_name[i].place(x=self.WIDTH/10*5, y=self.HEIGHT/10*4+(i*self.MAG/2), width=self.MAG*2, height=self.MAG/3, anchor=tkinter.CENTER)
                button.place(x=self.WIDTH/10*7, y=self.HEIGHT/10*4+(i*self.MAG/2), width=self.MAG/2, height=self.MAG/3, anchor=tkinter.CENTER)
            l_name[i].insert(0, self.player[i].name)

        self.var_select_menu = [select, player_num, old_key]

        # Update window
        self.root.update()

    # start game
    def start(self):
        self.print_field()
        self.move_player()

    def print_field(self):
        # Fill black
        canvas = tkinter.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
        canvas.place(x=0, y=0)
        l_field = [[None for j in range(self.field.y)] for i in range(self.field.x)]
        for i in range(self.field.x):
            for j in range(self.field.y):
                l_field[i][j] = tkinter.Label(text=self.field.field_array[i][j], background="red", relief="groove", borderwidth=self.MAG/10)
                l_field[i][j].place(x=self.WIDTH/2+(i-2)*self.MAG*5/2, y=self.HEIGHT/self.field.y*j+self.MAG*15/16, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tkinter.CENTER)
        l_stat = [None for i in range(4)]
        for i in range(4):
            JOB = "job:" + str(self.player[i].job) + "\n"
            MON = "money:" + str(self.player[i].money) + "\n"
            MUS = "muscle:" + str(self.player[i].muscle) + "\n"
            STR = "stress:" + str(self.player[i].stress) + "\n"
            DEX = "dexterity:" + str(self.player[i].dexterity)
            l_stat[i] = tkinter.Label(text=JOB+MON+MUS+STR+DEX, background="white", relief="ridge", borderwidth=self.MAG/20)
        l_stat[0].place(x=0, y=0, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tkinter.NW)
        l_stat[1].place(x=self.WIDTH, y=0, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tkinter.NE)
        l_stat[2].place(x=0, y=self.HEIGHT, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tkinter.SW)
        l_stat[3].place(x=self.WIDTH, y=self.HEIGHT, width=self.MAG*3/2, height=self.MAG*3/2, anchor=tkinter.SE)

    # roll dice randomly
    def roll_dice():
        r = random.randint(1, 6)
        return r

    # check each player's winning condition
    def check_win_condition():
        pass

    # check game's exit condition
    def check_exit_condition():
        pass

    # move player by dice number
    def move_player(self):
        # define
        up = 1
        down = 2
        left = 3
        right = 4

        old_key = None
        l_player = [None for i in range(4)]
        if "Up" in self.pressed and old_key != up:
            if self.player[self.turn].y > 0:
                self.player[self.turn].y -= 1
            old_key = up
        elif "Down" in self.pressed and old_key != down:
            if self.player[self.turn].y < 3:
                self.player[self.turn].y += 1
            old_key = down
        elif "Left" in self.pressed and old_key != left:
            if self.player[self.turn].x > 0:
                self.player[self.turn].x -= 1
            old_key = left
        elif "Right" in self.pressed and old_key != right:
            if self.player[self.turn].x < 4:
                self.player[self.turn].x += 1
            old_key = right
        elif "Return" in self.pressed:
            self.turn = (self.turn + 1) % 4
        elif self.pressed == {}:
            old_key = None

        l_player[0] = tkinter.Label(text="1", background="yellow", relief="ridge", borderwidth=self.MAG/60)
        l_player[0].place(x=self.player[0].x*self.MAG*5/2+self.MAG*76/32, y=self.player[0].y*self.MAG*9/4+self.MAG/3, width=self.MAG/3, height=self.MAG/3)
        l_player[1] = tkinter.Label(text="2", background="yellow", relief="ridge", borderwidth=self.MAG/60)
        l_player[1].place(x=self.player[1].x*self.MAG*5/2+self.MAG*105/32, y=self.player[1].y*self.MAG*9/4+self.MAG/3, width=self.MAG/3, height=self.MAG/3)
        l_player[2] = tkinter.Label(text="3", background="yellow", relief="ridge", borderwidth=self.MAG/60)
        l_player[2].place(x=self.player[2].x*self.MAG*5/2+self.MAG*76/32, y=self.player[2].y*self.MAG*9/4+self.MAG*5/4, width=self.MAG/3, height=self.MAG/3)
        l_player[3] = tkinter.Label(text="4", background="yellow", relief="ridge", borderwidth=self.MAG/60)
        l_player[3].place(x=self.player[3].x*self.MAG*5/2+self.MAG*105/32, y=self.player[3].y*self.MAG*9/4+self.MAG*5/4, width=self.MAG/3, height=self.MAG/3)

    # show result
    def show_result():
        pass
