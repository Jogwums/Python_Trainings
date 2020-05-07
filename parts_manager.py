from tkinter import *
from tkinter import messagebox
#import the database file created using sqlite3

from db import Database

db = Database('store.db') #its just going to basically use this not instantiating again


#create functions
def populate_list():
    parts_list.delete(0, END) #this ensures that db entries are not repeated multiple times
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    if part_text.get() == "" or customer_text.get() == "" or retailer_text.get() == "" or price_text.get() == "":
        messagebox.showerror("Error Message","Please No Empty Fields Allowed")
        return
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()) # former placeholder: print('add item')
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    clear_text()
    populate_list()

#there is a need to add validation here so that empty dicts are not added to the db
#this can be done by using tk messagebox
#add this to function add_item as an if statement

def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        print(selected_item) #just a check to see that its selecting the right thing

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(),
                                retailer_text.get(), price_text.get())
    populate_list()


def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)



#Create the frame
app = Tk()

#Part
part_text = StringVar()
part_label = Label(app, text="Part Name", font=('bold',14), pady=20)
part_label.grid(column=0, row=0, sticky=W) #align to left using sticky=W and east , E
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(column=1, row=0, sticky=W)

#Customer
customer_text = StringVar()
customer_label = Label(app, text="Customer Name", font=('bold',14))
customer_label.grid(column=2, row=0, sticky=E) #align to left using sticky=W and east , E
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(column=3, row=0)

#Retailer
retailer_text = StringVar()
retailer_label = Label(app, text="Retailer", font=('bold',14))
retailer_label.grid(column=0, row=1, sticky=W) #align to left using sticky=W and east , E
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(column=1, row=1, sticky=W)

#Price
price_text = StringVar()
price_label = Label(app, text="Price", font=('bold',14))
price_label.grid(column=2, row=1, sticky=W) #align to left using sticky=W and east , E
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(column=3, row=1, sticky=W)

#Parts List = ListBox()   #this is a widget
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(column=0, row=3, columnspan=3, rowspan=6, pady=20, padx=20)

#Create scrollbar and link it to the list box
scrollbar = Scrollbar(app)
scrollbar.grid(column=3, row=3)
#set scroll to list box
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

#Buttons
add_btn = Button(app, text="Add Part", width=12, command=add_item)
add_btn.grid(column=0, row=2, pady=20)

remove_btn = Button(app, text="Remove Part", width=12, command=remove_item)
remove_btn.grid(column=1, row=2)

update_btn = Button(app, text="Update Part", width=12, command=update_item)
update_btn.grid(column=2, row=2)

clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(column=3, row=2)

app.title("Part Manager")
app.geometry("700x350")


#populate the list
populate_list()


#start app
app.mainloop()

#Use this to create one file #pyinstaller parts_manager.py --onefile --windowed
