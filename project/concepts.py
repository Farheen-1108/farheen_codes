'''   
python GUL-- TKINTER:
single user
gul(graphical user interface)
import module
create the main window (like size font format)
add any number widgets to the main window
pack is used to organize the widgets 
main loop and main window

button :
w = Buttom(master.option=value)  (master = parent windoe(tk))
active background,command,activeforehead,bg,font,width,height

'''

import tkinter as tk
r = tk.Tk()

r.title("Vignan Bio tech")
button = tk.Button(r, text="Bio tech", width = 50 , command=r.destroy)
button.pack()

button = tk.Button(r, text="year", width = 50 , command=r.destroy)
button.pack()

button = tk.Button(r, text="section", width = 50 , command=r.destroy)
button.pack()

button = tk.Button(r, text="enter", width = 50 , command=r.destroy)
button.pack()

r.mainloop()