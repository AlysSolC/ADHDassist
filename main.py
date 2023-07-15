################################################
# Container for main window
################################################
import os
from tkinter import *
from tkinter import simpledialog
import datahandler as dh
import task_class2
import compinterface
import miscwins as mw


class Win:

    def __init__(self):
        # Build window basics
        self.root = Tk()
        self.root.geometry("750x500")
        self.root.resizable(height=False, width=False)
        self.root.title("ADHDassist v1.0.0")

        # window pieces
        self.left()
        self.instance = None
        self.root.mainloop()

    def left(self):
        """
        Sets up a static left panel.
        """
        # Creating the frame itself
        self.leftframe = LabelFrame(master=self.root, text="To do:", bg="lightgray")
        self.leftframe.grid(column=0, row=0, padx=10, pady=10)

        self.tasklistsetup()

        # Sets of buttons
        self.compbutton = Button(master=self.leftframe, text="Completed",command=compinterface.Win, width=12).grid(row=1, column=0, pady=10)
        self.checkbutton = Button(master=self.leftframe, text="Complete Task",command=lambda: self.delcmd("comp") ,width=12).grid(row=1, column=1, pady=10)
        self.addbutton = Button(master=self.leftframe, text="Add Task", command=self.addcmd, width=12).grid(row=2, column=0, pady=10)
        self.delbutton = Button(master=self.leftframe, text="Delete Task", command=lambda: self.delcmd("del"), width=12).grid(row=2, column=1, pady=10)
        self.helpbutton = Button(master=self.leftframe, text="Help", command=mw.Help,width=12).grid(row=3, column=0, pady=10)
        self.abtbutton = Button(master=self.leftframe, text="About", command=mw.About,width=12).grid(row=3, column=1, pady=10)

    def tasklistsetup(self):
        """
        Creates a listbox, then inputs all existing task files into the listbox
        """
        self.taskselect = Listbox(master=self.leftframe, height=20, width=40)  # Creates the listbox itself
        self.taskselect.grid(row=0, column=0, columnspan=2)

        listcount = 0  # translates files from task directory into class and adds the main task from each class instance
        taskdir = os.getcwd() + "\\tasks\\"  # to the listbox.
        for file in os.listdir(taskdir):
            item = dh.file2class(taskdir + file)
            listcount = listcount + 1
            self.taskselect.insert(listcount, item.maintask)

        # gettasks = self.taskselect.get(0, END)  # Potential rainmeter interface in a future update?

        self.taskselect.bind("<<ListboxSelect>>", self.right)

    def right(self, event):
        """
        Sets up a dynamic right panel based off of task item selected in taskselect
        """
        task = self.taskselect.get(self.taskselect.curselection())
        self.rightframe = LabelFrame(master=self.root, text=task)
        self.rightframe.grid(column=1, row=0, padx=10, pady=10)
        self.instance = task_class2.activeinstances[task]

        # Changeable deadline
        dltext = StringVar(value=self.instance.deadline)
        deadlineframe = LabelFrame(master=self.rightframe, text="Deadline: ", labelanchor="w")
        deadlineframe.grid(row=0, column=0, padx=10, pady=10)
        deadlinetextbox = Entry(master=deadlineframe, textvariable=dltext)
        deadlinetextbox.grid(row=0, column=0)

        # Changeable prereqs
        prqframe = LabelFrame(master=self.rightframe, text="Prerequsites:")
        prqframe.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        prqtextbox = Text(master=prqframe, height=6, width=20)
        prqtextbox.insert(index=END,chars="\n".join(self.instance.prereqs))
        prqtextbox.grid(row=0, column=0)

        # Changeable subtasks
        subtframe = LabelFrame(master=self.rightframe, text="Subtasks:")
        subtframe.grid(row=1, column=1, padx=10, pady=10)
        subttextbox = Text(master=subtframe, height=6, width=20, yscrollcommand="yes")
        subttextbox.insert(index=END, chars="\n".join(self.instance.subtasks))
        subttextbox.grid(row=0, column=0)

        # Changeable notes
        noteframe = LabelFrame(master=self.rightframe, text="Notes:")
        noteframe.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        notetextbox = Text(master=noteframe, height=6, width=30)
        notetextbox.insert(index=END, chars=self.instance.notes)
        notetextbox.grid(row=0, column=0)

        # Button to change shit
        editbutton = Button(master=self.rightframe, text="Save Changes", command=lambda: dh.edittask(self.instance, dltext.get(), prqtextbox.get("1.0",END), subttextbox.get("1.0",END), notetextbox.get("1.0",END)))
        editbutton.grid(row=2, column=1)

    def delcmd(self, delorcomp):
        """
        Deletes the selected instance
        :param delorcomp: saves task if == comp
        :return:
        """
        self.taskselect.delete(self.taskselect.curselection())
        if delorcomp == "del":
            dh.deltask(self.instance)
        elif delorcomp == "comp":
            dh.comptask(self.instance)
        self.rightframe.destroy()

    def addcmd(self):
        """
        Uses a series of dialogues to collect task data and creates a task instance out of it.
        :return: None
        """
        asktitle = simpledialog.askstring(title="Add Task", prompt="Name your task!", parent=self.root)
        while asktitle == "" or isinstance(asktitle, str) is False:  # Makes sure the task has a valid name
            asktitle = simpledialog.askstring(title="Add Task", prompt="Sorry dude, you gotta give it a name. Enter one below!", parent=self.root)
        askdeadline = simpledialog.askstring(title="Add Task", prompt="Okay, when does it need to be done by?", parent=self.root)
        askprqs = simpledialog.askstring(title="Add Task", prompt="Cool! Now, name a few things you need to get or do before you start on this. Separate your items by commas!", parent=self.root)
        asksubs = simpledialog.askstring(title="Add Task", prompt="Now lets break up your task into subtasks. List some subtasks of your main task! Again, separate your answers please", parent=self.root)
        asknotes = simpledialog.askstring(title="Add Task", prompt="Almost done! Finally, are there any other things you feel you should write down about this task?", parent=self.root)

        dh.createtask(title=asktitle, deadline=askdeadline, prereqs=askprqs, subtasks=asksubs, notes=asknotes, newtask=True)
        self.tasklistsetup()


gui = Win()
