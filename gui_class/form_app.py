from tkinter import *

window = Tk()
window.title('Contact form')
window.config(bg="grey90")
window.minsize(width=400, height=300)

form_frame = Frame(window)
form_frame.config(padx=20, pady=20, bg="grey89", bd=4, relief='solid')

name_lbl = Label(form_frame, text='Name')
name_lbl.config()
email_lbl = Label(form_frame, text='Email')
tel_lbl = Label(form_frame, text='Telephone')

name_entry = Entry(form_frame)
email_entry = Entry(form_frame)
tel_entry = Entry(form_frame)

submit_btn = Button(form_frame, text='Submit')

# Layout
name_lbl.grid(column=2, row=0)
email_lbl.grid(column=2, row=1)
tel_lbl.grid(column=2, row=2)

name_entry.grid(column=3, row=0)
email_entry.grid(column=3, row=1)
tel_entry.grid(column=3, row=2)
submit_btn.grid(column=2, row=3)

form_frame.grid(column=2, row=0)

window.mainloop()
