from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Menu App')
window.minsize(width=400, height=300)

# 1
main_menu = Menu(window)

def open_file():
    import time
    print('Opening file...')
    time.sleep(0.8)

def close_window():
    # TODO: Create a pop-up messagebox that asks the user for confirming before quiting the app
    confirm = messagebox.askyesno('Quit App?', 'Are you sure you want to quit?')
    if confirm:
        window.quit()

def create_menu(menu_label: str, menu_widget: Menu, menu_master: Menu = main_menu):
    menu_master.add_cascade(label=menu_label, menu=menu_widget)

# 3
file_menu = Menu(main_menu, tearoff=0)
tools_menu = Menu(main_menu, tearoff=False)

# 4
file_menu.add_command(label='OpenX', command=open_file)
file_menu.add_command(label='Create', command=open_file)
file_menu.add_command(label='New', command=open_file)
file_menu.add_command(label='Exit', command=close_window)


open_menu = Menu(file_menu, tearoff=False)
open_menu.add_command(label='File')
open_menu.add_command(label='Folder')
open_menu.add_command(label='Window')

file_menu.add_cascade(label='Open', menu=open_menu)

view_menu = Menu(main_menu, tearoff=False)
view_menu.add_command(label='Command Pallette')
view_menu.add_command(label='Open View...')
view_menu.add_separator()

appearance_submenu = Menu(view_menu, tearoff=0)
appearance_submenu.add_command(label='Fullscreen')
appearance_submenu.add_command(label='Zen Mode')
appearance_submenu.add_command(label='Centered Layout')

view_menu.add_cascade(label='Appearance', menu=appearance_submenu)


# 5
# main_menu.add_cascade(label='File', menu=file_menu)
# main_menu.add_cascade(label='')

create_menu(menu_label='File', menu_widget=file_menu)
create_menu(menu_label='Tools', menu_widget=tools_menu)
main_menu.add_cascade(label='View', menu=view_menu)

# 2
window.config(menu=main_menu)
window.mainloop()