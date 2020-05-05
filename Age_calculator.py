import tkinter as tk
from PIL import Image, ImageTk
import datetime

window = tk.Tk()
window.geometry("400x400")
window.title("Age Calculator App")

name = tk.Label(text="Name")
name.grid(row=1, column=0)

year = tk.Label(text="Year")
year.grid(row=2, column=0)

month = tk.Label(text="Month")
month.grid(row=3, column=0)

date = tk.Label(text="Day")
date.grid(row=4, column=0)

nameEntry = tk.Entry()
nameEntry.grid(row=1, column=1)

yearEntry = tk.Entry()
yearEntry.grid(row=2, column=1)

monthEntry = tk.Entry()
monthEntry.grid(row=3, column=1)

dateEntry = tk.Entry()
dateEntry.grid(row=4, column=1)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age


def getInput():
    name = nameEntry.get()
    monkey = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))

    textArea = tk.Text(master=window, height=10, width=25)
    textArea.grid(row=6, column=1)
    answer = "Hey {monkey}!!!. You are {age} years old!!! ".format(monkey=name, age=monkey.age())
    textArea.insert(tk.END, answer)


button = tk.Button(window, text="Calculate Age", bg="green", command=getInput)
button.grid(row=5, column=1)

image = Image.open('app_image.png')
image.thumbnail((300,300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image= tk.Label(image=photo)
label_image.grid(row=0, column=1)

window.mainloop()
