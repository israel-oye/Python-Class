from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title('Image Display')

window.minsize(width=500, height=400)

image = Image.open('gui_class/image-1.jpg')
image = image.resize((300, 200))

photo = ImageTk.PhotoImage(image)

new_label = Label(window, image=photo)
new_label.pack()

window.mainloop()