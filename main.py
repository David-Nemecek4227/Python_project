from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

# Define functions for file operations
def new_file():
    # Clear the text area
    text.delete(1.0, END)
    # Update the file name
    root.title("Untitled")

def save_file():
    # Open a dialog box to save the file
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    # Save the file
    with open(file_path, "w") as f:
        text_content = text.get(1.0, END)
        f.write(text_content)
    # Update the file name
    root.title(f"{file_path}")

def open_file():
    # Open a dialog box to choose the file to open
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    # Clear the text area
    text.delete(1.0, END)
    # Open the file and display its contents
    with open(file_path, "r") as f:
        text_content = f.read()
        text.insert(END, text_content)
    # Update the file name
    root.title(f"{file_path}")

# Create the GUI
root = Tk()
root.title("Untitled")

# Create the text area
text = Text(root, undo=True)
text.pack(expand=True, fill=BOTH)

# Create the menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add the File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add the Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_command(label="Redo", command=text.edit_redo)

# Run the GUI
root.mainloop()