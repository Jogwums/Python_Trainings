import tkinter
from tkinter import *


# Create the calculator frame

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


# Creating button

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
              justify='right',
              bd=30, bg="powder blue").pack(side=TOP, expand=YES, fill=BOTH)

        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''))

        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda
                    storeObj=display, q=iEquals: storeObj
                       .set(storeObj.get() + q))

        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e, s=self,
                                                            storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                    (storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

# Start the GUI
if __name__ == '__main__':
    app().mainloop()


# Add a display widget by inserting the following code into the class app
'''
    display = StringVar()
            Entry(self, relief=RIDGE, textvariable=display,
            justify='right', bd =30, bg="powder blue").pack(side=TOP, expand=YES, fill=BOTH)
'''
# Add a clear button widget

'''
    for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''))
'''

# Add Keypad and numbers button
'''
    for numButton in ("789/", "456*", "123-", "0.+"):
         FunctionNum = iCalc(self, TOP)
         for iEquals in numButton:
            button(FunctionNum, LEFT, iEquals, lambda
                storeObj=display, q=iEquals: storeObj
                   .set(storeObj.get() + q))
'''

# Add equal button

'''
    EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')
                                
            else:
            btniEquals = button(EqualButton, LEFT, iEquals,
                                lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                (storeObj.get() + s))
'''

# Add the Event triggers
# Now the last thing but very important is to apply event triggers on widgets.
# It means whenever you click any widget some function will be performed. So write the following code

'''
    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")
'''
