import tkinter as tk
def show():
	label.config(text=f"Selected: {listbox.get(listbox.curselection())}")
root = tk.Tk()
root.title("Listbox Demo")
frame = tk.Frame(root)
frame.pack()
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=4)
for i in ["Apple", "Banana", "Orange", "Mango", "Grapes"]:
	listbox.insert("end", i)
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)
tk.Button(root, text="Show", command=show).pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()
