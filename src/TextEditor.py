from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os


class TextEditor:
    """
    Создаются статусные строки и меню, объявляются методы для обработки операций работы с файлами.
    Далее реализуются операции, внесенные в меню:
    settitle(self)
    newfile(self, *args)
    openfile(self, *args)
    savefile(self, *args)
    saveasfile(self, *args)
    exit(self, *args)
    cut(self, *args)
    copy(self, *args)
    pust(self, *args)
    undo(self, *args)
    Также функция добавление хоткеев для операций. 
    """
    def __init__(self, root):
        self.root = root
        self.filename = "Новый текстовый документ"
        self.title = StringVar()
        self.status = StringVar()
        # Titlebar
        self.titlebar = Label(self.root, textvariable=self.title, font=("times new roman", 15, "bold", "italic"),
                              relief=RIDGE)
        self.titlebar.pack(side=TOP, fill=BOTH)
        self.settitle()
        # Statusbar
        self.statusbar = Label(self.root, textvariable=self.status, font=("times new roman", 15, "bold", "italic"),
                               relief=RIDGE)
        self.statusbar.pack(side=TOP, fill=BOTH)
        # Menubar
        self.menubar = Menu(self.root, font=("times new roman", 15), activebackground="skyblue",
                            activeforeground="white")
        self.root.config(menu=self.menubar)
        self.root.option_add("*tearOff", FALSE)
        # FileSection
        self.filemenu = Menu(self.menubar, font=("times new roman", 11), activebackground="skyblue",
                             activeforeground="white")
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", accelerator="Ctrl+N", command=self.newfile)
        self.filemenu.add_command(label="Open", accelerator="Ctrl+O", command=self.openfile)
        self.filemenu.add_command(label="Save", accelerator="Ctrl+S", command=self.savefile)
        self.filemenu.add_command(label="Save As", accelerator="Ctrl+A", command=self.saveasfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", accelerator="Ctrl+E", command=self.exit)
        # EditSection
        self.editmenu = Menu(self.menubar, font=("times new roman", 11), activebackground="skyblue",
                             activeforeground="white")
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut)
        self.editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy)
        self.editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste)
        self.editmenu.add_command(label="Undo", accelerator="Ctrl+U", command=self.undo)
        # Scrollbar and Text
        scrol_y = Scrollbar(self.root, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)
        self.txtarea = Text(self.root, yscrollcommand=scrol_y.set, font=("times new roman", 15), state="normal")
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        # ShortcutsFunction
        self.hotkeyforsshortcuts()

    def settitle(self):
        if self.filename != "Новый текстовый документ":
            self.title.set(f"{os.path.basename(self.filename)} - {self.filename}")
        else:
            self.title.set(self.filename)

    def newfile(self, *args):
        self.txtarea.delete("1.0", END)
        self.filename = "Новый текстовый документ"
        self.settitle()
        self.status.set("New File Created")

    def openfile(self, *args):
        try:
            self.filename = filedialog.askopenfilename(title="Select file",
                                                       filetypes=[["All Files", "*.*"], ["Text Files", "*.txt"],
                                                                  ["Python Files", "*.py"]])
            if self.filename:
                infile = open(self.filename, "r")
                self.txtarea.delete("1.0", END)
                for line in infile:
                    self.txtarea.insert(END, line)
                infile.close()
                self.settitle()
                self.status.set(f"{os.path.basename(self.filename)} - Opened Successfully")
        except Exception as e:
            messagebox.showerror("Error", e)

    def savefile(self, *args):
        try:
            if self.filename:
                data = self.txtarea.get("1.0", END)
                outfile = open(self.filename, "w")
                outfile.write(data)
                outfile.close()
                self.settitle()
                self.status.set(f"{os.path.basename(self.filename)} - Saved Successfully")
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror("Error", e)

    def saveasfile(self, *args):
        try:
            untitledfile = filedialog.asksaveasfilename(title="Save file As", defaultextension=".txt",
                                                        initialfile="Untitled.txt", filetypes=(
                    ("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")))
            data = self.txtarea.get("1.0", END)
            outfile = open(untitledfile, "w")
            outfile.write(data)
            outfile.close()
            self.filename = untitledfile
            self.settitle()
            self.status.set(f"{os.path.basename(self.filename)} - Saved Successfully")
        except Exception as e:
            messagebox.showerror("Error", e)

    def exit(self, *args):
        if messagebox.askyesno("Warning", "Your changes are not saved. Get out anyway?") > 0:
            self.root.destroy()

    def cut(self, *args):
        self.txtarea.event_generate("<<Cut>>")

    def copy(self, *args):
        self.txtarea.event_generate("<<Copy>>")

    def paste(self, *args):
        self.txtarea.event_generate("<<Paste>>")

    def undo(self, *args):
        try:
            if self.filename:
                self.txtarea.delete("1.0", END)
                infile = open(self.filename, "r")
                for line in infile:
                    self.txtarea.insert(END, line)
                infile.close()
                self.settitle()
                self.status.set("Undone Successfully")
            else:
                self.txtarea.delete("1.0", END)
                self.filename = None
                self.settitle()
                self.status.set("Undone Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)

    def hotkeyforsshortcuts(self):
        self.txtarea.bind("<Control-n>", self.newfile)
        self.txtarea.bind("<Control-o>", self.openfile)
        self.txtarea.bind("<Control-s>", self.savefile)
        self.txtarea.bind("<Control-a>", self.saveasfile)
        self.txtarea.bind("<Control-e>", self.exit)
        self.txtarea.bind("<Control-x>", self.cut)
        self.txtarea.bind("<Control-c>", self.copy)
        self.txtarea.bind("<Control-v>", self.paste)
        self.txtarea.bind("<Control-u>", self.undo)
