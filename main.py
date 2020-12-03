from game import GAME
from player import PLAYER
import tkinter



def main():
    #ウィンドウのインスタンス生成
    root = tkinter.Tk()



    #ウィンドウの設定
    root.title("prototype")
    window_ratio = (16, 9)#(w, h)
    window_magnification = 70#120代入で1920*1080になる
    h = window_ratio[1]*window_magnification#ウィンドウの高さ
    w = window_ratio[0]*window_magnification#ウィンドウの幅

    root.minsize(w, h)

    #gameのインスタンス生成
    g = GAME(w, h, root)

    #割り込みが起きる以外はループ
    root.mainloop()


if __name__ == '__main__':
    main()
