import tkinter as tk

window = tk.Tk()

window.title("Register and Log In")
window.geometry("400x200")
window.resizable(False, False)
window.configure(bg = "pink")

#Label
welkam = tk.Label(window, text="Welcome!", bg="pink",font = ("Arial",20,"bold"))
welkam.place(x=150,y=10)


#Funtion
def register():
    reg_level = tk.Toplevel(window)
    reg_level.geometry("300x300")
    reg_level.title("Registration")
    reg_level.configure(bg="pink")

    u_name = tk.Label(reg_level,text="Username:")
    u_name.place(x=20, y=40)

    pword = tk.Label(reg_level,text="Password:")
    pword.place(x=20, y=70)

    u_entry = tk.Entry(reg_level)
    u_entry.place(x=90,y=40)

    pword = tk.Entry(reg_level)
    pword.place(x=90, y=70)

    reg = tk.Button(reg_level,text = "Register",bg = "green",fg="white")
    reg.place(x=50, y=130)

    def show():
        show = int(var.get())
        if show == 1:
            pword["show"]=""
        else:
            pword["show"]="*"
    var = tk.IntVar()
    btn = tk.Checkbutton(reg_level,text="See Password",variable=var,onvalue=1,offvalue=0, bg= "white",command=show)
    btn.place(x=70, y=100)




def login():
    log_level = tk.Toplevel(window)
    log_level.geometry("300x300")
    log_level.title("Log In")
    log_level.configure(bg="pink")

    u_name = tk.Label(log_level,text="Username:")
    u_name.place(x=20, y=40)

    pword = tk.Label(log_level,text="Password:")
    pword.place(x=20, y=70)

    u_entry = tk.Entry(log_level)
    u_entry.place(x=90,y=40)

    pword = tk.Entry(log_level)
    pword.place(x=90, y=70)

    btn = tk.Checkbutton(log_level,text="See Password", bg= "white",command=login)
    btn.place(x=70, y=100)

    reg = tk.Button(log_level,text = "Log In",bg = "green",fg="white")
    reg.place(x=50, y=130)

    log = tk.Label(log_level,text="Log In",bg="pink",font = ("Arial",20,"bold"))
    log.pack(x=10, y=20)



#Button
login = tk.Button(window,text = "Log In",bg = "green",fg="white",font=("Arial",15,"bold"),padx=200,command=login)
login.place(x=-10, y=100)

register = tk.Button(window,text = "Register",bg = "red",fg="blue",font=("Arial",15,"bold"),padx=200,command=register)
register.place(x=-10, y=50)



window.mainloop()