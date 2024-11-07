import turtle
import random

screen = turtle.Screen()
screen.bgcolor("grey")
screen.title("Catch The Turtle")
FONT = ('Arial',30,'normal')
score = 0
game_over = False
#turtle list
turtle_list = []

#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdown_turtle = turtle.Turtle()

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]
grid_size = 10

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85
    score_turtle.setposition(0,y)
    score_turtle.write(arg="Score: 0",move=False,align="center",font=FONT)

def make_turtle(x,y):
    t = turtle.Turtle()
    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}",move=False,align="center",font=FONT)
        #print(x,y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtles_ramdomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_ramdomly, 500)


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("red")
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85
    countdown_turtle.setposition(0, y-30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)


def start_game():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_ramdomly()
    countdown(20)
    turtle.tracer(1)

start_game()
turtle.mainloop()
