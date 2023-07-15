######################################
# New version of the task class
# built by Alys Combs
######################################

activeinstances = {}  # Keeps track of all tasks; key is maintask, value is object


class Task:

    def __init__(self, title, file, deadline='', prereqlist=[], subtasklist=[], notes=''):
        """
        An instance of the Task class, a to-do list item with a bunch of attached data.
        :param title: Name of main task
        :param file: Filepath where the task's reference file is located
        :param deadline: A string representing a deadline
        :param prereqlist: A list of prerequisites to the main task
        :param subtasklist: A list of subtasks that make up the main task
        :param notes: Optional user-made notes for the task
        """
        self.maintask = title
        self.filepath = file
        self.deadline = deadline
        self.prereqs = prereqlist
        self.subtasks = subtasklist
        self.notes = notes
        activeinstances[self.maintask] = self

    def __str__(self):
        return "maintask = {0}\nfilepath = {1}\ndeadline = {2}\nprereqlist = {3}\nsubtasklist = {4}\nnotes = {5}".format(self.maintask,self.filepath,self.deadline,self.prereqs,self.subtasks,self.notes)

