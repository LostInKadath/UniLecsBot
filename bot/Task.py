class Task(object):
    """Description of any task"""
    def __init__(self, linkToTask, linkToSolution, category, tags):
        self.linkToTask = linkToTask
        self.linkToSolution = linkToSolution
        self.category = category
        self.tags = sorted(tags)

    @property
    def Problem(self):
        return self.linkToTask

    @property
    def Solution(self):
        return self.linkToSolution

    @property
    def Category(self):
        return self.category

