import turtle
import time

score_a = 0
score_b = 0


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=1000,height=700)
wn.tracer(0)


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-480,0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.penup()
paddle_b.goto(470,0)


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Player A: 0    Player B: 0",align="center",font=("Arial",20,'normal'))


Winner = turtle.Turtle()
Winner.speed(0)
Winner.color("white")
Winner.penup()
Winner.hideturtle()
Winner.goto(0,0)
Winner.write("{} has won this round.".format,align="center",font=("Arial",20,'normal'))



def paddle_a_up():
    y = paddle_a.ycor()
    if y==300:
        y=y+0
    else:
        y=y+30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y==-300:
        y=y+0
    else:
        y=y-30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y==300:
        y=y+0
    else:
        y=y+30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y==-300:
        y=y+0
    else:
        y=y-30
    paddle_b.sety(y)



wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=0.3

game_over = False
while True:
    Winner.clear()
    wn.update()
    if game_over == True:
        ball.goto(0,0)
        Winner.goto(0,0)
        if score_a>score_b:
            win = "Player A has won this round."
        elif(score_b>score_a):
            win = "Player B has won this round."
        else:
            win = "It's a tie."
        Winner.write("{}".format(win),align="center",font=("Arial",20,'normal'))
        time.sleep(5)
        score_a = 0
        score_b = 0
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a,score_b),align="center",font=("Arial",20,'normal'))
        Winner.clear()
        game_over = False

    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor()>340:
        ball.sety(340)
        ball.dy=ball.dy * (-1)

    if ball.ycor()<-340:
        ball.sety(-340)
        ball.dy=ball.dy * (-1)

    if ball.xcor()>495:
        ball.goto(0,0)
        ball.dx = ball.dx * (-1)
        game_over = True

    if ball.xcor()<-495:
        ball.goto(0,0)
        ball.dx=ball.dx * (-1)
        game_over = True
    
    if (ball.xcor()>455 and ball.xcor()<470 and ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        ball.setx(455)
        ball.dx*=-1
        #winsound.PlaySound('bounce.mp3',winsound.SND_ASYNC)
        score_b+=1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a,score_b),align="center",font=("Arial",20,'normal'))

    if (ball.xcor()<-455 and ball.xcor()>-470 and ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.setx(-455)
        ball.dx*=-1    
        #winsound.PlaySound('bounce.mp3',winsound.SND_ASYNC)
        score_a+=1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a,score_b),align="center",font=("Arial",20,'normal'))
