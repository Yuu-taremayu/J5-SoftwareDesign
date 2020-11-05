import random
import tkinter

class GAME():
    # ゲーム設定の初期化
    def __init__(self, w, h, root):
        #必要であれば適宜追加（修正）していって下さい
        self.WIDTH = w
        self.HEIGHT = h
        self.root = root

        #キーボード操作の設定
        frame = tkinter.Frame(self.root, width=w, height=h)
        frame.bind("<KeyPress>",self.key_pressed)
        frame.bind("<KeyRelease>",self.key_released)
        frame.focus_set()
        frame.pack()
        self.pressed = {}#押されているキーが格納される

        self.start_menu()
        self.select_menu()

    #押されたキーをpressedに追加
    def key_pressed(self, event):
        self.pressed[event.keysym] = True
        self.pos = (0,0)

    #離されたキーをpressedから削除
    def key_released(self, event):
        self.pressed.pop(event.keysym, None)


    #スタートメニューを表示
    #TODO: 背景などの画像を適用する。アイテム配置の修正
    def start_menu(self):
        #define
        up = 1
        down = 2

        #テキスト設定
        self.root.option_add("*font", ["MS Pゴシック", 22])

        #スタートメニューの描画と操作の処理
        select = 1#1:start, 2:exit
        old_key = None
        while True:#セレクト決定までループ
            #キャンバス生成
            canvas = tkinter.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
            canvas.place(x=0, y=0)

            #押されたキーによってセレクトを操作
            if "Up" in self.pressed and old_key != up:
                select = 1
                old_key = up
            elif "Down" in self.pressed and old_key != down:
                select = 2
                old_key = down
            elif "Return" in self.pressed:
                if select == 1:#関数終了
                    return 0
                else:#ゲーム終了
                    exit()
            elif self.pressed == {}:
                old_key = None

            #ラベル生成
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

            #ウィンドウの更新
            self.root.update()

    # show select menu
    # TODO: fix UI
    def select_menu(self):
        # define
        up = 1
        down = 2
        left = 3
        right = 4

        # 1:player 2:start 3:left 4:right
        select = 3
        player_num = 2
        old_key = None

        while True:
            #キャンバス生成
            canvas = tkinter.Canvas(bg="black", width=self.WIDTH, height=self.HEIGHT)
            canvas.place(x=0, y=0)

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
                    return 0
                elif select == 3 and old_key is None:
                    player_num -= 1
                    old_key = 0
                elif select == 4 and old_key is None:
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
            l_title.place(x=self.WIDTH/2, y=100, anchor=tkinter.N)
            l_player.place(x=self.WIDTH/2-150, y=self.HEIGHT/2-50, anchor=tkinter.N)
            l_start.place(x=self.WIDTH/2, y=self.HEIGHT/2+100, anchor=tkinter.N)
            l_num.place(x=self.WIDTH/2, y=self.HEIGHT/2-50, anchor=tkinter.N)
            l_left.place(x=self.WIDTH/2-40, y=self.HEIGHT/2-50, anchor=tkinter.N)
            l_right.place(x=self.WIDTH/2+40, y=self.HEIGHT/2-50, anchor=tkinter.N)

            #ウィンドウの更新
            self.root.update()

    # start game
    def start():
        pass

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
