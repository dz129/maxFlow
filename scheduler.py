from flownetwork import *


def schedule(stationcounts, stationtimes, employeetraining, employeetimes):
    """station counts: a list of length 4 containing (in order):
    number of employees per shift on blending
    number of employees per shift on cooking
    number of employees per shift on straining
    number of employees per shift on finishing

    stationtimes:  list of lists of length 4 containing (in order):
    shift times for blending
    shift times for cooking
    shift times for straining
    shift times for finishing

    employeetraining: index i contains the list of stations that employee i is trained to work on
    empolyeetimes: index i contains the list of times that employee i can work
    """
    maxFlowGraph = flownetwork("start", "end")

    for i in range(len(employeetimes)):
        maxFlowGraph.add_node("e:" + str(i))
        maxFlowGraph.add_edge("start", "e:" + str(i), len(employeetimes[i]))
        for j in range(len(employeetimes[i])):
            maxFlowGraph.add_node("e:" + str(i) + "t: " + str(employeetimes[i][j]))
            maxFlowGraph.add_edge("e:" + str(i), "e:" + str(i) + "t: " + str(employeetimes[i][j]), 1)

    for i in range(len(employeetimes)):
        for j in range(len(employeetimes[i])):
            employeetimeNode = "e:" + str(i) + "t: " + str(employeetimes[i][j])
            if "blend" in employeetraining[i]:
                for k in range(len(stationtimes[0])):
                    if stationtimes[0][k] == employeetimes[i][j]:
                        timenode = "b" + str(stationtimes[0][k])
                        maxFlowGraph.add_node(timenode)
                        maxFlowGraph.add_edge(employeetimeNode, timenode, 1)
            if "cook" in employeetraining[i]:
                for k in range(len(stationtimes[1])):
                    if stationtimes[1][k] == employeetimes[i][j]:
                        timenode = "c" + str(stationtimes[1][k])
                        maxFlowGraph.add_node(timenode)
                        maxFlowGraph.add_edge(employeetimeNode, timenode, 1)
            if "strain" in employeetraining[i]:
                for k in range(len(stationtimes[2])):
                    if stationtimes[2][k] == employeetimes[i][j]:
                        timenode = "s" + str(stationtimes[2][k])
                        maxFlowGraph.add_node(timenode)
                        maxFlowGraph.add_edge(employeetimeNode, timenode, 1)
            if "finish" in employeetraining[i]:
                for k in range(len(stationtimes[3])):
                    if stationtimes[3][k] == employeetimes[i][j]:
                        timenode = "f" + str(stationtimes[3][k])
                        maxFlowGraph.add_node(timenode)
                        maxFlowGraph.add_edge(employeetimeNode, timenode, 1)
    for i in range(len(stationtimes)):
        for j in range(len(stationtimes[i])):
            stationtimenode = str(stationtimes[i][j])
            if i == 0:
                maxFlowGraph.add_edge("b" + stationtimenode, "end", stationcounts[i])
            if i == 1:
                maxFlowGraph.add_edge("c" + stationtimenode, "end", stationcounts[i])
            if i == 2:
                maxFlowGraph.add_edge("s" + stationtimenode, "end", stationcounts[i])
            if i == 3:
                maxFlowGraph.add_edge("f" + stationtimenode, "end", stationcounts[i])
    print(maxFlowGraph)
    total_jobs = 0
    for i in range(len(stationcounts)):
        total_jobs += stationcounts[i] * len(stationtimes[i])
    return (maxFlowGraph.maxflow() >= total_jobs)




