import scheduler

def readinput():
    blendcount = int(input().strip().split()[1])
    blendtimes = []
    for item in input().strip().split():
        blendtimes.append(int(item))
    cookcount = int(input().strip().split()[1])
    cooktimes = []
    for item in input().strip().split():
        cooktimes.append(int(item))
    straincount = int(input().strip().split()[1])
    straintimes = []
    for item in input().strip().split():
        straintimes.append(int(item))
    finishcount = int(input().strip().split()[1])
    finishtimes = []
    for item in input().strip().split():
        finishtimes.append(int(item))
    employeecount = int(input().strip().split()[1])
    employee_training = []
    employee_times = []
    for i in range(employeecount):
        training = input().strip().split()
        employee_training.append(training)
        times = []
        for item in input().strip().split():
            times.append(int(item))
        employee_times.append(times)
    stationtimes = [blendtimes, cooktimes, straintimes, finishtimes]
    stationcounts = [blendcount, cookcount, straincount, finishcount]
    print(scheduler.schedule(stationcounts, stationtimes, employee_training, employee_times))


readinput()