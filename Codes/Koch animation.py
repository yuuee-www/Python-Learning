import time
import random
import turtle

def koch(len,target):
    tasks = '000'
    step,depth = len/(3**target),0
    while depth < target:
        depth += 1
        tasks = ''.join([s + str(depth)*2 + s for s in tasks])
    pre = ''
    for task in tasks:
        if pre == task:
            turtle.right(120)
        else:
            turtle.left(60)
        turtle.forward(step)
        pre = task

def snowflake(level=3,width=150):
    koch(width,level)
    turtle.right(180)

def main():
    random.seed()
    sn = random.randint(75,100)
    print("生成雪花",sn)
    level1 = 2
    width1 = 24
    x = []
    y = []
    for i in range(0,sn):
        x.append(random.randint(-200,200))
        y.append(random.randint(-300,300))

    turtle.hideturtle()
    turtle.pensize(1)
    turtle.speed(1)

    for i in range(1000):
        turtle.tracer(False)

        turtle.clear()

        for co in range(sn):
            turtle.pu()
            turtle.goto(x[co],y[co])
            turtle.pd()
            snowflake(level1,width1)

        for co in range(sn):
            x[co]+=random.uniform(-1,1)
            y[co]-=random.uniform(1,3)

            if y[co]<-300:
                y[co]+=600

        time.sleep(0.01)
        turtle.tracer(True)

main()
