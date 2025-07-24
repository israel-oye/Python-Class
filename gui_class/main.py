from tkinter import *

window = Tk()

window.title('First app')
window.config(bg="teal")
# window.geometry("600x500")
window.minsize(width=400, height=300)

label = Label(text='Label', font=('serif', 16, 'bold'))
label.pack(side='left')
# label.config(text='Updated value')
# Button and Entry widgets in TKinter








window.mainloop()