# 05.07.2023

#############################################################
# ALL THIS WITH THE HELP OF THE MIGHTY BRO CODE TUTORIAL <3 #
#############################################################

from tkinter import *
import random
import subprocess

# settings
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 1000
SPACE_SIZE = 50
BODY_PARTS = 3  # initial snake size
SNAKE_COLOR = "#00ff00"
FOOD_COLOR = "#ff0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food"
        )


def check_collision(snake):
    x, y = snake.coordinates[0]

    # wall collisions
    if x >= GAME_WIDTH or x < 0:
        return True

    elif y >= GAME_HEIGHT or y < 0:
        return True

    # self collision
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "down":
        y += SPACE_SIZE
    elif direction == "up":
        y -= SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
    )

    snake.squares.insert(0, square)

    # handling food eating
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        score += 1

        label.config(text="score: {}".format(score))

        canvas.delete("food")

        food = Food()

    # if no food is eaten size is unchanged
    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


# game over sign
# new game button


def game_over():
    canvas.delete(ALL)  # clear the screen

    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        text="game over!",
        font=("consolas", 70),
        fill="brown",
        tag="game_over",
    )
    canvas.configure(bg="#123456")


def change_direction(new_direction):
    global direction

    if new_direction == "down" and not direction == "up":
        direction = "down"
    elif new_direction == "up" and not direction == "down":
        direction = "up"
    elif new_direction == "left" and not direction == "right":
        direction = "left"
    elif new_direction == "right" and not direction == "left":
        direction = "right"


# code formatting each time the program is run
command = "black ."

process = subprocess.Popen(
    command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)


window = Tk()  # create window


window.title("Snake game")  # name it
window.resizable(False, False)  # lock width and height

score = 0
direction = "right"

label = Label(window, text="score: {}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()  # render window

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)


window.mainloop()

# window.destroy()
