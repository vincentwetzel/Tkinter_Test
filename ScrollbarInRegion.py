import tkinter as tk


def populate(frame_param):
    """Put in some fake data"""
    for row in range(100):
        tk.Label(frame_param, text="%s" % row, width=3, borderwidth="1",
                 relief="solid").grid(row=row, column=0)
        t = "this is the second column for row %s" % row
        tk.Label(frame_param, text=t).grid(row=row, column=1)


def on_frame_configure(canvas_param):
    """Reset the scroll region to encompass the inner frame"""
    canvas_param.configure(scrollregion=canvas_param.bbox("all"))


root = tk.Tk()
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4, 4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))

populate(frame)

root.mainloop()
