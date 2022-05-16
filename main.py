from tkinter import *
from tkinter import ttk, font

import brickblock


def start_gui():
    app = Application()


class Application():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('100x250')
        self.root.config(bg='aquamarine2')
        self.root.title('Play Brick Block Break Game')
        fuente = font.Font(weight='bold')

        self.game_label = ttk.Label(self.root, text="Games", font=fuente, background="aquamarine2")
        self.game_label.config(font=("Verdana", 24))

        self.level1 = ttk.Button(self.root, text='Level 1',
                                 command=lambda: self.start_level1())
        self.level2 = ttk.Button(self.root, text='Level 2',
                                 command=lambda: self.start_level2())
        self.level3 = ttk.Button(self.root, text='Level 3',
                                 command=lambda: self.start_level3())
        self.exit_button = ttk.Button(self.root, text='Exit', command=lambda: self.exit())

        self.game_label.grid(row=0, column=1000, sticky='n', padx=5, pady=5)
        self.level1.grid(row=3, column=1000, sticky='n', padx=5, pady=5)
        self.level2.grid(row=5, column=1000, sticky='n', padx=5, pady=5)
        self.level3.grid(row=7, column=1000, sticky='n', padx=5, pady=5)
        self.exit_button.grid(row=15, column=1000, sticky='n', padx=5, pady=5)

        self.root.mainloop()

    def start_level1(self):
        brickblock.start_game('1')

    def start_level2(self):
        self.game_label.quit()
        brickblock.start_game('2')

    def start_level3(self):
        self.game_label.quit()
        brickblock.start_game('3')

    def exit(self):
        self.game_label.quit()
        print("Has acabado de jugar")


if __name__ == '__main__':
    start_gui()
