# def directionPriorityServer():
#     rospy.init_node("Direction_Priority_Generator_Server")
#     s = rospy.Service(
#         "Direction_Priority_Generator", DirectionPriority, handleDirectionPriority
#     )
#     print("Ready to Generate Direction Priorities.")
#     rospy.spin()


# def directionPriorityClient(x, y):
#     rospy.wait_for_service("Direction_Priority_Generator")
#     try:
#         DirectionPriorityGenerator = rospy.ServiceProxy(
#             "Direction_Priority_Generator", DirectionPriority
#         )
#         resp1 = DirectionPriorityGenerator(x, y)
#         # todo: convert to JSON, use this (https://github.com/uos/rospy_message_converter)
#         return resp1
#     except rospy.ServiceException as e:
#         print("Service call failed: %s" % e)


# def handleDirectionPriority(req):
#     # req.map -> may need to be deserialized
#     numberOfRows, numberOfColumns = req.map.shape

#     #
#     west = req.currentPosition[0]
#     east = numberOfColumns - req.currentPosition[0]
#     north = req.currentPosition[1]
#     south = numberOfRows - req.currentPosition[1]

#     robotPositionState = NextDestination(
#         bounds={
#             "northBound": north,
#             "southBound": south,
#             "westBound": west,
#             "eastBound": east,
#         }
#     )
#     dxnPriorities = robotPositionState.generateStepPriority()

#       tuple of Dictionaries
#     ({'WEST': 1, 'NORTH': 2, 'SOUTH': 3, 'EAST': 4}, {1: 'WEST', 2: 'NORTH', 3: 'SOUTH', 4: 'EAST'})
#     return DirectionPriorityResponse()


# Next Step
# def nextStepServer():
#     rospy.init_node("Next_Step_Server")
#     s = rospy.Service("Next_Step", NextStep, handleNextStep)
#     print("Ready to Generate the Next Step.")
#     rospy.spin()


# def nextStepClient(x, y):
#     rospy.wait_for_service("Next_Step")
#     try:
#         NextStep = rospy.ServiceProxy("Next_Step", NextStep)

#         # todo: Do some serialization on arrays
#         # todo: convert dxnPriorities to JSON, use this (https://github.com/uos/rospy_message_converter)
#         resp1 = NextStep(
#             areaMap, currentPosition, directionPriorities, branchingStack, visitedMap
#         )
#         return resp1
#     except rospy.ServiceException as e:
#         print("Service call failed: %s" % e)


# def handleDirectionPriority(req):
#     areaMap, currentPosition, directionPriorities, branchingStack, visitedMap = req

#     dfs = DFS(areaMap, directionPriorities, branchingStack, visitedMap)

#     x = currentPosition[0]
#     y = currentPosition[1]

#     nextPoint = dfs.getNextStep((x, y))
#     return nextPoint
