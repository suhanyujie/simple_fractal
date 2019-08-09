# -*- coding: utf-8 -*-

' a $ module '
"""
>* 参考视频 https://www.bilibili.com/video/av28637396?from=search&seid=1910073814438035916
>* 相关论文 http://algorithmicbotany.org/papers/abop/abop-ch1.pdf
"""


__author__ = 'Samuel'

import turtle
import time

length = 5
angle = 90


def main():
    path = 'F-F-F-F'
    turtle.speed(0)
    path = apply_rule(path)
    path = apply_rule(path)
    draw_path(path=path)
    turtle.exitonclick()
    pass


def apply_rule(path=''):
    return path.replace('F', 'F-F+F+FF-F-F+F')
    pass


def draw_path(path=''):
    for symbol in path:
        if symbol == 'F':
            turtle.forward(length)
        elif symbol == '-':
            turtle.left(angle)
        elif symbol == '+':
            turtle.right(angle)
    pass


if __name__ == '__main__':
    main()
