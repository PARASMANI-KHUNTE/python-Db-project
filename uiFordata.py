import mysql.connector as con
import tkinter as tk
from tkinter import messagebox

connection = con.connect(host='localhost', user='root', password='root')
cursor = connection.cursor()
cursor.execute("show databases like 'plan'")
check = cursor.fetchall()

# Below code will check whether the database is present or not. If it is, it will use it; otherwise, it will create a new one.
if not check:
    cursor.execute("create database plan")
    print("Database not found, so created a new one!!")
    cursor.execute("use plan")
    print("Database has been selected!!")

else:
    cursor.execute("use plan")
    print("Database has been selected!!")

# Database has been selected this far

cursor.execute("CREATE TABLE IF NOT EXISTS list (GoodHabbits VARCHAR(50), BadHabbits VARCHAR(50))")
print("Table 'list' created successfully!!")


def add_element():
    good_things = entry_good.get()
    bad_things = entry_bad.get()
    try:
        sql = 'insert into list(GoodHabbits, BadHabbits) values(%s, %s)'
        val = (good_things, bad_things)
        cursor.execute(sql, val)
        connection.commit()
        messagebox.showinfo("Success", "Successfully entered elements!!")

    except ValueError:
        messagebox.showerror("Error", "An error occurred while entering elements. Please check your input.")


def view():
    cursor.execute("SELECT * FROM list")
    elements = cursor.fetchall()
    listbox.delete(0, tk.END)
    for element in elements:
        listbox.insert(tk.END, element)


def delete():
    try:
        cursor.execute("delete from list")
        connection.commit()
        messagebox.showinfo("Success", "All data has been successfully deleted!!")

    except ValueError:
        messagebox.showerror("Error", "An error occurred while deleting data. Please try again.")


# Tkinter GUI setup
root = tk.Tk()
root.title("Database Interaction")

label_good = tk.Label(root, text="Good Habits:")
label_good.pack()

entry_good = tk.Entry(root)
entry_good.pack()

label_bad = tk.Label(root, text="Bad Habits:")
label_bad.pack()

entry_bad = tk.Entry(root)
entry_bad.pack()

button_add = tk.Button(root, text="Add Element", command=add_element)
button_add.pack()

button_view = tk.Button(root, text="View List", command=view)
button_view.pack()

button_delete = tk.Button(root, text="Delete List", command=delete)
button_delete.pack()

listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()
