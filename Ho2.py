import tkinter as tk

window = tk.Tk()

window.title("Oswald Pastorfide's Profile")
window.geometry("600x600")
window.resizable(False,True)
window.configure(bg="pink",cursor="hand2")
label = tk.Label (window, text = '𝒮𝓉𝓊𝒹ℯ𝓃𝓉 𝒫𝓇ℴ𝒻𝒾𝓁ℯ', font=('Arial',30,'bold'),  fg='red', bg= 'pink', anchor='center')
label.pack()

label1 = tk.Label (window, text = 'Name : Oswald Pastorfide', font=('Arial',20,'bold'), fg='black', bg='white',)
label1.pack(padx=5,pady=20, anchor="w")

label2 = tk.Label (window, text = 'Age : 22 years old', font=('Arial',20,'bold'), fg='green', bg='yellow',)
label2.pack(padx=5,pady=20, anchor="w")

label3 = tk.Label (window, text = 'Course : BSIT', font=('Arial',20,'bold'), fg='red', bg='black',)
label3.pack(padx=5,pady=20, anchor="w")

label4 = tk.Label (window, text = 'Birthday : January 27, 2004', font=('Arial',20,'bold'), fg='yellow', bg='orange',)
label4.pack(padx=5,pady=20, anchor="w")

label5 = tk.Label (window, text = 'Motto :', font=('Arial',20,'bold'), fg='blue', bg='purple',)
label5.pack(padx=5,pady=20, anchor="w")

label6 = tk.Label (window, text =   'Motorcycle', font=('Arial',20,'bold'), fg='white', bg='green',)
label6.pack(padx=5,pady=20, anchor="w")

window.mainloop()