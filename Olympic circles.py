from tkinter import *
from random import *
def col():
    color = '#'
    for j in range(6):
        color+=hex(randint(0,15))
    return color
def hex(num):
    if 0<=num<=9:
        return chr(num+ord('0'))
    else:
        return chr(num-10+ord('A'))
class Ball:
    def __init__(self):
        self.x=0
        self.y=0
        self.dx=2
        self.dy=2
        self.rad=4
        self.c=col()
class Bounce:
    def __init__(self):
        win=Tk()
        win.title("Bouncing balls")
        self.w=350
        self.h=250
        self.can=Canvas(win,width=self.w,height=self.h,bg="white")
        self.can.pack()
        self.list=[]
        frame=Frame(win)
        frame.pack()
        stop=Button(frame,text="Stop",command=self.st)
        stop.pack(side=LEFT)
        resume=Button(frame,text="Resume",command=self.res)
        resume.pack(side=LEFT)
        inc=Button(frame,text="Add",command=self.add)
        inc.pack(side=LEFT)
        dec=Button(frame,text="Remove",command=self.rem)
        dec.pack(side=LEFT)
        self.sleep=15
        self.stopped=False
        self.animate()
        win.mainloop()
    def st(self):
        self.stopped=True
    def res(self):
        self.stopped=False
        self.animate()
    def add(self):
        self.list.append(Ball())
    def rem(self):
        self.list.pop()
    def animate(self):
        while self.stopped==False:
            self.can.after(self.sleep)
            self.can.update()
            self.can.delete("ball")
            for ball in self.list:
                self.reanim(ball)
    def reanim(self,ball):
        if ball.x>self.w or ball.x<0:
            ball.dx=-ball.dx
        if ball.y>self.h or ball.y<0:
            ball.dy=-ball.dy
        ball.x+=ball.dx
        ball.y+=ball.dy
        self.can.create_oval(ball.x-ball.rad,ball.y-ball.rad,ball.x+ball.rad,ball.y+ball.rad,fill=col(),tags="ball")
Bounce()

