import random
import tkinter
from field import FIELD

class GAME():
    # Game config
    def __init__(self, w, h, root):
        # Please add variables as appropriate
        # Variables of class
        self.WIDTH = w
        self.HEIGHT = h
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
        self.field = FIELD()

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
    def click_button(self):
        self.frame.focus_set()

    # Disp start menu
    # TODO: Modify the design
    def start_menu(self):
        #define
        up = 1
        down = 2

        # Text config
        self.root.option_add("*font", ["MS Pゴシック", 22])

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
        l_title.place(x=self.WIDTH/2, y=100, anchor=tkinter.N)
        l_start.place(x=self.WIDTH/2, y=self.HEIGHT/2+50, anchor=tkinter.N)
        l_exit.place(x=self.WIDTH/2, y=self.HEIGHT/2+100, anchor=tkinter.N)

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
        l_title.place(x=self.WIDTH/2, y=50, anchor=tkinter.N)
        l_player.place(x=self.WIDTH/2-150, y=self.HEIGHT/2-100, anchor=tkinter.N)
        l_start.place(x=self.WIDTH/2, y=self.HEIGHT/2+150, anchor=tkinter.N)
        l_num.place(x=self.WIDTH/2, y=self.HEIGHT/2-100, anchor=tkinter.N)
        l_left.place(x=self.WIDTH/2-40, y=self.HEIGHT/2-100, anchor=tkinter.N)
        l_right.place(x=self.WIDTH/2+40, y=self.HEIGHT/2-100, anchor=tkinter.N)

        # input player name
        l_name = [tkinter.Entry(width=10), tkinter.Entry(width=10), tkinter.Entry(width=10), tkinter.Entry(width=10)]
        button = tkinter.Button(text="OK", command=lambda: self.click_button())
        for i in range(player_num):
            lbl = tkinter.Label(text="Player "+str(i+1))
            lbl.place(x=self.WIDTH/2-150, y=self.HEIGHT/2-45+i*50, anchor=tkinter.N)
            l_name[i].place(x=self.WIDTH/2, y=self.HEIGHT/2-45+i*50, anchor=tkinter.N)
            button.place(x=self.WIDTH/2+150, y=self.HEIGHT/2+30, anchor=tkinter.N)

        self.var_select_menu = [select, player_num, old_key]

        # Update window
        self.root.update()

    # start game
    def start(self):
        self.print_field(self.field)

    def print_field(self, field):
        l_field = [[None for j in range(field.y)] for i in range(field.x)]
        for i in range(field.x):
            for j in range(field.y):
                l_field[i][j] = tkinter.Label(text=field.field_array[i][j], background="red")
                l_field[i][j].place(x=self.WIDTH/2+(i-2)*250, y=self.HEIGHT/field.y*j+70, anchor=tkinter.N)

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
    def move_player():
        pass

    # show result
    def show_result():
        pass
