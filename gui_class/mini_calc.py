from tkinter import *

# window = Tk()
# window.geometry('300x360')

class MiniCalc(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Mini Calc')
        self.minsize(width=300, height=200)
        self.config(bg='snow')

        self.input_field = Entry(self)
        self.submit_btn = Button(self, text='Submit')

        self.input_field.pack()
        self.submit_btn.pack()
        # print(self.input_field)
        # self.place_child(child=self.input_field, coordinate=(100, 200,))
        # self.place_child(child=self.submit_btn, coordinate=(100, 250))

    def place_child(child: Widget, coordinate: tuple[int, int]):
        child.place(x=coordinate[0], y=coordinate[1])


# def display():
#     myapp = MiniCalc()


# Button(window, text='Diplay', command=display).pack()
# window.mainloop()

myapp = MiniCalc()
myapp.mainloop()