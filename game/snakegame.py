import turtle
import time
import random
import winsound
import datetime
global delay
day = int(datetime.datetime.now().day)
month = int(datetime.datetime.now().month)
srt = datetime.datetime.now().strftime('%H:%M:%S')

def play():
    f = open('file.txt', 'a')
    f.write(f'Game: Snake game,Date:{day},Month:{month},Start time:{srt}\n')
    f.close()
    delay = 0.1
    # score
    score = 0
    high_score = 0
    # screen
    wn = turtle.Screen()
    wn.title('snake game')
    wn.bgcolor('black')
    wn.setup(width=600, height=600)
    wn.tracer(0)

    # snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape('square')
    head.color('white')
    head.penup()
    head.goto(0, 0)
    head.direction = 'stop'

    # food
    food = turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color('red')
    food.penup()
    food.goto(0, 100)

    segments = []
    # pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 270)
    pen.write('Score: 0  High Score:0', align='center', font=('Times new roman', 24, 'bold'))

    # function
    def go_up():
        if head.direction != 'down':
            head.direction = 'up'

    def go_down():
        if head.direction != 'up':
            head.direction = 'down'

    def go_left():
        if head.direction != 'right':
            head.direction = 'left'

    def go_right():
        if head.direction != 'left':
            head.direction = 'right'

    def move():

        if head.direction == 'up':
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == 'down':
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == 'left':
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == 'right':
            x = head.xcor()
            head.setx(x + 20)

    # key
    wn.listen()
    wn.onkeypress(go_up, 'Up')
    wn.onkeypress(go_down, 'Down')
    wn.onkeypress(go_left, 'Left')
    wn.onkeypress(go_right, 'Right')
    # main loop

    while True:
        wn.update()


        # check for a collision with wall
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:

            winsound.PlaySound('die.wav', winsound.SND_ASYNC)
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # hiding the segments
            for segment in segments:
                segment.goto(1000, 1000)
            # clear the list
            segments.clear()
            # reset score
            score = 0

            # reset the delay
            delay = 0.1
            pen.clear()
            pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center',
                      font=('Times new roman', 24, 'bold'))
        # check collision
        if head.distance(food) < 20:
            # move food
            #put sound here
            winsound.PlaySound('snake.wav', winsound.SND_ASYNC)
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)
            # segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape('square')
            new_segment.color('grey')
            new_segment.penup()
            segments.append(new_segment)

            # shorten the delay
            delay -= 0.001

            # increase the score
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center',
                      font=('Times new roman', 24, 'bold'))
        # move the end segments first in rev order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        # move seg 0 to head
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()
        # check for head collision with body
        for segment in segments:

            if segment.distance(head) < 20:
                #die sound

                winsound.PlaySound('die.wav', winsound.SND_ASYNC)
                time.sleep(1)
                head.goto(0, 0)
                head.direction = 'stop'

                # hiding the segments
                for segment in segments:
                    segment.goto(1000, 1000)
                # clear the list
                segments.clear()
                # reset score
                score = 0
                # reset the delay
                delay = 0.1
                pen.clear()
                pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center',
                          font=('Times new roman', 24, 'bold'))

        time.sleep(delay)
    wn.mainloop()

