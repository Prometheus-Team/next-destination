import numpy as np


# TODO: 
#have a board
#

class DFS:
    OPEN = 0
    WALL = 1
    VISITED = 2
    visitedStack = []
    # todo: the visited stack needs to be updated when the robot moves across a line
    # todo: add branching stack

    def __init__(self, board, stepPriority):
        self.board = board
        self.stepPriority = stepPriority
        # todo: either find the current position from the board
        # todo: or get it on __init__

    # todo
    # return the farthest point in the needed direction
    # this point will be in the OPEN spots in the map
    # - or it can be a VISITED spot if an open slot is not found in the direct vicinity
    def getNextStep(self):
        if (
        currentRow + 1 >= 0
        and currentRow + 1 != board.shape[0]
        and board[currentRow + 1, currentColumn] == OPEN
    ):
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