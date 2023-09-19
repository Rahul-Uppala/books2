from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W,E,N,S, END
from tkinter import ttk
from tkinter import messagebox
from postgres_config import dbConfig

import psycopg2 as pyo

con =pyo.connect(**dbConfig)
print(con) 

class Bookdb:
    def __init__(self) :
        self.con = pyo.connect(**dbConfig)
        self.cursor = self.con.cursor()
        print("You have established a connection ...")
        print(self.con)

    def __del__(self):
        self.con.close()

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows
    
    def insert(self,title,author,isbn):
        sql=("INSERT INTO books (title,author,isbn) VALUES (%s,%s,%s)") 
        values = [ title,author,isbn]
        self.cursor.execute(sql,values)
        self.con.commit()
        messagebox.showinfo(title="Book Database", message="New book added to the Book Table of mybooks DATABASE")
   
    def update(self,id, title,author,isbn):
        update_sql=("UPDATE books SET title=%s, author=%s, isbn =%s WHERE id =%s")
        self.cursor.execute(update_sql, [title, author, isbn, id ])
        self.con.commit()
        messagebox.showinfo(title="mybooks Database", message="Book table updated")
   
    def delete(self,id ):
        delete_sql=("DELETE from books where id =%s")
        self.cursor.execute(delete_sql,[id])
        self.con.commit()
        messagebox.showinfo(title="mybooks Database", message=" row deleted ")


def get_selected_row(event):
	global selected_tuple
	index = list_box.curselection()[0]
	selected_tuple = list_box.get(index)
	title_entry.delete(0,'end') # clears the input after inserting
	title_entry.insert('end', selected_tuple[1])
	author_entry.delete(0,'end')
	author_entry.insert('end',selected_tuple[2])
	isbn_entry.delete(0, 'end')
	isbn_entry.insert('end',selected_tuple[3])    

db = Bookdb()  #  Bookdb is the class created to access 

def view_records():
    list_box.delete(0,'end')
    for row in db.view():
        list_box.insert('end',row) 

def add_book():
    db.insert(title_text.get(), author_text.get(), isbn_text.get() )
    list_box.delete(0, 'end')
    list_box.insert ('end',(title_text.get(), author_text.get(), isbn_text.get()))
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0,'end')
    conn.commit()

def delete_records():
    db.delete(selected_tuple[0])
    conn.commit() 


def clear_screen():
        list_box.delete(0,'end')
        title_entry.delete(0,'end')
        author_entry.delete(0,'end')
        isbn_entry.delete(0,'end')

def update_records():
        db.update(selected_tuple[0], title_text.get(), author_text.get(), isbn_text.get())
        title_entry.delete(0,'end')
        author_entry.delete(0,'end')
        isbn_entry.delete(0,'end')

    
def on_closing():
        dd=db
        if messagebox.askokcancel("Quit","Do you want to quit?"):
            root.destroy()
            del dd


root=Tk() 

root.title("My Books Database Application")
root.configure(background="dark blue") # -- 101010 is blackish grey colour
root.geometry("900x500") #  -- Geometry() to set the dimensions of the tkinter application window. 
root.resizable(False,False) # -- making width, height unchangable 


title_label = ttk.Label(root, text=" Title ",background="black",borderwidth=4, relief= "sunken", foreground ="white" , font=("TkDefaultFont",16))
title_label.place(x=185,y=30)

title_text= StringVar()
title_entry= ttk.Entry(root, width=13, textvariable=title_text)
title_entry.place(x=55,y=30)

author_label = ttk.Label(root, text=" Author ",background="black",borderwidth=4, relief= "sunken", foreground ="white" ,font=("TkDefaultFont",16))
author_label.place(x=405,y=30)

author_text= StringVar()
author_entry= ttk.Entry(root, width=13, textvariable=author_text)
author_entry.place(x=275,y=30)

isbn_label = ttk.Label(root, text=" ISBN ",background="black",borderwidth=4, relief= "sunken", foreground ="white" , font=("TkDefaultFont",16))
isbn_label.place(x=640,y=30)

isbn_text= StringVar()
isbn_entry= ttk.Entry(root, width=13, textvariable=isbn_text)
isbn_entry.place(x=510,y=30)


add_btn = Button(root, text="  Add Book  ",border=4, borderwidth=6,  bg="white",fg="black",font="system 12", command=add_book)
add_btn.place(x=740,y=25) 

list_box = Listbox(root, height=16, width=75, bd = 5, relief= 'solid', font="helvetica 13", bg="light blue")
list_box.place(x=50, y=110) 
list_box.bind('<<ListboxSelect>>',get_selected_row)

scroll_bar = Scrollbar(root)
scroll_bar.place(x=655,y=250)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

viewButton = Button(root, text="View All Records", border=4, borderwidth=6, bg='white', fg='black', font='System 12', command=view_records)
viewButton.place(x=725,y=135)

modifyButton = Button(root, text="  Modify Record  ",border=4, borderwidth=6,  bg='white', fg='black', font='system 12', command=update_records)
modifyButton.place(x=725,y=195)

deleteButton = Button(root, text="  Delete Record  ",border=4, borderwidth=6,  bg='white', fg='black', font='system 12', command=delete_records)
deleteButton.place(x=725,y=255)

clearButton = Button(root, text="   Clear Screen   ", border=4, borderwidth=6, bg='white', fg='black', font='system 12', command=clear_screen)
clearButton.place(x=725,y=315)

exitButton = Button(root, text=" Exit Application ", border=4, borderwidth=6, bg='white', fg='black', font='system 12', command=on_closing)
exitButton.place(x=725,y=375)



root.mainloop() 
