from tkinter import *

window = Tk()
window.title('Theme Switcher')
window.minsize(width=300, height=250)

# def switch_theme():
#     current_color = window.cget('bg')
#     new_color = 'lightblue' if current_color == 'lightgrey' else 'lightgrey'
#     window.config(bg=new_color)

# switch_btn = Button(text='Switch Theme', command=switch_theme)
# switch_btn.place(x=120, y=100)  
mode = StringVar(value='None')
sex = StringVar()
age = IntVar()

def toggle_theme():
    if mode.get() == 'dark':
        window.config(bg='grey29')
        return
    window.config(bg='snow')

dark_radio = Radiobutton(window, variable=mode, text='Dark', value='dark', command=toggle_theme)
light_radio = Radiobutton(window, variable=mode, text='Light', value='light', command=toggle_theme)

dark_radio.place(x=120, y=100)
light_radio.place(x=120, y=120)

male_radio = Radiobutton(text='Male', variable=sex, value='M')
female_radio = Radiobutton(text='Female', variable=sex, value='F')

male_radio.place(x=120, y=140),
female_radio.place(x=120, y=160)

window.mainloop()