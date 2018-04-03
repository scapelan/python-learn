# 使用turtle库画出一条蟒蛇

# 引入turtle标准库
import turtle

# setup(width, height, startx, starty)确定绘图窗体宽高和初始位置
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize()
turtle.pencolor('purple')
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.down()
