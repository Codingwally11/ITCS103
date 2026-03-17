import tkinter as tk

window = tk.Tk()
window.title("Profile Builder")

window.geometry("600x300")
window.configure(bg="lightgreen", cursor="cross")

toplabel = tk.Label(window,text="Profilde Builder",font = ("Arial",12,"bold"),bg="lightgreen")
toplabel.place(x=240,y=10)

#label
fname = tk.Label(window,text="First Name")
fname.place(x=60,y=80)

mname = tk.Label(window,text="Middle Name")
mname.place(x=250,y=80)

lname = tk.Label(window,text="Last Name")
lname.place(x=450,y=80)

byear = tk.Label(window,text="Birth Year")
byear.place(x=60,y=130)

gender = tk.Label(window,text="Gender")
gender.place(x=60,y=155)


#entry
u_entry = tk.Entry(window)
u_entry.place(x=40,y=60)

m_entry = tk.Entry(window)
m_entry.place(x=230,y=60)

l_entry = tk.Entry(window)
l_entry.place(x=430,y=60)

b_entry = tk.Entry(window)
b_entry.place(x=40,y=110)


#func

def sbtn():
    f = u_entry.get()
    m = m_entry.get()
    l = l_entry.get()
    b = b_entry.get()
    up = tk.Toplevel()
    up.configure(bg="red")
    up.geometry("200x100")

    head = tk.Label(up,text="Student ID")
    head.pack()

    name = f"{f} {m}. {l}"
    
    name1 = tk.Label(up,text=f"Name: {name}")
    name1.pack()

    age = tk.Label(up,text=f"Age:{b}")
    age.pack()

    gender1 = tk.Label(up,text=f"Gender:")
    gender1.pack()



#button

def enter(event):
    sbtn ["bg"] = bg ="pink"

def leave(event):
    sbtn ["bg"] = bg ="green"    

sbtn = tk.Button(window,text="Submit",relief="sunken",bg="pink",command=sbtn)
sbtn.place(x=250,y=190)
sbtn.bind("<Enter>",enter)
sbtn.bind("<Leave>",leave)



#radiobtn

gender1= tk.IntVar()

lalake = tk.Radiobutton(window,text="Male",variable=gender,value=1)
lalake.place(x=230,y=150)

babae = tk.Radiobutton(window,text="Female",variable=gender,value=2)
babae.place(x=300,y=150)

window.mainloop()