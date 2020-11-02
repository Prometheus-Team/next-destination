import numpy as np
from util import Directions


class DFS:
    OPEN = 0
    WALL = 1
    VISITED = 2
    visitedStack = []
    branchingStack = []
    # todo: the visited stack needs to be updated when the robot moves across a line
    # todo: add branching stack

    map = [[]]

    def __init__(self, board, stepPriority):
        self.board = board
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
            if (currentRow + 1 >= 0 and self.map[currentRow + 1, currentColumn] == OPEN):
                openDirections.append(Directions.SOUTH)
        except IndexError as err:
            pass
            
        try:
            if(currentRow - 1 >= 0 and self.map[currentRow - 1, currentColumn] == OPEN):
                openDirections.append(Directions.NORTH)
        except IndexError as err:
            pass

        try:
            if(currentColumn + 1 >= 0 and self.map[currentRow, currentColumn + 1] == OPEN):
                openDirections.append(Directions.EAST)
        except IndexError as err:
            pass
        
        try:
            if(currentColumn - 1 >= 0 and self.map[currentRow, currentColumn - 1] == OPEN):
                openDirections.append(Directions.WEST)
        except IndexError as err:
            pass


        for i in openDirections:
            sortedOpenDirections.append(self.stepPriority[0][i])

        sortedOpenDirections.sort()

        for i in range(len(sortedOpenDirections)):
            sortedOpenDirections[i] = stepPriority[1][sortedOpenDirections[i]]

        if (sortedOpenDirections.__len__ > 1):
            self.branchingStack.append((currentRow, currentColumn, sortedOpenDirections))
            
        return sortedOpenDirections


    # todo
    def getNextStep(self, currentPosition):

        openDirections = self.getOpenDirections(currentPosition)
        
        if (len(openDirections) == 0):
            # No open directions from current position
            # Backtrack!
            
        else:
            # "EAST" | "NORTH" | "SOUTH" | "WEST"
            nextStepDirection = openDirections[0]



        
        # (x,y)

        




    # todo
    # return the farthest point in the needed direction
    # this point will be in the OPEN spots in the map
    # - or it can be a VISITED spot if an open slot is not found in the direct vicinity
    def idk(self, currentPosition):
        currentRow = currentPosition[0]
        currentColumn = currentPosition[1]

        

        try:
            if currentRow + 1 >= 0 and board[currentRow + 1, currentColumn] == OPEN:
            

        except IndexError as err:
            print(err)
            
            try:
                
                if currentRow + 1 >= 0 and board[currentRow - 1, currentColumn] == OPEN:
                    currentRow = currentRow + 1
            except expression as identifier:

                try:
                    if currentColumn + 1 >= 0 and board[currentRow, currentColumn + 1] == OPEN:
                        board[currentRow, currentColumn] = VISITED
                except expression as identifier:

                    try:
                        if currentColumn + 1 >= 0 and board[currentRow, currentColumn - 1] == OPEN:
                            visitedStack.append((currentRow, currentColumn))
                    except expression as identifier:





        if currentRow + 1 >= 0 and board[currentRow + 1, currentColumn] == OPEN:
            # GO DOWN
            print("GO DOWN")

            # todo: the check will start at the current position
            # and go to the vision limit from the robot
            # if there is an obstacle before vision limit is reached consider direction blocked
            # loop to check in a direction

            # TODO
            # Consider adding to stack before updating current position
            # Otherwise, there is an extra check when an obstacle is reached
            # visitedStack.append((currentRow, currentColumn))

            openDirections.append("SOUTH")
            currentRow = currentRow + 1
            board[currentRow, currentColumn] = VISITED
            visitedStack.append((currentRow, currentColumn))

        if currentColumn + 1 >= 0 and board[currentRow, currentColumn + 1] == OPEN:
            # GO RIGHT
            print("GO RIGHT")

            openDirections.append("EAST")

            currentColumn = currentColumn + 1
            board[currentRow, currentColumn] = VISITED
            visitedStack.append((currentRow, currentColumn))

        if (
            currentRow - 1 >= 0
            and currentRow - 1 != board.shape[0]
            and board[currentRow - 1, currentColumn] == OPEN
        ):
            # GO UP
            print("GO UP")
            openDirections.append("NORTH")
            currentRow = currentRow - 1
            board[currentRow, currentColumn] = VISITED
            visitedStack.append((currentRow, currentColumn))

        if (
            currentColumn - 1 >= 0
            and currentColumn - 1 != board.shape[1]
            and board[currentRow, currentColumn - 1] == OPEN
        ):
            # GO LEFT
            print("GO LEFT")
            openDirections.append("WEST")
            currentColumn = currentColumn - 1
            board[currentRow, currentColumn] = VISITED
            visitedStack.append((currentRow, currentColumn))

        else:
            # BACKTRACK

            if np.where(board == OPEN)[0].__len__() > 0:
                pass
            else:
                print(">...EXPLORED...<")
                exploring = False

            if visitedStack.__len__() != 0:
                print("Stack Before Popping: ", visitedStack)
                currentRow, currentColumn = visitedStack.pop()
                print("Stack After Popping: ", visitedStack)
            else:
                exploring = False

        # todo: return next step

        # todo: mark the returned next step to the visitedStack
        # visitedStack.append((currentRow, currentColumn))


# region
# Create Board and Storing Stack
# board = np.zeros((5, 5))

# # Obstacles | Walls
# board[3, 1] = 1
# board[4, 1] = 1

# visitedStack = []

# Starting Point
currentRow, currentColumn = 0, 0
# endregion
exploring = False

board[currentRow, currentColumn] = VISITED
visitedStack.append((currentRow, currentColumn))


while exploring:
    # region
    if (
        currentRow + 1 >= 0
        and currentRow + 1 != board.shape[0]
        and board[currentRow + 1, currentColumn] == OPEN
    ):
        # GO DOWN
        print("GO DOWN")

        # TODO
        # Consider adding to stack before updating current position
        # Otherwise, there is an extra check when an obstacle is reached
        # visitedStack.append((currentRow, currentColumn))

        currentRow = currentRow + 1
        board[currentRow, currentColumn] = VISITED
        visitedStack.append((currentRow, currentColumn))

    elif (
        currentColumn + 1 >= 0
        and currentColumn + 1 != board.shape[1]
        and board[currentRow, currentColumn + 1] == OPEN
    ):
        # GO RIGHT
        print("GO RIGHT")
        currentColumn = currentColumn + 1
        board[currentRow, currentColumn] = VISITED
        visitedStack.append((currentRow, currentColumn))

    elif (
        currentRow - 1 >= 0
        and currentRow - 1 != board.shape[0]
        and board[currentRow - 1, currentColumn] == OPEN
    ):
        # GO UP
        print("GO UP")
        currentRow = currentRow - 1
        board[currentRow, currentColumn] = VISITED
        visitedStack.append((currentRow, currentColumn))

    elif (
        currentColumn - 1 >= 0
        and currentColumn - 1 != board.shape[1]
        and board[currentRow, currentColumn - 1] == OPEN
    ):
        # GO LEFT
        print("GO LEFT")
        currentColumn = currentColumn - 1
        board[currentRow, currentColumn] = VISITED
        visitedStack.append((currentRow, currentColumn))

    else:
        # BACKTRACK

        if np.where(board == OPEN)[0].__len__() > 0:
            pass
        else:
            print(">...EXPLORED...<")
            exploring = False

        if visitedStack.__len__() != 0:
            print("Stack Before Popping: ", visitedStack)
            currentRow, currentColumn = visitedStack.pop()
            print("Stack After Popping: ", visitedStack)
        else:
            exploring = False
    # endregion

    # print("currentRow: ", currentRow)
    # print("currentColumn: ", currentColumn)
    # print("visitedStack: ", visitedStack)
    # print(board)
    # print()


# print(board)

# main()