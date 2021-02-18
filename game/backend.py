import turtle
import datetime
day = int(datetime.datetime.now().day)
month = int(datetime.datetime.now().month)
srt = datetime.datetime.now().strftime('%H:%M:%S')
def pong():
    f = open('file.txt', 'a')
    f.write(f'Game: Pong game,Date:{day},Month:{month},Start time:{srt}\n')
    f.close()
    wn = turtle.Screen()
    wn.title('Pong')
    wn.bgcolor('white')
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Score
    s_a = 0
    s_b = 0

    # paddle A
    p_a = turtle.Turtle()
    p_a.speed(0)
    p_a.shape('square')
    p_a.color('black')
    p_a.shapesize(stretch_wid=5, stretch_len=1)
    p_a.penup()
    p_a.goto(-350, 0)
    # paddle B
    p_b = turtle.Turtle()
    p_b.speed(0)
    p_b.shape('square')
    p_b.color('black')
    p_b.shapesize(stretch_wid=5, stretch_len=1)
    p_b.penup()
    p_b.goto(350, 0)
    # ball
    b = turtle.Turtle()
    b.speed(0)
    b.shape('circle')
    b.color('red')
    b.penup()
    b.goto(0, 0)
    b.dx = 1
    b.dy = 1

    # pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('black')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write('Player A: 0 Player B: 0', align='center', font=('times', 24, 'bold'))

    # Function
    def p_a_up():
        y = p_a.ycor()
        y += 20
        p_a.sety(y)

    def p_a_down():
        y = p_a.ycor()
        y -= 20
        p_a.sety(y)

    def p_b_up():
        y = p_b.ycor()
        y += 20
        p_b.sety(y)

    def p_b_down():
        y = p_b.ycor()
        y -= 20
        p_b.sety(y)

    # keyboard bindling
    wn.listen()
    wn.onkeypress(p_a_up, 'w')
    wn.onkeypress(p_a_down, 's')
    wn.onkeypress(p_b_up, 'Up')
    wn.onkeypress(p_b_down, 'Down')

    # main loop
    while True:
        wn.update()

        # moving the ball
        b.setx(b.xcor() + b.dx)
        b.sety(b.ycor() + b.dy)

        # border checking
        if b.ycor() > 290:
            b.sety(290)
            b.dy *= -1
        if b.ycor() < -290:
            b.sety(-290)
            b.dy *= -1
        if b.xcor() > 390:
            b.goto(0, 0)
            b.dx *= -1
            s_a += 1
            pen.clear()
            pen.write('Player A: {} Player B: {}'.format(s_a, s_b), align='center', font=('times', 24, 'bold'))

        if b.xcor() < -390:
            b.goto(0, 0)
            b.dx *= -1
            s_b += 1
            pen.clear()
            pen.write('Player A: {} Player B: {}'.format(s_a, s_b), align='center', font=('times', 24, 'bold'))

        # paddle and ball collision
        if (b.xcor() > 340 and b.xcor() < 350) and (b.ycor() < p_b.ycor() + 40 and b.ycor() > p_b.ycor() - 40):
            b.setx(340)
            b.dx *= -1
        if (b.xcor() < -340 and b.xcor() > -350) and (b.ycor() < p_a.ycor() + 40 and b.ycor() > p_a.ycor() - 40):
            b.setx(-340)
            b.dx *= -1
