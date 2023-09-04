import tkinter as tk

def add_checkbox():
    current_line = text_entry.index(tk.INSERT).split('.')[0]
    text = text_entry.get(f"{current_line}.0", f"{current_line}.end-1c")
    text_entry.delete(f"{current_line}.0", f"{current_line}.end-1c")
    text_entry.insert(f"{current_line}.0", "☐ ")
    text_entry.insert(f"{current_line + 1}.0", text + "\n")

def toggle_checkbox(event):
    index = text_entry.index(tk.CURRENT)
    char = text_entry.get(index, index + "+1c")
    
    if char == "☐":
        text_entry.delete(index)
        text_entry.insert(index, "☑")
    elif char == "☑":
        text_entry.delete(index)
        text_entry.insert(index, "☒")

root = tk.Tk()
root.title("To-Do list")
root.configure(bg="black")

text_entry = tk.Text(root, wrap=tk.WORD, bg="black", fg="white")
text_entry.pack(expand=True, fill=tk.BOTH)
text_entry.bind("<Return>", lambda event: add_checkbox())
text_entry.bind("<Button-1>", toggle_checkbox)

root.mainloop()
