up = 20
down = 20
left = 10
right = 30




If not at edge:
    startingPoint -> the Nearest edge
    theNearestEdge - startingPoint = > A vector or a direction
    For example - LEFT


If at edge already or you get to the edge do this:
    Pick a direction that is parallel to the edge of the MAP
    (This direction will also be perpendicular to[theNearestEdge - startingPoint])

THEN the directions will be:
    Parallel to edge
    Perpendicular to and away from the edge.
    Perpendicular to and facing the edge.
    AntiParallel to the edge




DOWN, RIGHT, LEFT, UP


First approach:
    1. First go to the first nearest edge
    2. Parallel to edge (to the second nearest edge)
    3. Perpendicular to and away from the first nearest edge.
    4. Perpendicular to and facing the first nearest edge.
    5. AntiParallel to the edge

Second approach:
    1. To the nearest edge
    2. To the second nearest edge on the opposite axis
    3. Opposite of 2
    4. Opposite of 1

When all apparent empty spaces are discovered.
Or when the need to backtrack occurs
    - the next step is not open

    - Will recording branches help? Can branches be detected?