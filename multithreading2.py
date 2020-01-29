import os
import time
from datetime import datetime
import shutil
import threading
from tkinter import *
import tkinter.ttk as ttk

submit_thread = None


def submit():
    for i in range(5):
        print(i)
        time.sleep(1)  # put your stuff here


def start_submit_thread(event):
    global submit_thread
    submit_thread = threading.Thread(target=submit)
    submit_thread.daemon = True  # Closing the GUI now kills this thread
    submit_thread.start()
    root.after(20, check_submit_thread)


def check_submit_thread():
    if submit_thread.is_alive():
        root.after(20, check_submit_thread)
    else:
        print("Done!")


root = Tk()
frame = ttk.Frame(root)
frame.pack()
ttk.Button(frame, text="Check", command=lambda: start_submit_thread(None)).grid(column=0, row=1, sticky=E)
root.mainloop()
