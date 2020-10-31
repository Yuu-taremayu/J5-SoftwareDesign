from game import GAME
from player import PLAYER
import tkinter



def main():
    #ウィンドウのインスタンス生成
    root = tkinter.Tk()

    #ウィンドウの設定
    root.title("prototype")
    h = 400#ウィンドウの高さ
    w = 600#ウィンドウの幅
    root.minsize(w, h)

    #gameのインスタンス生成
    g = GAME(w, h, root)

    #割り込みが起きる以外はループ
    root.mainloop()


if __name__ == '__main__':
    main()
