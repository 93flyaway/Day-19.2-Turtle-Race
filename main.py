import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["blue", "red", "purple", "yellow", "green", "orange"]
turtle_list = []

initial_y_position = 75
for index in range(len(colors)):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-240, y=initial_y_position)
    initial_y_position -= 30
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

screen.exitonclick()
