from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Contact form")
window.config(bg="grey90")
window.minsize(width=400, height=300)

form_frame = Frame(window)
form_frame.config(padx=20, pady=20, bg="grey89", bd=4, relief="solid")

name_lbl = Label(form_frame, text="Name")
name_lbl.config()
email_lbl = Label(form_frame, text="Email")
tel_lbl = Label(form_frame, text="Telephone")

name_entry = Entry(form_frame)
email_entry = Entry(form_frame)
tel_entry = Entry(form_frame)

submit_btn = Button(form_frame, text="Submit")

list_box = Listbox()
for name in ['Ajayi', 'Babalola', 'Dosumnu', 'Erinle']:
    list_box.insert(END, name)
get_list_btn = Button(text='Get item')
item_display_lbl = Label(text='List Item')
displayed_item = Label()
# Layout
name_lbl.grid(column=2, row=0)
email_lbl.grid(column=2, row=1)
tel_lbl.grid(column=2, row=2)

name_entry.grid(column=3, row=0)
email_entry.grid(column=3, row=1)
tel_entry.grid(column=3, row=2)
submit_btn.grid(column=2, row=3)

form_frame.grid(column=2, row=0)

list_box.grid(column=2, row=1)
get_list_btn.grid(column=4, row=0)
item_display_lbl.grid(column=4, row=1)
# displayed_item.grid(column=4, row=2)

# Event handlers
def validate():
    confirm = messagebox.askyesno('Submit', 'Are you sure to submit')

    if confirm and not name_entry.get():
        messagebox.showerror('Error', 'Enter a valid name')
        return False
    return True

def on_submit():
    if validate():
        username = name_entry.get()
        list_box.insert(END, username)
        name_entry.delete(0, END)
        messagebox.showinfo("Info", message="Form submitted")

def on_get_list():
    item_display_lbl.config(text=list_box.get(ANCHOR))


submit_btn.config(command=on_submit)
get_list_btn.config(command=on_get_list)
# submit_btn.config(
#     cnf={"command": lambda: messagebox.showinfo("Info", "Info leyan finfo")},
# )

window.mainloop()
