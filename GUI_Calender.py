#Use tkinter
from tkinter import *
import calendar
from calendar import timegm

#create a function for showing the calendar

def showCal():

    #create a new GUI
    new_gui = Tk()

    #set the background color of the GUI
    new_gui.config(background = "white")

    #set the name of the GUI Window
    new_gui.title("CALENDAR")

    #set the configuration of the GUI window
    new_gui.geometry("550x600")

    #get method returns current text as string
    fetch_year = int(year_field.get())

    #calender method returns the calendar of the given year
    cal_content = calendar.calendar(fetch_year)

    #create a label for showing the content of the calendar
    cal_year = Label(new_gui, text = cal_content, font= "Consolas 10 bold")

    #grid method is used for placing the widgets at respective positions
    #in a table-like structure
    cal_year.grid(row=5, column=1, padx=20)

    #start the GUI
    new_gui.mainloop()

if __name__ == "__main__":

    #create a GUI window
    gui = Tk()

    # set the background color of the GUI
    gui.config(background="white")

    # set the name of the GUI Window
    gui.title("CALENDAR")

    # set the configuration of the GUI window
    gui.geometry("550x600")

    #create a Calendar : Label with specified font size
    cal = Label(gui, text = "CALENDAR", bg="dark gray", font=("times", 28, "bold"))

    #create an enter Year : label
    year = Label(gui, text="Enter Year", bg="light green")

    #create a text entry box for filling or typing the information
    year_field = Entry(gui)

    # create a Show Calendar button and attach to ShowCal function
    Show = Button(gui, text=" SHOW CALENDAR", fg="black" , bg="red", command= showCal)

    # create an Exit Calendar button and attach to an exit function
    Exit = Button(gui, text=" EXIT", fg="black", bg="red", command= exit)

    # grid method is used for placing the widgets at respective positions
    # in a table-like structure
    cal.grid(row=1, column=1)

    year.grid(row=1, column=1)

    year_field.grid(row=3, column=1)

    Show.grid(row=4, column=1)

    Exit.grid(row=6, column=1)

    #start the GUI
    gui.mainloop()








