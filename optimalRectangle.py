import numpy as np


def getOptimalRectangle(array, circleRadius, tileSize, conversion=1):
    arrayRow, arrayColumn = array.shape
    # convert circleradius size to tile size if not equal
    circleRadius = tileSize * conversion
    # formula for x and y is r / squareroot(2)
    x = int(circleRadius / (2 ** 1 / 2))

    # considering that the array formed fromthe vision is assigned for bottom to up (decending value) and left to right(ascending value)
    numberOfTiles = int(x / tileSize)

    # cutting the array vertical starting from bottom
    newArrayRowStart = arrayRow - numberOfTiles
    array = array[
        newArrayRowStart:,
    ]

    # cutting the array horizontally starting from the right
    newArrayColumnStart = arrayColumn - numberOfTiles
    startingGap = int(newArrayColumnStart / 2)
    array = array[:, startingGap : startingGap + numberOfTiles + 1]


def getCarEdges(carPosition, carDimension):
    carLength, carWidth = carDimension
    carXPos, carYPos = carPosition
    carPoints = [carPosition]
    carPoints.append((carXPos, carYPos + carWidth))
    carPoints.append((carXPos + carLength, carYPos))
    carPoints.append((carXPos + carLength, carYPos + carWidth))

    return carPoints


def getMapCluster(array, clusterDirection, carDimension, carCurrentPosition):
    arrayRow, arrayColumn = array.shape
    carCoordinates = getCarEdges(carCurrentPosition, carDimension)

    if clusterDirection == "NORTH":
        # columns stay constant and check rows if they are open
        workingArray = array[
            0 : carCoordinates[0][0], carCoordinates[0][1] : carCoordinates[1][1] + 1
        ]
        workingArrayRow, workingArrayColumn = workingArray.shape
        for i in range(workingArrayRow):
            # considering all movable areas will be valued 1 so the sum of all the values within the array should be the size of the array
            checkArray = workingArray[
                i : workingArrayRow + 1,
            ]
            if sum(sum(checkArray)) == checkArray.size:
                # it can move this much tiles
                return workingArrayRow - i

        # it cant move any tiles in this direction
        return 0

    if clusterDirection == "EAST":
        # rows stay constant and check columns if they are open
        workingArray = array[
            carCoordinates[1][0] : carCoordinates[3][0], carCoordinates[1][1] :
        ]
        workingArrayRow, workingArrayColumn = workingArray.shape
        for i in range(workingArrayColumn):
            # considering all movable areas will be valued 1 so the sum of all the values within the array should be the size of the array
            checkArray = workingArray[: workingArrayColumn + 1 - i]
            if sum(sum(checkArray)) == checkArray.size:
                # it can move this much tiles
                return workingArrayColumn - i

        # it cant move any tiles in this direction
        return 0
