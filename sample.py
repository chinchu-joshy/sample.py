import turtle
import time
import random

delay = 0.1
segment = []
score = 0
high_score = 0
# set up the screen
window = turtle.Screen()
window.title("snake game")
window.bgcolor("yellow")
window.setup(width=500, height=600)
window.tracer(0)  # turns off the screen updates
# setting snake head
head = turtle.Turtle()
head.color("black")
head.shape("square")
head.speed(0)
head.penup()
head.goto(100, 100)
head.direction = "stop"
# setting food for snake
food = turtle.Turtle()
food.shape("circle")
food.color("green")
food.speed(0)
food.penup()
# score board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High score : 0", align="center", font=("Courier", 20, "normal"))


def movement():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def upward():
    if head.direction != "down":
        head.direction = "up"


def downward():
    if head.direction != "up":
        head.direction = "down"


def leftward():
    if head.direction != "right":
        head.direction = "left"


def rightward():
    if head.direction != "left":
        head.direction = "right"


window.listen()
window.onkeypress(upward, "w")
window.onkeypress(downward, "z")
window.onkeypress(rightward, "d")
window.onkeypress(leftward, "a")

while True:
    window.update()
    # head collision
    if head.xcor() > 230 or head.xcor() < -230 or head.ycor() > 285 or head.ycor() < -285:

        time.sleep(1)
        head.goto(100, 100)
        head.direction = "stop"
        for x in segment:
            x.goto(1000, 1000)
        segment.clear()
        score = 0

        pen.clear()
        pen.write("Score : {} High score : {}".format(score, high_score), align="center",
                  font=("Courier", 20, "normal"))
    if head.distance(food) < 20:
        x = random.randint(-200, 200)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # setting the segment addition
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.speed(0)
        new_segment.penup()
        segment.append(new_segment)

        # score increasing
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High score : {}".format(score, high_score), align="center",
                  font=("Courier", 20, "normal"))

    for i in range(len(segment) - 1, 0, -1):
        x = segment[i - 1].xcor()
        y = segment[i - 1].ycor()
        segment[i].goto(x, y)
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)
    movement()

    # body collision
    for y in segment:
        if y.distance(head) < 20:
            time.sleep(1)
            head.goto(100, 100)
            head.direction = "stop"

            for x in segment:
                x.goto(1000, 1000)
            segment.clear()
            score = 0

            pen.clear()
            pen.write("Score : {} High score : {}".format(score, high_score), align="center",
                      font=("Courier", 20, "normal"))
    time.sleep(delay)

window.mainloop()
