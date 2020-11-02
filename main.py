import numpy as np
import math

# 0 - Undiscovered cell
# 1 - Wall or Obstacle
# 2 - Discovered Cell
# 3 - Discovered and Next to Walls


VISION_RANGE = 5
VISION_ANGLE = 90
INITIAL_BEARING = "north"
BEARING = math.radians(45)

# Playground
area = np.zeros((20, 20))


# Place the dude in the middle
centerRow = int(area.shape[0] / 2)
centerColumn = int(area.shape[1] / 2)

area[centerRow, centerColumn] = 1

areaCopy = np.zeros((20, 20))
areaCopy[centerRow, centerColumn] = 1

# block = area[
#     centerRow - VISION_RANGE : centerRow + 1,
#     centerColumn - VISION_RANGE : centerColumn + VISION_RANGE + 1,
# ]

for rowIndex, row in enumerate(
    area[
        centerRow - VISION_RANGE : centerRow + 1,
        centerColumn - VISION_RANGE : centerColumn + VISION_RANGE + 1,
    ]
):
    for columnIndex, item in enumerate(row):

        # the row at the edge
        # TODO: change 5 to the length of rows?
        # TODO: or maybe the max distance from the position of the robot?
        rowDistace = 5 - rowIndex
        squaredRowDistance = rowDistace ** 2

        # the column at the center
        # TODO: change 5 to the length of columns divided by 2?
        # TODO: or maybe the max distance from the position of the robot?
        columnDistance = columnIndex - 5
        squaredColumnDistance = columnDistance ** 2

        distance = (squaredRowDistance + squaredColumnDistance) ** 0.5

        if columnDistance == 0:
            if rowDistace > 0:
                angle = 90
            # else:
            #     angle = 270
        else:
            angle = math.degrees(math.atan(rowDistace / columnDistance))

        # What the sensor can sense
        # Taking vision_angle and distance into account
        if distance <= 5.0 and (90 - abs(angle) <= VISION_ANGLE / 2):
            # TODO: Do rotation
            # print("Row: ", centerRow - VISION_RANGE + rowIndex)
            # print("Col: ", centerColumn - VISION_RANGE + columnIndex)
            rowNow = centerRow - VISION_RANGE + rowIndex
            columnNow = centerColumn - VISION_RANGE + columnIndex

            rowRotated = (centerColumn - columnNow) * math.sin(BEARING) + (
                centerRow - rowNow
            ) * math.cos(BEARING)
            # region
            # print(
            #     "E: ",
            #     centerColumn - columnNow,
            #     " > ",
            #     ((centerColumn - columnNow) * math.cos(BEARING)),
            # )
            # print(
            #     "E: ",
            #     centerRow - rowNow,
            #     " > ",
            #     math.sin(BEARING),
            #     " > ",
            #     (centerRow - rowNow) * math.sin(BEARING),
            # )
            # endregion

            columnRotated = (centerColumn - columnNow) * math.cos(BEARING) - (
                centerRow - rowNow
            ) * math.sin(BEARING)

            print(
                "ROW: ",
                rowNow,
                " * ",
                centerRow - rowNow,
                " > ",
                rowRotated,
                " > ",
                int(round(rowRotated)),
            )
            print(
                "COL: ",
                columnNow,
                " * ",
                centerColumn - columnNow,
                " > ",
                columnRotated,
                " > ",
                int(round(columnRotated)),
            )
            print()

            print(
                centerRow + int(round(rowRotated)),
                centerColumn + int(round(columnRotated)),
            )
            areaCopy[
                centerRow + int(round(rowRotated)),
                centerColumn + int(round(columnRotated)),
            ] = 2

            area[
                centerRow - VISION_RANGE + rowIndex,
                centerColumn - VISION_RANGE + columnIndex,
            ] = 2
print("AreaCopy: ", areaCopy)

print("The Field: \n", area)
