###############################
# A script containing the completed tasks interface
###############################
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil


class Win:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Completed Tasks")
        self.root.geometry("300x400")

        self.comps = tk.Listbox(master=self.root, width=45, height=20)
        log = open(os.getcwd() + "\\complist.txt")
        for line in log:
            self.comps.insert(tk.END, line)
        log.close()
        self.comps.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        exportbutt = tk.Button(master=self.root, text="Export", command=self.export)
        exportbutt.grid(row=1, column=0, padx=10, pady=10)
        deltxtbutt = tk.Button(master=self.root, text="Delete", command=self.dellist)
        deltxtbutt.grid(row=1, column=1, padx=10, pady=10)

        self.root.mainloop()

    def dellist(self):
        warning = tk.messagebox.askyesno("Wait!", "Are you sure you want to delete the tasks you've checked off? This cannot be undone.")
        if not warning:
            return None
        else:
            log = open(os.getcwd() + "\\complist.txt", "w")
            log.close()
            self.comps.delete(0, tk.END)

    def export(self):
        dialog = tk.filedialog.asksaveasfilename(title="Save as..", initialdir=os.getcwd(), filetypes=(("text file", "*.txt"), ("all files", "*")))
        shutil.copy(os.getcwd() + "\\complist.txt", dialog)


