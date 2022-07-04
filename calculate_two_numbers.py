
import tkinter
from tkinter import messagebox


main_window = tkinter.Tk()
main_window.geometry("300x300+300+300")
main_window.title("Calculate two numbers")

frame = tkinter.Frame(main_window)
frame.pack(padx=10, pady=10, expand=True)

label_first_field = tkinter.Label(
    frame,
    text="Enter first number:",
    font=("Arial", 18)
)

first_value = tkinter.IntVar()
entry_first_value = tkinter.Entry(
    frame,
    textvariable=first_value
)

label_first_field.pack(
    ipadx=5,
    ipady=5
)

entry_first_value.pack(fill="x")

label_second_field = tkinter.Label(
    frame,
    text="Enter second number:",
    font=("Arial", 18)
)

label_second_field.pack(
    ipadx=5,
    ipady=5
)

second_value = tkinter.IntVar()
entry_second_value = tkinter.Entry(
    frame,
    textvariable=second_value
)

entry_second_value.pack(fill="x")

#=========================================
#making this work
#=========================================



def sum_operation():
    
    get_first_field = int(first_value.get())
    get_second_field = int(second_value.get())
    
    result = get_first_field + get_second_field
    messagebox.showinfo(message=result)

def subtraction_operation():
    
    get_first_field = int(first_value.get())
    get_second_field = int(second_value.get())
    
    result = (get_first_field - get_second_field)
    messagebox.showinfo(message=result)

def multiplication_operation():
    get_first_field = int(first_value.get())
    get_second_field = int(second_value.get())
    
    result = (get_first_field * get_second_field)
    messagebox.showinfo(message=result)

def division_operation():
    get_first_field = int(first_value.get())
    get_second_field = int(second_value.get())
    
    result = (get_first_field / get_second_field)
    messagebox.showinfo(message=result)

#================================================
#buttons
#================================================
sum_button = tkinter.Button(
    frame,
    text="Sum",
    bg="gray",
    command=sum_operation
).pack(
    pady=10,
    side="left"
)

subtract_button = tkinter.Button(
    frame,
    text="Subtract",
    bg="gray",
    command=subtraction_operation
).pack(pady=10, side="right")

multiply_button = tkinter.Button(
    frame,
    text="Multiplication",
    bg="gray",
    command=multiplication_operation
).pack(pady=10, side="bottom")

division_button = tkinter.Button(
    frame,
    text="Division",
    bg="gray",
    command=division_operation
).pack(pady=10, side="top")



main_window.mainloop()