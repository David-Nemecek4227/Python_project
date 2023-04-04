from functions import *


# Create the GUI
root = Tk()
root.title("Untitled")
root.geometry("540x500")

#Set default font
my_font=font.Font(family="Helvetica", size="10")

my_frame = Frame(root, width=510, height=500)
my_frame.pack(pady=10)
my_frame.grid_propagate(False)
my_frame.columnconfigure(0, weight=10)
# Create the text area
text = Text(my_frame,font=my_font, undo=True)
text.grid(row=0, column=0)
text.grid_rowconfigure(0,weight=1)
text.grid_columnconfigure(0,weight=1)
text.pack_propagate(False)

# Create the menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add the File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file(text, root))
file_menu.add_command(label="Open", command=open_file(text, root))
file_menu.add_command(label="Save", command=save_file(text, root))
file_menu.add_command(label="Print to PDF", command=prt_to_pdf(text, my_font))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add the Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_command(label="Redo", command=text.edit_redo)

#Add Bold menu
bold_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Bold", command=make_bold(text))

#Add Itallic menu
italic_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Italic", command=make_italic(text))

#Add Underline menu
underline_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Underline", command=make_underline(text))

#Add Font menu
font_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Arial", command=lambda:font_chooser('Arial', my_font))
font_menu.add_command(label="Times New Roman", command=lambda:font_chooser('Times New Roman', my_font))
font_menu.add_command(label="Courier New", command=lambda:font_chooser('Courier New', my_font))
font_menu.add_command(label="Calibri", command=lambda:font_chooser('Calibri', my_font))

#Add Size menu
size_menu=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Size", menu=size_menu)
size_menu.add_command(label="8", command=lambda:size_chooser(8, my_font))
size_menu.add_command(label="10", command=lambda:size_chooser(10, my_font))
size_menu.add_command(label="12", command=lambda:size_chooser(12, my_font))
size_menu.add_command(label="14", command=lambda:size_chooser(14, my_font))
size_menu.add_command(label="16", command=lambda:size_chooser(16, my_font))
size_menu.add_command(label="24", command=lambda:size_chooser(24, my_font))
size_menu.add_command(label="32", command=lambda:size_chooser(32, my_font))

