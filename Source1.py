from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from random import *
class Editor:
    def __init__(self):
        win=Tk()
        win.title("File Editor")
        frame1=Frame(win)
        frame1.pack()
        save=PhotoImage(file="save.png")
        open=PhotoImage(file="open.png")
        Button(frame1,image=save,command=self.s).pack(side=LEFT)
        Button(frame1,image=open,command=self.o).pack(side=LEFT)
        Button(frame1,text="Change color",command=self.col).pack(side=LEFT)
        frame2=Frame(win)
        frame2.pack()
        scroll=Scrollbar(frame2)
        scroll.pack(side=RIGHT,fill=Y)
        self.text=Text(frame2,width=40,height=20,yscrollcommand=scroll.set,wrap=WORD)
        self.text.pack()
        scroll.config(command=self.text.yview)
        win.mainloop()
    def s(self):
        saveAs=asksaveasfilename()
        file=open(saveAs,'a')
        file.write(self.text.get(1.0,END))
        file.close()
    def o(self):
        openAs=askopenfilename()
        filen=open(openAs,'r')
        self.text.insert(END,filen.read())
        filen.close()
    def col(self):
        color=['red','blue','green','black','brown']
        shuffle(color)
        for c in color:
            self.text["fg"]=c
Editor()




