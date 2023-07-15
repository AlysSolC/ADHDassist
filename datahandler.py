###################################################################
# ADHD Assist data handler
# Built by Alys Combs
# Meant to read saved tasks and translate them from a txt file into
# a class.
###################################################################
# A guide on how to read these files:
#
# ^ -> title
# @ -> filepath
# $ -> deadline
# ! -> prerequisites
# * -> subtasks
# & -> notes
###################################################################
import os
import task_class2


def file2class(file):
    """
    Translates a properly formatted file into an instance of a Task.
    :param file: Formatted file
    :return: an instance of the task class constructed with the information in the file specified.
    Returns none if file does not pass format check.
    """
    contents = open(file, "r")
    filecheck = contents.readline()
    if filecheck != "taskfile\n":
        return None
    else:
        #  Applying default values where applicable
        # TODO: do this!
        taskdeadline = ""
        tasksubs = []
        taskprereqs = []
        tasknotes = ""

        #  Sorting txt lines into appropriate data based on line prefix
        for line in contents:
            datacheck = line[0:3]
            if datacheck == "^- ":
                tasktitle = line[3:-1]
            elif datacheck == "@- ":
                taskfile = line[3:-1]
            elif datacheck == "$- ":
                taskdeadline = line[3:-1]
            elif datacheck == "!- ":
                taskprereqs.append(line[3:-1])
            elif datacheck == "*- ":
                tasksubs.append(line[3:-1])
            elif datacheck == "&- ":
                tasknotes = line[3:]
        contents.close()

        #  putting assorted data into a class
        task = task_class2.Task(tasktitle, taskfile, taskdeadline, taskprereqs, tasksubs, tasknotes)
        return task


def createtask(title, deadline, prereqs, subtasks, notes="", newtask=False):
    """
    Elements pulled from the main window turned into a file then an instance of the task class.
    :param title: str
    :param deadline: str
    :param prereqs: str
    :param subtasks: str
    :param notes: str
    :param newtask: bool, specifies if task is created from add interface
    :return: task instance and corresponding file
    """
    filepath = os.getcwd() + "\\tasks\\" + title[0:11] + ".txt"
    file = open(filepath, "w")

    file.write("taskfile\n")
    file.write("^- " + title + "\n")
    file.write("@- " + filepath + "\n")
    file.write("$- " + deadline + "\n")
    if newtask:
        prereqlist = prereqs.split(",")
    else:
        prereqlist = prereqs.split("\n")
    for item in prereqlist:
        file.write("!- " + item + "\n")
    if newtask:
        subtasklist = subtasks.split(",")
    else:
        subtasklist = subtasks.split("\n")
    for item in subtasklist:
        file.write("*- " + item + "\n")
    file.write("&- " + notes)

    file.close()
    return file2class(filepath)  # After closing the file, puts it through the file2class function.
    # Returns the str value for the created task class


def edittask(maintask, deadline, prereqs, subtasks, notes):
    """
    Modifies instance values
    :param maintask: The task instance being manipulated
    :param deadline: str
    :param prereqs: str
    :param subtasks: str
    :param notes: str
    :return: Edited task instance
    """
    # Sets new values
    maintask.deadline = deadline
    maintask.prereqs = prereqs  # prereqs.split('\n')
    maintask.subtasks = subtasks  # subtasks.split('\n')
    maintask.notes = notes

    # Creates file for edited instance
    createtask(maintask.maintask, maintask.deadline, maintask.prereqs, maintask.subtasks, maintask.notes)


def deltask(instance):
    """
    Deletes an instance of a task & deletes its corresponding file
    :param instance: Task instance
    :return: None
    """
    if instance == None:
        return None
    else:
        os.remove(instance.filepath)
        del instance


def comptask(instance):
    """
    Records the name of the task instance, adds it onto the completed task log, then runs the delete function
    :param instance: Task instance
    :return: None
    """
    comptxt = open(os.getcwd() + "\\complist.txt", "a")
    comptxt.write(instance.maintask + "\n")
    comptxt.close()
    deltask(instance)
