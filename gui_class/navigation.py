from tkinter import *

window = Tk()
window.title('Multi Windows')
window.minsize(width=300, height=250)


def change_window():
    new_window = Toplevel()

    new_window.geometry('200x150')
    new_window.config(bg='grey49')

    label = Label(new_window, text='New Window', font=('Arial', 24))
    label.place(x=90, y=65)
    change_btn = Button(new_window, text='New Window', command=change_window_2)
    change_btn.place(x=80, y=80)

def change_window_2():
    new_window = Toplevel()

    new_window.geometry('200x150')
    new_window.config(bg='tomato2')

    label = Label(new_window, text='New Window', font=('Arial', 24))
    label.place(x=90, y=65)
    



change_btn = Button(text='New Window', command=change_window)
change_btn.place(x=140, y=100)












window.mainloop()