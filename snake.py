from tkinter import *
from constants import *

import random

class Snake:
    pass







class Food:
    #Game board is visualised similar to chess board, every square is 50 
    def __init__(self):
        x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        x = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coords = [x,y]
        canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOUR,tag="food")


def next_turn():
    pass

def change_direction():
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text = "Score:{}".format(score), font=('console',40))
label.pack()
canvas = Canvas(window, bg=BG_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
#makes python window start at the centre instead of bottom left corner
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


snake = Snake()
food = Food()



window.mainloop()