from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_row
        index = ls.curselection()[0]
        selected_row = ls.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_row[1])
        e2.delete(0,END)
        e2.insert(END, selected_row[2])
        e3.delete(0,END)
        e3.insert(END, selected_row[3])
        e4.delete(0,END)
        e4.insert(END, selected_row[4])
    except IndexError:
        pass

def view_command():
    ls.delete(0, END)
    for row in backend.view():
        ls.insert(END, row)

def search_command():
    ls.delete(0, END)
    for row in backend.search(e1_title.get(), e2_author.get(), e3_year.get(), e4_isbn.get()):
        ls.insert(END, row)

def add_command():
    backend.insert(e1_title.get(), e2_author.get(), e3_year.get(), e4_isbn.get())
    ls.delete(0, END)
    ls.insert(END, (e1_title.get(), e2_author.get(), e3_year.get(), e4_isbn.get()))

def delete_command():
    backend.delete(selected_row[0])

def update_command():
    backend.update(selected_row[0],e1_title.get(), e2_author.get(), e3_year.get(), e4_isbn.get())

window = Tk()

window.wm_title("BookStore")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l1 = Label(window, text="Author")
l1.grid(row=0, column=2)

l1 = Label(window, text="Year")
l1.grid(row=1, column=0)

l1 = Label(window, text="ISBN")
l1.grid(row=1, column=2)

e1_title = StringVar()
e1 = Entry(window, textvariable=e1_title)
e1.grid(row=0, column=1)

e2_author = StringVar()
e2 = Entry(window, textvariable=e2_author)
e2.grid(row=0, column=3)

e3_year = StringVar()
e3 = Entry(window, textvariable=e3_year)
e3.grid(row=1, column=1)

e4_isbn = StringVar()
e4 = Entry(window, textvariable=e4_isbn)
e4.grid(row=1, column=3)

ls = Listbox(window, height=6, width=35)
ls.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

ls.configure(yscrollcommand=sb1.set)
sb1.configure(command=ls.yview())

ls.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
