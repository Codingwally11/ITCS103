
import tkinter as tk

window = tk.Tk()
window.title("Calculator")

window.geometry("300x200")
window.configure(bg="pink", cursor="cross")

toplabel = tk.Label(window,text="simple calculator")
toplabel.place(x=100,y=10)




#Label
label1=tk.Label(window,text = "Enter the first number:")
label1.place(x=5,y=40)

label2=tk.Label(window,text = "Enter the second number:")
label2.place(x=5,y=70)

#Entry
labent = tk.Entry(window)
labent.place(x=170,y=40)

labent2 = tk.Entry(window)
labent2.place(x=170,y=70)

def add():
    num1 = float(labent.get())
    num2 = float(labent2.get())
    result = num1 + num2
    toplabel ["text"] = f"The addition of {num1} + {num2} = {result}"


def subtraction():
    num1 = float(labent.get())
    num2 = float(labent2.get())
    result = num1 - num2
    toplabel ["text"] = f"The subtraction of {num1} - {num2} = {result}"


def multiplication():
    num1 = float(labent.get())
    num2 = float(labent2.get())
    result = num1 * num2
    toplabel ["text"] = f"The multiplication of {num1} x {num2} = {result}"

def division():
    num1 = float(labent.get())
    num2 = float(labent2.get())
    result = num1 / num2
    toplabel ["text"] = f"The division of {num1} / {num2} = {result}"

add_btn = tk.Button(window,text="add",bg="red",fg="pink",font=("Arial",10,"bold"),command=add)
sub_btn = tk.Button(window,text="subtraction",bg="red",fg="pink",font=("Arial",10,"bold"),command=subtraction)
mul_btn = tk.Button(window,text="multiply",bg="red",fg="pink",font=("Arial",10,"bold"),command=multiplication)
div_btn = tk.Button(window,text="divide",bg="red",fg="pink",font=("Arial",10,"bold"),command=division)

add_btn.place(x=63,y=100)
sub_btn.place(x=150,y=100)
mul_btn.place(x=50,y=150)
div_btn.place(x=163,y=150)


window.mainloop()