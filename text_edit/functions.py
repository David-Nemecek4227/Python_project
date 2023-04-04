from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import font
from fpdf import FPDF



# Define functions for file operations
def new_file(text, root):
    # Clear the text area
    text.delete(1.0, END)
    # Update the file name
    root.title("Untitled")

def save_file(text, root):
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

def open_file(text, root):
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

def make_bold(text):

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
def make_italic(text):
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
def make_underline(text):

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
def font_chooser(f, my_font):
    my_font.config(family=f)

#Function for choosing size
def size_chooser(s, my_font):
    my_font.config(size = s)

#Export to pdf
def prt_to_pdf(text, my_font):
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