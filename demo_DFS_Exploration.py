import numpy as np


OPEN = 0
WALL = 1
VISITED = 2

# Create Board and Storing Stack
board = np.zeros((5, 5))

# Obstacles | Walls
board[3, 1] = 1
board[4, 1] = 1

visitedStack = []

# Starting Point
currentRow, currentColumn = 0, 0

exploring = True

board[currentRow, currentColumn] = VISITED
visitedStack.append((currentRow, currentColumn))

while exploring:
    # exploring function
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

    print("currentRow: ", currentRow)
    print("currentColumn: ", currentColumn)
    print("visitedStack: ", visitedStack)
    print(board)
    print()


print(board)

# main()