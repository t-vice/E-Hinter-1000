#E-Hider 1000 for all your rudimentary email address encryption needs!
import tkinter as tk

#window/w
w = tk.Tk()
w.title("E-Hider 1000")
w.geometry("600x300")

#Labels
line1 = tk.Label(text="Enter an email to turn into an e-hint")
line1.grid(column=0,row=0)
email_label = tk.Label(text="Email:")
email_label.grid(column=0,row=1)

#Buttons
email_entry = tk.Entry(width=30)
email_entry.grid(column=1,row=1)

#input
def getInput():
    email_label = email_entry.get()
    id1 = 2
    id2 = email_label.index("@") - 1
    hinter = (email_label[:id1] + "*" * (id2 - id1) + email_label[id2:])
    textarea = tk.Text(master=w,height=10,width=25)
    textarea.grid(column=1,row=3)
    answer = (email_label[:id1] + "*" * (id2 - id1) + email_label[id2:])
    textarea.insert(tk.END,answer)

#Ehint Button
ehint_button = tk.Button(w, text="Encrypt", command=getInput, bg="red")
ehint_button.grid(column=1, row=2)

#Mainloop
w.mainloop()