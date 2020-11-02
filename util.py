class Directions:
    def __init__(self, priorityList):
        self.directions = {}
        self.invertedDirections = {}
        for index, value in enumerate(priorityList):
            self.directions[value] = index + 1
            self.invertedDirections[index + 1] = value

    def getDirections(self):
        return (self.directions, self.invertedDirections)
