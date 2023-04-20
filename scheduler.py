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
    maxFlowGraph = flownetwork("s", "t")
    



    for i in range(len(employeetimes)):
        maxFlowGraph.add_edge("s", "e" + str(i), len(employeetimes[i]))
        for j in employeetimes[i]:
            maxFlowGraph.add_edge("e" + str(i), "e" + str(i) + "t" + str(j), 1)
    for i in range(len(stationtimes)):
        for j in stationtimes[i]:
            if i == 0:
                maxFlowGraph.add_edge("b" + str(j), "t", stationcounts[i])
            if i == 1:
                maxFlowGraph.add_edge("c" + str(j), "t", stationcounts[i])
            if i == 2:
                maxFlowGraph.add_edge("s" + str(j), "t", stationcounts[i])
            if i == 3:
                maxFlowGraph.add_edge("f" + str(j), "t", stationcounts[i])
    for i in range(len(employeetimes)):
        for j in employeetimes[i]:
            if "blend" in employeetraining[i]:
                for k in stationtimes[0]:
                    if k == j:
                        maxFlowGraph.add_edge("e" + str(i) + "t" + str(j), "b" + str(k), 1)
            if "cook" in employeetraining[i]:
                for k in stationtimes[1]:
                    if k == j:
                        maxFlowGraph.add_edge("e" + str(i) + "t" + str(j), "c" + str(k), 1)
            if "strain" in employeetraining[i]:
                for k in stationtimes[2]:
                    if k == j:
                        maxFlowGraph.add_edge("e" + str(i) + "t" + str(j), "s" + str(k), 1)
            if "finish" in employeetraining[i]:
                for k in stationtimes[3]:
                    if k == j:
                        maxFlowGraph.add_edge("e" + str(i) + "t" + str(j), "f" + str(k), 1)
    print(maxFlowGraph)
    need = 0
    for i in range(len(stationcounts)):
        need += stationcounts[i] * len(stationtimes[i])
    return (maxFlowGraph.maxflow == need)
    




