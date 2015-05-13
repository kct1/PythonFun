#!/usr/bin/python
from Tkinter import * 
import Calc

root = Tk()
root.title("Tk Calculator")

class CalcGui (object): 
	def __init__ (self):
	# load the calculator engine
	self.calcEngine = Calc.Calculator()
	# now create the gui
	self.labelString = StringVar()
	lab = Label(root, textvariable=self.labelString)
	b0 =Button(root,text="0",command=lambda: self.buttonAction('0')) 
	b1 =Button(root,text="1",command=lambda: self.buttonAction('1')) 
	b2 =Button(root,text="2",command=lambda: self.buttonAction('2')) 
	b3 =Button(root,text="3",command=lambda: self.buttonAction('3')) 
	b4 =Button(root,text="4",command=lambda: self.buttonAction('4')) 
	b5 =Button(root,text="5",command=lambda: self.buttonAction('5')) 
	b6 =Button(root,text="6",command=lambda: self.buttonAction('6')) 
	b7 =Button(root,text="7",command=lambda: self.buttonAction('7')) 
	b8 =Button(root,text="8",command=lambda: self.buttonAction('8')) 
	b9 =Button(root,text="9",command=lambda: self.buttonAction('9')) 
	blp=Button(root,text=" (",command=lambda:self.buttonAction('(')) 
		brp=Button(root,text=" )",command=lambda:self.buttonAction(')')
	bplus=Button(root,text="+",command=lambda:self.buttonAction('+')) 
	bminus=Button(root,text="-",command=lambda:self.buttonAction('-'))

	btimes=Button(root,text="*",command=lambda:self.buttonAction('*')) 
	bdivide=Button(root,text="/",command=lambda: self.buttonAction('/'))
	bclear= Button(root, text="clear", command=self.doClearButton) 
	bcal = Button(root, text="calc", command=self.doCalcButton) 
	bdel = Button(root, text="del", command=self.doDelButton) 
    lab.grid(row=0, column=0, columnspan=4)
	b0.grid(row=1, column=0)
	b1.grid(row=1, column=1)
	b2.grid(row=1, column=2)
	b3.grid(row=1, column=3)
	b4.grid(row=2, column=0)
	b5.grid(row=2, column=1)
	b6.grid(row=2, column=2)
	b7.grid(row=2, column=3)
	b8.grid(row=3, column=0)
	b9.grid(row=3, column=1)
	blp.grid(row=3, column=2) 
	brp.grid(row=3, column=3) 
	bplus.grid(row=4, column=0) 
	bminus.grid(row=4, column=1)
	btimes.grid(row=4, column=2) 
	bdivide.grid(row=4, column=3) 
	bclear.grid(row=5, column=0)
	bcal.grid(row=5, column=1, columnspan=2)
    bdel.grid(row=5, column=3)

def buttonAction (self, c): 
	self.labelString.set(self.labelString.get() + c)
def doClearButton(self): 
	self.labelString.set("")
def doCalcButton(self): 
	self.labelString.set(self.calcEngine.eval(self.labelString.get()))
def doDelButton(self): 
	self.labelString.set(self.labelString.get()[:-1])
if __name__ == “__main__”: # only do if invoked as application c = CalcGui()
root.mainloop()