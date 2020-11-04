import numpy as np
from util import Directions, Point
from nextDestination import NextDestination


class DFS:
    OPEN = 0
    WALL = 1
    VISITED = 2
    SOUTH = "SOUTH"
    NORTH = "NORTH"
    WEST = "WEST"
    EAST = "EAST"
    visitedStack = []
    branchingStack = []
    # todo: the visited stack needs to be updated when the robot moves across a line
    # todo: add branching stack

    def __init__(self, board, stepPriority):
        self.board = board
        self.visitedMap = np.zeros(board.shape)
        # 2D num-py array
        # [[,]]
        # value of a cell --> OPEN, WALL, VISITED, UNVISITED, ROBOT POSITION

        self.stepPriority = stepPriority
        # ["EAST", "NORTH", "SOUTH", "WEST"]

    def getOpenDirections(self, currentPosition):
        currentRow = currentPosition[0]
        currentColumn = currentPosition[1]

        openDirections = []
        sortedOpenDirections = []

        # todo: the +/- 1 values should actually be the vision range of the robot.
        # todo: OR we should decide on the size of a "TILE"

        try:
            if (
                currentRow + 1 >= 0
                and self.board[currentRow + 1, currentColumn] == self.OPEN
                and self.visitedMap[currentRow + 1, currentColumn] != self.VISITED
            ):
                openDirections.append(self.SOUTH)
        except IndexError as err:
            pass

        try:
            if (
                currentRow - 1 >= 0
                and self.board[currentRow - 1, currentColumn] == self.OPEN
                and self.visitedMap[currentRow - 1, currentColumn] != self.VISITED
            ):
                openDirections.append(self.NORTH)
        except IndexError as err:
            pass

        try:
            if (
                currentColumn + 1 >= 0
                and self.board[currentRow, currentColumn + 1] == self.OPEN
                and self.visitedMap[currentRow, currentColumn + 1] != self.VISITED
            ):
                openDirections.append(self.EAST)
        except IndexError as err:
            pass

        try:
            if (
                currentColumn - 1 >= 0
                and self.board[currentRow, currentColumn - 1] == self.OPEN
                and self.visitedMap[currentRow, currentColumn - 1] != self.VISITED
            ):
                openDirections.append(self.WEST)
        except IndexError as err:
            pass

        for i in openDirections:
            sortedOpenDirections.append(self.stepPriority[0][i])

        sortedOpenDirections.sort()

        for i in range(len(sortedOpenDirections)):
            sortedOpenDirections[i] = self.stepPriority[1][sortedOpenDirections[i]]

        if len(sortedOpenDirections) > 1:
            self.branchingStack.append(
                # (currentRow, currentColumn, sortedOpenDirections)
                (currentRow, currentColumn)
            )

        return sortedOpenDirections

    # todo
    def getNextStep(self, currentPosition):

        self.visitedMap[currentPosition[0], currentPosition[1]] = self.VISITED
        openDirections = self.getOpenDirections(currentPosition)
        print("*************************************")
        print(openDirections)
        print("*************************************")

        for dxn in openDirections:
            newPoint = Point.addTuples(currentPosition, Directions.getCoordinate(dxn))
            # check if the newpoint is visted or not
            # if self.visitedMap[newPoint[0], newPoint[1]] != self.VISITED:
            print("Fount new point", newPoint)
            print(self.visitedMap)
            print("-------------------------------------------------")
            return newPoint
        else:
            # backtracking
            print("got back to branching point")
            if len(self.branchingStack) > 0:
                returnPoint = self.branchingStack.pop()
                print(returnPoint)
                return returnPoint
            else:
                print("no more moves")
                return -50

        # (x,y)

    # todo
    # return the farthest point in the needed direction
    # this point will be in the OPEN spots in the map
    # - or it can be a VISITED spot if an open slot is not found in the direct vicinity


def startExploration(droneStartingCoordinate):
    x = droneStartingCoordinate[0]
    y = droneStartingCoordinate[1]

    robotPositionState = NextDestination(
        bounds={"northBound": 20, "southBound": 20, "westBound": 10, "eastBound": 30}
    )
    dxnPriorities = robotPositionState.generateStepPriority()

    print(dxnPriorities)

    simpleMap = np.zeros((5, 5))

    dfs = DFS(simpleMap, dxnPriorities)

    nextPoint = (x, y)
    while nextPoint != -50:
        nextPoint = dfs.getNextStep(nextPoint)


startExploration((1, 4))
