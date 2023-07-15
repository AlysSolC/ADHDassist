#########################################################
# A container for the Help window and About window
# Built by Alys Combs
#########################################################
import tkinter as tk
import webbrowser as web
from tkinter import messagebox


#################################################################


class About:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("About")
        self.root.resizable(height=False, width=False)

        self.verstext = "Version 1.0.0"
        self.abouttext = "This is ADHDassist, a program made by undergrad student\nAlys Combs. I built this program" \
                         "because I struggle with managing\nmany of the responsibilities that hit me in daily life. This" \
                         " program\n combats overwhelming and executive dysfunction by urging users\nto analyze their" \
                         "'to-dos' into much more manageable bite-sized\nchunks. I built this program using what would help" \
                         " me personally\ncomplete my goals as a guide, but I'd love for this program\nto become a useful" \
                         "tool for everyone else who struggles with ADHD\nor just staying on top of things. If you have" \
                         " any suggestions\nfor how to improve this program, I encourage you to contact me!"

        self.interface()
        self.root.mainloop()

    def interface(self):
        vers = tk.Label(master=self.root, text=self.verstext).grid(row=0, column=0, padx=10, pady=10)
        changebutt = tk.Button(master=self.root, text="Changelog", command=self.changelog).grid(row=0, column=1, padx=10, pady=10)
        about = tk.Label(master=self.root, text=self.abouttext).grid(row=1, column=0, padx=10, columnspan=2)
        contactbutt = tk.Button(master=self.root, text="Contact me!", command=self.contact).grid(row=2, column=0, padx=10, pady=10)
        portfolbutt = tk.Button(master=self.root, text="See my other work!", command=lambda:web.open("https://github.com/AlysSolC")).grid(row=2, column=1, padx=10, pady=10)

    def changelog(self):
        """
        To be altered with each new update, giving a record of what has changed since the beginning of this program
        """
        c = tk.messagebox.showinfo(title="Changelog", message="Woah, looks like you're on the earliest version, you early adopter!")

    def contact(self):
        c = tk.messagebox.showinfo(title="Contact me!", message="Email:\tacombs.ohva@gmail.com\nGithub:\thttps://github.com/AlysSolC\n")

###############################################################################


class Help:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Help")
        self.root.resizable(height=False, width=False)

        self.interface()
        self.root.mainloop()

    def interface(self):
        # FAQ data
        q1 = "How do I use this application?"
        a1 = "This program works as a to-do list. Using the interface\n" \
             "on the left, you can write out a task that you need to\n," \
             "do, and add in any information connected to that task"
        q2 = "Can I edit my tasks?"
        a2 = "Yes! To edit a task, click on it from the left to edit\n" \
             "its data. You must click the 'Save Changes' button after\n" \
             "you finish editing in order for your changes to be\n" \
             "applied. You cannot edit task titles at this time."
        q3 = "How do I check off a task?"
        a3 = "In order to check off a task, click the 'Complete Task'\n" \
             "button. You will not be able to 'uncheck' a task."
        q4 = "How do I check off a prerequisite/subtask?"
        a4 = "There is currently no function to check off a task at\n" \
             "this time. Instead, you must manually edit the task to\n" \
             "clear the prerequisite/subtask from the main task."
        q5 = "How do I see what tasks I've completed so far?"
        a5 = "In order to see what tasks you've completed so far,\n" \
             "click the 'Completed Tasks' button on the left. This\n" \
             "will show you a list of all the tasks you have done so\n" \
             "far. Prerequisites and subtasks manually checked off do\n" \
             "not show up at this time. You have the option of\n" \
             "exporting your completed tasks to a .txt file if you\n" \
             "want, or you can clear off the list and start from\n" \
             "scratch. Warning: you cannot retrieve a completed task\n" \
             "list after you have cleared it."
        qnalist = [q1, a1, q2, a2, q3, a3, q4, a4, q5, a5]

        # Main parent
        titletext = tk.Label(master=self.root, text="Frequently Asked Questions").grid(row=0, column=0)
        frame = tk.Frame(master=self.root, highlightbackground="gray", highlightthickness=1)
        self.qna(frame, qnalist)
        frame.grid(row=1, column=0, padx=5, pady=5)
        helptext = tk.Label(master=self.root, text="None of this helpful? Feel free to contact me!\n(See the 'About' section)").grid(row=2, column=0)

    def qna(self, frame, list_of_elements):
        """
        Positions question and answers in a frame. Assumes questions are on the left and their respective answers on the
        right.
        :param frame: tk.Frame
        :param list_of_elements: list
        :return: None
        """
        count = 0
        for item in list_of_elements:
            if list_of_elements.index(item) % 2 == 1:  # if in answer position:
                tk.Label(master=frame, text=item).grid(row=count, column=1)
            else:
                tk.Label(master=frame, text=item).grid(row=count, column=0)
            count = count + 1
