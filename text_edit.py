from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import font
from fpdf import FPDF

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

def make_bold():

    bold_italic_font=font.Font(text, text.cget("font"))
    bold_italic_font.configure(weight="bold",slant="italic")
    text.tag_configure("bold_italic", font=bold_italic_font)

    bold_underline_font=font.Font(text, text.cget("font"))
    bold_underline_font.configure(weight="bold",underline=1)
    text.tag_configure("bold_underline", font=bold_underline_font)

    italic_underline_font=font.Font(text, text.cget("font"))
    italic_underline_font.configure(slant="italic",underline=1)
    text.tag_configure("italic_underline", font=italic_underline_font)

    bold_italic_underline_font=font.Font(text, text.cget("font"))
    bold_italic_underline_font.configure(weight="bold",slant="italic", underline=1)
    text.tag_configure("bold_italic_underline", font=bold_italic_underline_font)

    bold_font = font.Font(text, text.cget("font"))
    bold_font.configure(weight="bold")

    text.tag_configure("bold", font=bold_font)
    current_tags = text.tag_names("sel.first")
    if "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
    elif "italic" in current_tags:
            # If the text is also italic, remove "italic and add the "bold_italic" tag
        text.tag_remove("italic", "sel.first", "sel.last")
        text.tag_add("bold_italic", "sel.first", "sel.last")
    elif "underline" in current_tags:
            # If the text is also underline, remove "underline" and add the "bold_underline" tag
        text.tag_remove("underline", "sel.first", "sel.last")
        text.tag_add("bold_underline", "sel.first", "sel.last")
    elif "italic_underline" in current_tags:
            # If the text is also italic_underline, remove "italic_underline" add the "bold_italic_underline" tag
        text.tag_remove("italic_underline", "sel.first", "sel.last")
        text.tag_add("bold_italic_underline", "sel.first", "sel.last")
    elif "bold_italic" in current_tags:
            # If the text is also bold_italc, remove "bold_italic" and add the "italic" tag
        text.tag_remove("bold_italic", "sel.first", "sel.last")
        text.tag_add("italic", "sel.first", "sel.last")
    elif "bold_underline" in current_tags:
            # If the text is also bold_underline, remove "bold_underline" and add the "underline" tag
        text.tag_remove("bold_underline", "sel.first", "sel.last")
        text.tag_add("underline", "sel.first", "sel.last")
    elif "bold_italic_underline" in current_tags:
            # If the text is also bold_italic_underline, remove "bold_italic_underline" and add the italic_underline" tag
        text.tag_remove("bold_italic_underline", "sel.first", "sel.last")
        text.tag_add("italic_underline", "sel.first", "sel.last")
    else:
        text.tag_add("bold", "sel.first", "sel.last")
def make_italic():

    bold_italic_font=font.Font(text, text.cget("font"))
    bold_italic_font.configure(weight="bold",slant="italic")
    text.tag_configure("bold_italic", font=bold_italic_font)

    bold_underline_font=font.Font(text, text.cget("font"))
    bold_underline_font.configure(weight="bold",underline=1)
    text.tag_configure("bold_underline", font=bold_underline_font)

    italic_underline_font=font.Font(text, text.cget("font"))
    italic_underline_font.configure(slant="italic",underline=1)
    text.tag_configure("italic_underline", font=italic_underline_font)

    bold_italic_underline_font=font.Font(text, text.cget("font"))
    bold_italic_underline_font.configure(weight="bold",slant="italic", underline=1)
    text.tag_configure("bold_italic_underline", font=bold_italic_underline_font)

    italic_font = font.Font(text, text.cget("font"))
    italic_font.configure(slant="italic")

    text.tag_configure("italic", font=italic_font)
    current_tags = text.tag_names("sel.first")
    if "italic" in current_tags:
        text.tag_remove("italic", "sel.first", "sel.last")
    elif "bold" in current_tags:
            # If the text is also bold, remove "bold" and add the "bold_italic" tag
        text.tag_remove("bold", "sel.first", "sel.last")
        text.tag_add("bold_italic", "sel.first", "sel.last")    
    elif "underline" in current_tags:
            # If the text is also underline, remove "underline" and add the "italic_underline" tag
        text.tag_remove("underline", "sel.first", "sel.last")
        text.tag_add("italic_underline", "sel.first", "sel.last")   
    elif "bold_italic" in current_tags:
            # If the text is also bold_italic, remove "bold_italic" and add the "bold" tag
        text.tag_remove("bold_italic", "sel.first", "sel.last")
        text.tag_add("bold", "sel.first", "sel.last")
    elif "italic_underline" in current_tags:
            # If the text is also italic_underline, remove "italic_underline" and add the "underline" tag
        text.tag_remove("italic_underline", "sel.first", "sel.last")
        text.tag_add("underline", "sel.first", "sel.last")
    elif "bold_underline" in current_tags:
            # If the text is also bold_underline, remove "bold_underline" and add the "bold_italic_underline" tag
        text.tag_remove("bold_underline", "sel.first", "sel.last")
        text.tag_add("bold_italic_underline", "sel.first", "sel.last")
    elif "bold_italic_underline" in current_tags:
            # If the text is also bold_italic_underline, remove "bold_italic_underline" add the "bold_underline" tag
        text.tag_remove("bold_italic_underline", "sel.first", "sel.last")
        text.tag_add("bold_underline", "sel.first", "sel.last")
    else:
        # If the text is not italic, add the "italic" tag
        text.tag_add("italic", "sel.first", "sel.last")

def make_underline():

    bold_italic_font=font.Font(text, text.cget("font"))
    bold_italic_font.configure(weight="bold",slant="italic")
    text.tag_configure("bold_italic", font=bold_italic_font)

    bold_underline_font=font.Font(text, text.cget("font"))
    bold_underline_font.configure(weight="bold",underline=1)
    text.tag_configure("bold_underline", font=bold_underline_font)

    italic_underline_font=font.Font(text, text.cget("font"))
    italic_underline_font.configure(slant="italic",underline=1)
    text.tag_configure("italic_underline", font=italic_underline_font)

    bold_italic_underline_font=font.Font(text, text.cget("font"))
    bold_italic_underline_font.configure(weight="bold",slant="italic", underline=1)
    text.tag_configure("bold_italic_underline", font=bold_italic_underline_font)

    underline_font = font.Font(text, text.cget("font"))
    underline_font.configure(underline=1)

    text.tag_configure("underline", font=underline_font)
    current_tags = text.tag_names("sel.first")
    if "underline" in current_tags:
        # If the text is already underline, remove the "underline" tag
        text.tag_remove("underline", "sel.first", "sel.last")  
    elif "bold" in current_tags:
            # If the text is also bold, remove "bold" and add the "bold_underline" tag
        text.tag_remove("bold", "sel.first", "sel.last")
        text.tag_add("bold_underline", "sel.first", "sel.last")
    elif "italic" in current_tags:
            # If the text is also italic, remove "italic" and add the "italic_underline" tag
        text.tag_remove("italic", "sel.first", "sel.last")
        text.tag_add("italic_underline", "sel.first", "sel.last")
    elif "bold_italic" in current_tags:
           # If the text is also bold_italic, remove "bold_italic" and add the "bold_italic_underline" tag
        text.tag_remove("bold_italic", "sel.first", "sel.last")
        text.tag_add("bold_italic_underline", "sel.first", "sel.last")
    elif "bold_underline" in current_tags:
             # If the text is also bold_underline, remove "bold_underline" and add the "bold" tag
        text.tag_remove("bold_underline", "sel.first", "sel.last")
        text.tag_add("bold", "sel.first", "sel.last")
    elif "italic_underline" in current_tags:
            # If the text is also italic_underline, remove "italic_underline" and add the "italic" tag
        text.tag_remove("italic_underline", "sel.first", "sel.last")
        text.tag_add("italic", "sel.first", "sel.last")
    elif "bold_italic_underline" in current_tags:
            # If the text is also bold_italic_underline, remove "bold_italic_underline" and add the "bold_italic" tag
        text.tag_remove("bold_italic_underline", "sel.first", "sel.last")
        text.tag_add("bold_italic", "sel.first", "sel.last")
    else:
        # If the text is not underline, add the "underline" tag
        text.tag_add("underline", "sel.first", "sel.last")

#Function for choosing font
def font_chooser(f):
    my_font.config(family=f)

#Function for choosing size
def size_chooser(s):
    my_font.config(size = s)

#Export to pdf
def prt_to_pdf():
    with open("temp.txt", "w") as f:
        text_content = text.get(1.0, END)
        f.write(text_content)

    pdf = FPDF()  
    # Add a page
    pdf.add_page()  
    pdf.set_font(my_font.actual("family"), size = my_font.actual("size"))
    
    f = open("temp.txt", "r")
    for x in f:
        pdf.cell(200, 5, txt = x, ln = 1, align = 'L')
    pdf.output("my_pdf.pdf")  




# Add the File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Print to PDF", command=prt_to_pdf)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add the Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_command(label="Redo", command=text.edit_redo)

#Add Bold menu
bold_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Bold", command=make_bold)

#Add Itallic menu
italic_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Italic", command=make_italic)

#Add Underline menu
underline_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Underline", command=make_underline)

#Add Font menu
font_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Arial", command=lambda:font_chooser('Arial'))
font_menu.add_command(label="Times New Roman", command=lambda:font_chooser('Times New Roman'))
font_menu.add_command(label="Courier New", command=lambda:font_chooser('Courier New'))
font_menu.add_command(label="Calibri", command=lambda:font_chooser('Calibri'))

#Add Size menu
size_menu=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Size", menu=size_menu)
size_menu.add_command(label="8", command=lambda:size_chooser(8))
size_menu.add_command(label="10", command=lambda:size_chooser(10))
size_menu.add_command(label="12", command=lambda:size_chooser(12))
size_menu.add_command(label="14", command=lambda:size_chooser(14))
size_menu.add_command(label="16", command=lambda:size_chooser(16))
size_menu.add_command(label="24", command=lambda:size_chooser(24))
size_menu.add_command(label="32", command=lambda:size_chooser(32))

# Run the GUI
root.mainloop()

