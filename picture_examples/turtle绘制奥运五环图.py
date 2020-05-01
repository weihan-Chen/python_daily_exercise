'''
@Description:
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-05-01 23:58:11
@LastEditTime: 2020-05-02 00:04:22
'''
import turtle as p


def draw_circle(x, y, c="red"):
    p.pu()  # 抬起画笔
    p.goto(x, y)  # 圆的起始位置
    p.pd()  # 放下画笔
    p.color(c)  # 设置颜色
    p.circle(30, 360)  # 绘制圆：半径，角度


p.pensize(3)
draw_circle(0, 0, "blue")
draw_circle(60, 0, "black")
draw_circle(120, 0, "red")
draw_circle(90, -30, "green")
draw_circle(30, -30, "yellow")

p.done()
