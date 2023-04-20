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
    #sets a dictionary of employees that that takes their shift and the station they can work in

    employeeTimeandTrain = []
    for i in range(len(employeetimes)):
        temp = {}
        temp[employeetimes[i]] = employeetraining[i]
        employeeTimeandTrain.append(temp)

    
    #gives all the times of shifts
    totalShiftTimes = []
    for k in employeeTimeandTrain:
        for i in k.keys():
            if i not in totalShiftTimes:
                totalShiftTimes.append(i)

        
    #graph will connect the number of shifts a employee can take into the root node
    #so employee with 4 shifts root -> 4 -> employee
    #then it will connect those shifts to stations lets say this employee cooks and strain
    # root -> 4 -> employee -> shifts (4 different shifts) -> stations
    #shift will only connect to stations if the station has that shift
    #the number of shift to station will be the amount of people needed per shift for that station
    # station needing 4 people per shift : shiftA -> 4 -> station , shiftB -> 4 -> station
    graph = flownetwork("start", "end")
    #adds the jobs
    #need to add all the shifts to these nodes later
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("s")
    graph.add_node("f")
    #adds all shift times
    for i in totalShiftTimes:
        graph.add_node(i)

    for i in employeeTimeandTrain:
        #need to add start to these
        #the edge weight would be the number of shifts the employee worked
        name = str(i)
        graph.add_node(name)
        count = 0
        for times in i.keys():
            for time in times:
                graph.add_edge(name,time,1)
                count += 1
        graph.add_edge("start",name,count)

    #add shift times to each station
    for i in range(len(stationtimes)):
        for time in stationtimes[i]:
            if (i == 0):
                graph.add_edge(time, "b", stationcounts[i])
            if (i == 1):
                graph.add_edge(time, "c", stationcounts[i])
            if (i == 2):
                graph.add_edge(time, "s", stationcounts[i])
            if (i == 3):
                graph.add_edge(time, "f", stationcounts[i])
    
    for i in range(len(stationtimes)):
        total = len(stationtimes[i])
        if (i == 0):
            graph.add_edge("b","end",stationcounts[i] * total)
        if (i == 0):
            graph.add_edge("c","end",stationcounts[i] * total)
        if (i == 0):
            graph.add_edge("s","end",stationcounts[i] * total)
        if (i == 0):
            graph.add_edge("f","end",stationcounts[i] * total)
    print(graph.toString()) 

            
    




