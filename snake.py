from tkinter import *
from constants import *

import random

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coords = []
        self.squares = []

        for i in range (0,BODY_PARTS):
            self.coords.append([0,0])

        for x,y in self.coords:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE, fill=SNAKE_COLOUR,tag="snake")
            self.squares.append(square)








class Food:
    #Game board is visualised similar to chess board, every square is 50 
    def __init__(self):
        x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        x = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coords = [x,y]
        canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOUR,tag="food")


def next_turn(snake, food):
    
    x,y = snake.coords[0]
    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    

    snake.coords.insert(0, (x,y))
    square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOUR)
    
    snake.squares.insert(0,square)
    del snake.coords[-1]
    canvas.delete(snake.squares[-1])

    del snake.squares[-1]

    window.after(SPEED,next_turn,snake,food)


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

next_turn(snake,food)



window.mainloop()