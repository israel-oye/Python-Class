from tkinter import *

window = Tk()

window.title('First app')
window.config(bg="teal")
# window.geometry("600x500")
window.minsize(width=400, height=300)

label = Label(text='Km ➡️ Miles', font=('serif', 14, 'bold'))
value_label = Label(text='Miles: ', font=('Arial', 12), fg='dark slate gray')
# label.config(text='Updated value')
# Button and Entry widgets in TKinter
text_input = Entry()

def convert_to_miles():
    entered_text = text_input.get()
    miles = float(entered_text) * 0.62137119
    value_label.config(text=f'Miles: {miles:.2f}')

def clear_input():
    text_input.delete(0, 'end')

# Print the last character of the text input as the
# value of a label on a button click
# Add a button to clear the input


submit_btn = Button(text='Click me', command=convert_to_miles)
clear_btn = Button(text='Clear', command=clear_input)




label.pack(pady=10)
text_input.pack()
submit_btn.pack(pady=5)
clear_btn.pack(pady=5)
value_label.pack(pady=10)

window.mainloop()