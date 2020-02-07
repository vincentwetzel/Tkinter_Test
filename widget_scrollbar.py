import tkinter  # python 3


# import Tkinter as tk  # python 2

def populate(frame_param: tkinter.Frame) -> None:
    # Put in some fake data
    for row in range(10):
        tkinter.Label(frame_param, text=str(row), width=3, borderwidth=1,
                      relief="solid").grid(row=row, column=0)
        t = "this is the second column for row %s" % row
        tkinter.Label(frame_param, text=t).grid(row=row, column=1)


def on_frame_configure(canvas: tkinter.Canvas) -> None:
    """
    Resets the scrollbar region to encompass the inner frame
    :param canvas:
    """
    # Note: bbox is a bounding box
    canvas.configure(scrollregion=canvas.bbox("all"))


def on_mousewheel(event: tkinter.Event) -> None:
    # TODO: Make it so this ONLY works if there are widgets filling the whole screen and I need to enable scrolling.
    canvas_1.yview_scroll(int(-1 * (event.delta / 120)), "units")


root = tkinter.Tk()
canvas_1 = tkinter.Canvas(root, borderwidth=0, background="#ffffff")
canvas_1.bind_all("<MouseWheel>", on_mousewheel)
frame = tkinter.Frame(canvas_1, background="#ffffff")
vertical_scrollbar = tkinter.Scrollbar(root, orient="vertical", command=canvas_1.yview)
canvas_1.configure(yscrollcommand=vertical_scrollbar.set)

vertical_scrollbar.pack(side="right", fill="y")
canvas_1.pack(side="left", fill="both", expand=True)
canvas_1.create_window((4, 4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas_1: on_frame_configure(canvas))

populate(frame)

root.mainloop()
