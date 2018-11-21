from constants import *


class Task(object):
    """Description of any task"""
    def __init__(self, name, linkToTask, linkToSolution, category, tags):
        self.name = name
        self.linkToTask = linkToTask
        self.linkToSolution = linkToSolution
        self.category = category
        self.tags = sorted(tags)

    @property
    def Name(self):
        return self.name

    @property
    def Problem(self):
        return self.linkToTask

    @property
    def Solution(self):
        return self.linkToSolution

    @property
    def Category(self):
        return self.category


def TaskDictionary():
    return {str(i + 1) : Task(link, "", "", []) for i, link in enumerate(dict_of_tasks)}

