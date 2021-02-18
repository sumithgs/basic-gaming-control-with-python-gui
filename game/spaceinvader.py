import turtle
import math
import random
import winsound
import datetime

day = int(datetime.datetime.now().day)
month = int(datetime.datetime.now().month)
srt = datetime.datetime.now().strftime('%H:%M:%S')

global bustate
def pp():
    f = open('file.txt', 'a')
    f.write(f'Game:Space invaders,Date:{day},Month:{month},Start time:{srt}\n')
    f.close()

    global bustate
    # set up screen
    wn = turtle.Screen()
    wn.bgcolor('black')
    wn.title('Space Invader')
    #wn.bgpic('space1.png')
    # Draw border
    b_pen = turtle.Turtle()
    b_pen.speed(0)
    b_pen.color('white')
    b_pen.penup()
    b_pen.setposition(-300, -300)
    b_pen.pendown()
    b_pen.pensize(3)
    for side in range(4):
        b_pen.fd(600)
        b_pen.lt(90)
    b_pen.hideturtle()
    # set scoring process
    score = 0
    # draw score
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.setposition(-290, 275)
    scorestring = 'score: %s' % score
    pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
    pen.hideturtle()
    # player turtle
    player = turtle.Turtle()
    player.color('blue')
    player.shape('triangle')
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    # enemy = turtle.Turtle()
    ps = 15
    # incresing no of enemies
    noe = 5
    # creating an empty list
    enemies = []

    # add enemies to list
    for i in range(noe):
        # create enemy
        enemies.append(turtle.Turtle())
    for enemy in enemies:
        enemy.color('red')
        enemy.shape('circle')
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)

    es = 4

    # weapon
    bu = turtle.Turtle()
    bu.color('yellow')
    bu.shape('triangle')
    bu.penup()
    bu.speed(0)
    bu.setheading(90)
    bu.shapesize(0.5, 0.5)
    bu.hideturtle()

    bs = 20

    # define bullet
    bustate = 'ready'

    # movw the player left and right
    def left():
        x = player.xcor()
        x -= ps
        if x < -280:
            x = -280
        player.setx(x)

    def right():
        x = player.xcor()
        x += ps
        if x > 280:
            x = 280
        player.setx(x)

    def fb():
        # declare bullet state as a global when it changes
        global bustate
        if bustate == 'ready':
            winsound.PlaySound('laser.wav', winsound.SND_ASYNC)
            bustate = 'fire'
            # firing the bullet
            x = player.xcor()
            y = player.ycor() + 10
            bu.setposition(x, y)
            bu.showturtle()

    def iscollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        if distance < 15:
            return True
        else:
            return False

    # create keyboard movement
    wn.listen()
    wn.onkeypress(left, 'Left')
    wn.onkeypress(right, 'Right')
    wn.onkeypress(fb, 'space')

    # main loop
    while True:

        for enemy in enemies:
            # move the enemy
            x = enemy.xcor()
            x += es
            enemy.setx(x)

            # move the enemy back and down
            if enemy.xcor() > 280:
                # move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # change enemy direction
                es *= -1
            if enemy.xcor() < -280:
                # move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # change enemy direction
                es *= -1
            # check for a collision btwn bullet and enemey
            if iscollision(bu, enemy):
                winsound.PlaySound('EXPLOSN.wav', winsound.SND_ASYNC)
                # reset the bullet
                bu.hideturtle()
                bustate = 'ready'
                bu.setposition(0, -400)
                # reset the enemy
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setposition(x, y)
                # updating the score

                score += 10
                scorestring = 'score:%s' % score
                pen.clear()
                pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

            if iscollision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print('Game Over')
                break

            # move the bullet
        if bustate == 'fire':
            y = bu.ycor()
            y += bs
            bu.sety(y)
        # checking bullet state
        if bu.ycor() > 275:
            bu.hideturtle()
            bustate = 'ready'

    wn.mainloop()