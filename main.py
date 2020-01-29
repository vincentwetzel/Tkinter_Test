from tkinter import *
from tkinter import ttk
import time


def calculate(*args):
    try:
        value = float(args[0].get())
        args[1].set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


def metric_changed(*args):
    print("metric toggled!")


def main():
    root_tk = Tk()  # constructor for TK object
    root_tk.title("Feet to Meters")

    # Initialize grid
    # main_frame is our content frame inside of the root window.
    main_frame = ttk.Frame(root_tk, padding="3 3 12 12")
    main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    root_tk.columnconfigure(0, weight=1)
    root_tk.rowconfigure(0, weight=1)

    # Demonstrate some mouseover and clicking events
    event_label = ttk.Label(main_frame, text="Hello!")
    event_label.grid(column=1, row=1, sticky=E)
    event_label.bind('<Enter>', lambda e: event_label.configure(text='Moved mouse inside'))
    event_label.bind('<Leave>', lambda e: event_label.configure(text='Moved mouse outside'))
    event_label.bind('<1>', lambda e: event_label.configure(text='Clicked left mouse button'))
    event_label.bind('<Double-1>', lambda e: event_label.configure(text='Double clicked'))
    event_label.bind('<B3-Motion>', lambda e: event_label.configure(text='right button drag to %d,%d' % (e.x, e.y)))

    # StringVar are used to hold data
    feet = StringVar()
    meters = StringVar()

    # An Entry box to allow the user to type
    feet_entry = ttk.Entry(main_frame, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W, E))

    # Grid of words and buttons on the GUI
    ttk.Label(main_frame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
    ttk.Button(main_frame, text="Calculate", command=lambda: calculate(feet, meters)).grid(column=3, row=3, sticky=W)
    ttk.Label(main_frame, text="feet").grid(column=3, row=1, sticky=W)
    ttk.Label(main_frame, text="is equivalent to").grid(column=1, row=2, sticky=E)
    ttk.Label(main_frame, text="meters").grid(column=3, row=2, sticky=W)

    # Demonstrate a check button
    measureSystem = StringVar()
    ttk.Checkbutton(main_frame, text='Use Metric',
                    command=metric_changed, variable=measureSystem,
                    onvalue='metric', offvalue='imperial').grid(column=1, row=4, sticky=W)

    # Demonstrate radio buttons
    phone = StringVar()
    home = ttk.Radiobutton(main_frame, text='Home', variable=phone, value='home').grid(column=1, row=5)
    office = ttk.Radiobutton(main_frame, text='Office', variable=phone, value='office').grid(column=2, row=5)
    cell = ttk.Radiobutton(main_frame, text='Mobile', variable=phone, value='cell').grid(column=3, row=5)

    # Demonstrate combo box
    countryvar = StringVar()  # can use get() and set() to access this variable
    country = ttk.Combobox(main_frame, textvariable=countryvar, values=['1', '2', '3']).grid(column=1, row=6)

    # Demonstrate listbox
    listbox_items = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                     "November", "December")
    listbox_stringvar = StringVar(value=listbox_items)
    months_listbox = Listbox(main_frame, height=12, listvariable=listbox_stringvar, selectmode="browse").grid(column=1,
                                                                                                              row=7)
    # Demonstrate Scrollbar
    listbox_items_2 = ("Adam", "Matthew", "David", "CJ", "Michael", "Buzz")
    listbox_stringvar_2 = StringVar(value=listbox_items_2)
    months_listbox_2 = Listbox(main_frame, height=4, listvariable=listbox_stringvar_2, selectmode="browse")
    months_listbox_2.grid(column=1, row=8)
    s = ttk.Scrollbar(main_frame, orient=VERTICAL, command=months_listbox_2.yview)
    s.grid(column=2, row=8)
    months_listbox_2.configure(yscrollcommand=s.set)

    # Demonstrate sizegrip
    ttk.Sizegrip(main_frame).grid(column=999, row=999, sticky=(S, E))

    # Pad all the children from one another
    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    # Start with the cursor in the text box
    feet_entry.focus()

    # Enter key will bind to the calculate button
    # NOTE: This is 'lambda x:' instead of 'lambda:' (see above) because 'command=' wanted a function call
    # whereas bind() wants a value (x)
    root_tk.bind('<Return>', lambda x: calculate(feet, meters))

    root_tk.mainloop()

def print_hello():
    for i in range(10):
        time.sleep(1)
        print(i)


if __name__ == "__main__":
    main()
