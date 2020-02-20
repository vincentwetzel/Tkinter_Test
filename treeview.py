import tkinter as tk
import tkinter.ttk

root_tk = tk.Tk()
root_tk.columnconfigure(0, weight=1)
root_tk.rowconfigure(0, weight=1)
main_frame = tk.Frame(root_tk, bg="#FF0000", )
main_frame.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

tree = tk.ttk.Treeview(main_frame)

# Configure scrolling
treescroll = tk.ttk.Scrollbar(main_frame)
treescroll.configure(command=tree.yview)
tree.configure(yscrollcommand=treescroll.set)

# Define columns
tree["columns"] = ("one", "two", "three")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.column("one", width=150, minwidth=150, stretch=tk.NO)
tree.column("two", width=400, minwidth=200)
tree.column("three", width=80, minwidth=50, stretch=tk.NO)

# Define headings
tree.heading("#0", text="Name", anchor=tk.W)
tree.heading("one", text="Date modified", anchor=tk.W)
tree.heading("two", text="Type", anchor=tk.W)
tree.heading("three", text="Size", anchor=tk.W)

# Add some rows
# Level 1
folder1 = tree.insert("", 1, iid=None, text="Folder 1", values=("23-Jun-17 11:05", "File folder", ""))
tree.insert("", 2, iid=None, text="text_file.txt", values=("23-Jun-17 11:25", "TXT file", "1 KB"))
# Level 2
tree.insert(folder1, "end", iid=None, text="photo1.png", values=("23-Jun-17 11:28", "PNG file", "2.6 KB"))
tree.insert(folder1, "end", iid=None, text="photo2.png", values=("23-Jun-17 11:29", "PNG file", "3.2 KB"))
tree.insert(folder1, "end", iid=None, text="photo3.png", values=("23-Jun-17 11:30", "PNG file", "3.1 KB"))

# Pack
tree.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
treescroll.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E))

root_tk.mainloop()
