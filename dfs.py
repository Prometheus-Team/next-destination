import numpy as np
from util import Directions, Point
from nextDestination import NextDestination


class DFS:
    OPEN = 0
    WALL = 1
    VISITED = 2
    BUFFER = 3
    SOUTH = "SOUTH"
    NORTH = "NORTH"
    WEST = "WEST"
    EAST = "EAST"

    BUFFER_SIZE = 3

    # todo: is this not important?
    visitedStack = []

    branchingStack = []
    # todo: the visited stack needs to be updated when the robot moves across a line
    # todo: add branching stack

    # todo: discuss with Milky
    # ? Should we check distances from currentPosition to the closest branching point? Instead of going back to the last seen branching point?
    # ?

    def __init__(self, board, stepPriority):
        self.board = board
        # loop through the board
        # when you get a 1, set the below to self.BUFFER
        # row1 - row2
        # column1 - column2

        self.visitedMap = np.zeros(board.shape)
        # 2D num-py array
        # [[,]]
        # value of a cell --> OPEN, WALL, VISITED, UNVISITED, ROBOT POSITION

        # todo: discuss with Sami
        # ? Open, Wall, and Unvisited should be already in Sami's input
        # ? We're keeping track of Visited in this class.
        # ? It would be great if we can get the Robot's Position from Sami.

        # padding/buffer to check whether something is an obstacle

        self.stepPriority = stepPriority
        # ["EAST", "NORTH", "SOUTH", "WEST"]

    def addBufferToObstacles(self):
        for rowIndex, row in enumerate(self.board):
            for cellIndex, cell in enumerate(row):
                if cell == self.WALL:
                    print("HERE?")

                    for i in range(self.BUFFER_SIZE * 2 + 1):
                        for j in range(self.BUFFER_SIZE * 2 + 1):
                            currentRowIndex = rowIndex - self.BUFFER_SIZE + i
                            currentCellIndex = cellIndex - self.BUFFER_SIZE + j

                            squaredRowDistance = (rowIndex - currentRowIndex) ** 2
                            squaredCellDistance = (cellIndex - currentCellIndex) ** 2
                            distance = (squaredRowDistance + squaredCellDistance) ** 0.5

                            if (
                                currentRowIndex > 0
                                and currentCellIndex > 0
                                and distance <= self.BUFFER_SIZE
                            ):
                                self.board[
                                    rowIndex - self.BUFFER_SIZE + i,
                                    cellIndex - self.BUFFER_SIZE + j,
                                ] = self.BUFFER

    def getOpenDirections(self, currentPosition):
        currentRow = currentPosition[0]
        currentColumn = currentPosition[1]

        openDirections = []
        sortedOpenDirections = []

        # todo: discuss with Sami/Milky??
        # todo: the +/- 1 values should actually be the vision range of the robot.
        # todo: OR we should decide on the size of a "TILE"

        # decide on adding padding to openings on both sides...
        # dimension of robot - 30x30
        # min distance traveled 30cm

        # ?: ORRRR maybe set the next go to point to a place where we think we might find an open space that is facing our preferred direction

        try:
            if (
                currentRow + 1 >= 0
                and self.board[currentRow + 1, currentColumn] == self.OPEN
                and self.board[currentRow + 1, currentColumn] != self.BUFFER
                and self.visitedMap[currentRow + 1, currentColumn] != self.VISITED
            ):
                openDirections.append(self.SOUTH)
        except IndexError as err:
            pass

        try:
            if (
                currentRow - 1 >= 0
                and self.board[currentRow - 1, currentColumn] == self.OPEN
                and self.board[currentRow - 1, currentColumn] != self.BUFFER
                and self.visitedMap[currentRow - 1, currentColumn] != self.VISITED
            ):
                openDirections.append(self.NORTH)
        except IndexError as err:
            pass

        try:
            if (
                currentColumn + 1 >= 0
                and self.board[currentRow, currentColumn + 1] == self.OPEN
                and self.board[currentRow, currentColumn + 1] != self.BUFFER
                and self.visitedMap[currentRow, currentColumn + 1] != self.VISITED
            ):
                openDirections.append(self.EAST)
        except IndexError as err:
            pass

        try:
            if (
                currentColumn - 1 >= 0
                and self.board[currentRow, currentColumn - 1] == self.OPEN
                and self.board[currentRow, currentColumn - 1] != self.BUFFER
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
            if len(self.branchingStack) == 0 or (
                len(self.branchingStack) > 0
                and self.branchingStack[-1]
                != (
                    currentRow,
                    currentColumn,
                )
            ):
                # todo: append also on the edge of updateVisitedMap where we go to the edge of the VISION_RANGE

                self.branchingStack.append(
                    # (currentRow, currentColumn, sortedOpenDirections)
                    (currentRow, currentColumn)
                )

        return sortedOpenDirections

    # todo
    def updateVisitedMap(self, currentPosition, direction):
        self.visitedMap[currentPosition[0], currentPosition[1]] = self.VISITED

        VISITING_RANGE = 4
        if direction == "NORTH" or direction == "SOUTH":
            # if facing NORTH or SOUTH, mark adjacent (EAST and WEST) positions inside the VISION_RANGE as VISITED

            continueLeftCheck = True
            continueRightCheck = True
            for i in range(VISITING_RANGE):

                # todo: add the position to branching stack on the last loop
                if continueLeftCheck is False and continueRightCheck is False:
                    break

                leftSideAdjacentCellColumn = currentPosition[1] - i - 1
                rightSideAdjacentCellColumn = currentPosition[1] + i + 1

                if leftSideAdjacentCellColumn < 0:
                    leftSideAdjacentCellColumn = 0

                try:
                    if (
                        continueLeftCheck
                        and self.visitedMap[
                            currentPosition[0], leftSideAdjacentCellColumn
                        ]
                        != self.VISITED
                        and self.board[currentPosition[0], leftSideAdjacentCellColumn]
                        == self.OPEN
                    ):
                        self.visitedMap[
                            currentPosition[0], leftSideAdjacentCellColumn
                        ] = self.VISITED
                    else:
                        continueLeftCheck = False

                    if (
                        continueRightCheck
                        and self.visitedMap[
                            currentPosition[0], rightSideAdjacentCellColumn
                        ]
                        != self.VISITED
                        and self.board[currentPosition[0], rightSideAdjacentCellColumn]
                        == self.OPEN
                    ):
                        self.visitedMap[
                            currentPosition[0], rightSideAdjacentCellColumn
                        ] = self.VISITED

                    else:
                        continueRightCheck = False

                except IndexError:
                    break

        elif direction == "EAST" or direction == "WEST":
            continueTopCheck = True
            continueBottomCheck = True

            for i in range(VISITING_RANGE):
                topSideAdjacentCellColumn = currentPosition[0] - i - 1
                bottomSideAdjacentCellColumn = currentPosition[0] + i + 1

                if topSideAdjacentCellColumn < 0:
                    topSideAdjacentCellColumn = 0

                if continueTopCheck is False and continueBottomCheck is False:
                    break

                try:
                    if (
                        continueTopCheck
                        and self.visitedMap[
                            topSideAdjacentCellColumn, currentPosition[1]
                        ]
                        != self.VISITED
                        and self.board[topSideAdjacentCellColumn, currentPosition[1]]
                        == self.OPEN
                    ):
                        self.visitedMap[
                            topSideAdjacentCellColumn, currentPosition[1]
                        ] = self.VISITED
                    else:
                        continueTopCheck = False

                    if (
                        continueBottomCheck
                        and self.visitedMap[
                            bottomSideAdjacentCellColumn, currentPosition[1]
                        ]
                        != self.VISITED
                        and self.board[bottomSideAdjacentCellColumn, currentPosition[1]]
                        == self.OPEN
                    ):
                        self.visitedMap[
                            bottomSideAdjacentCellColumn, currentPosition[1]
                        ] = self.VISITED

                    else:
                        continueBottomCheck = False

                except IndexError:
                    break

    def getNextStep(self, currentPosition):
        self.addBufferToObstacles()
        openDirections = self.getOpenDirections(currentPosition)

        directionFacing = ""
        if len(openDirections) > 0:
            directionFacing = openDirections[0]
        self.updateVisitedMap(currentPosition, directionFacing)

        print("*************************************")
        print(openDirections)
        print("*************************************")
        print(self.visitedMap)

        for direction in openDirections:

            if self.stepPriority[0][direction] == 1:
                while True:
                    newPoint = Point.addTuples(
                        currentPosition, Directions.getCoordinate(direction)
                    )

                    openDirections = self.getOpenDirections(newPoint)
                    if (
                        len(openDirections) > 0
                        and self.stepPriority[0][openDirections[0]] == 1
                    ):
                        self.updateVisitedMap(newPoint, direction)
                        currentPosition = newPoint
                    else:
                        return newPoint

            else:
                prevStepPriority = self.stepPriority[0][direction]

                while True:
                    newPoint = Point.addTuples(
                        currentPosition, Directions.getCoordinate(direction)
                    )

                    openDirections = self.getOpenDirections(newPoint)
                    if (
                        len(openDirections) > 0
                        and self.stepPriority[0][openDirections[0]] < prevStepPriority
                    ):
                        return newPoint
                    elif (
                        len(openDirections) > 0
                        and self.stepPriority[0][openDirections[0]] == prevStepPriority
                    ):
                        self.updateVisitedMap(newPoint, direction)
                        currentPosition = newPoint
                    else:
                        return newPoint

        else:
            # backtracking
            # print("got back to branching point")
            if len(self.branchingStack) > 0:
                returnPoint = self.branchingStack.pop()
                # print(returnPoint)
                return returnPoint
            else:
                # print("no more moves")
                return -50

        # (x,y)

    # todo
    # return the farthest point in the needed direction
    # this point will be in the OPEN spots in the map
    # - or it can be a VISITED spot if an open slot is not found in the direct vicinity


# Example for Usage
def startExploration(droneStartingCoordinate):
    x = droneStartingCoordinate[0]
    y = droneStartingCoordinate[1]

    # todo: drone starting coordinate should be the bounds in the next line
    robotPositionState = NextDestination(
        bounds={"northBound": 20, "southBound": 20, "westBound": 10, "eastBound": 30}
    )
    dxnPriorities = robotPositionState.generateStepPriority()

    # print("Direction Priorities: ", dxnPriorities)

    simpleMap = np.zeros((5, 5))

    dfs = DFS(simpleMap, dxnPriorities)

    nextPoint = (x, y)
    while nextPoint != -50:
        nextPoint = dfs.getNextStep(nextPoint)


startExploration((1, 4))
