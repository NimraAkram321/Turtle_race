from turtle import Turtle, Screen
import  random


screen = Screen()
colors= ["red","orange","green","blue","purple","yellow"]
is_game_on=False
screen.setup(width=500, height=400)
user_input= screen.textinput(title="Make your bet", prompt="which tutle will win the race? Enter a color: ")
turles=[]
y_position = [-100,-60,-20,20,60,100]
for tutle_index in range(0, 6):

    tim = Turtle(shape='turtle')
    tim.color(colors[tutle_index])
    tim.penup()
    tim.goto(x=-230,y=y_position[tutle_index])
    turles.append(tim)
if user_input:
    is_game_on=True

while is_game_on:

    for turtle in turles:
        randomSteps = random.randint(0, 11)
        turtle.forward(randomSteps)
        if turtle.xcor() >=228:
            turtleColor = turtle.pencolor()
            if turtleColor == user_input:
                print(f"You've win, the {turtleColor} turtle is the winner")
            else:
                print(f"You've lose, the {turtleColor} turtle is the winner")
            is_game_on = False

screen.exitonclick()