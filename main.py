import turtle
import random
import time
import winsound
from food import Food
from head import Head
from tissue import Tissue
from scoreboard import Scors, Gameover

winsound.PlaySound('sound.wav', winsound.SND_LOOP + winsound.SND_ASYNC)

turtle.register_shape('bg.gif')

screen = turtle.Screen()
screen.setup(width=1400, height=900)
screen.tracer(0)
screen.bgpic('bg.gif')

score = 0
now = 0

head = Head()
food = Food()
tissue = Tissue()
scores = Scors()
gameover = Gameover()

tissue_time = [3]

# Creating Tissue Time

for i in range(3):
    now1 = random.randint(25, 40)
    now2 = random.randint(45, 55)
    now3 = random.randint(65, 80)
    now4 = random.randint(85, 100)
    tissue_time.append(now1)
    tissue_time.append(now2)
    tissue_time.append(now3)
    tissue_time.append(now4)

screen.listen()
screen.onkey(head.goup, "Up")
screen.onkey(head.godown, "Down")
screen.onkey(head.goleft, "Left")
screen.onkey(head.goright, "Right")

with_tissue = False

game_on = True
while game_on:
    screen.update()
    time.sleep(0.0005)
    head.move()
    scores.clear()
    scores.write(f'Your Score is : {score}')
    if now in tissue_time:
        tissue.showturtle()
        for i in head.poops:
            if tissue.distance(i) < 15:
                tissue.refresh()
        if head.distance(tissue) < 15:
            with_tissue = True
            tissue.hideturtle()
            now += 1
    else:
        tissue.hideturtle()

    if head.distance(food) < 15:
        with_tissue = False
        score += 1
        now += 1
        food.refresh()
        for i in head.poops:
            if food.distance(i) < 15:
                food.refresh()
        head.pooping()

    elif head.xcor() > 675 or head.ycor() > 430 or head.xcor() < -675 or head.ycor() < -430:
        winsound.PlaySound('poop-sound.wav', winsound.SND_ASYNC)
        screen.tracer(1)
        head.poopfall()
        gameover.write('GAME OVER', align='center', font=("Verdana", 30, "normal"))
        game_on = False

    else:

        for i in head.poops[0:-1]:
            if with_tissue == True:
                if head.distance(i) < 15:
                    head.poops.remove(i)
                    i.hideturtle()
                    with_tissue = False
            elif head.distance(i) < 15:
                screen.tracer(1)
                winsound.PlaySound('poop-sound.wav', winsound.SND_ASYNC)
                head.poopfall()
                gameover.write('GAME OVER', align='center', font=("Verdana", 30, "normal"))
                game_on = False

screen.exitonclick()
