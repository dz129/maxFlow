

class edge:

    def __init__(self, source, dest, capacity, flow=0):
        self.source = source
        self.dest = dest
        self.capacity = capacity
        self.flow = flow

    def __str__(self):
        return self.source+"->"+self.dest+":"+str(self.flow)+"/"+str(self.capacity)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.source) ^ hash(self.dest)

    def __eq__(self, other):
        return (self.source == other.source) and (self.dest == other.dest)

class flownetwork:

    def __init__(self, source, sink):
        self.network = {}
        self.back = {}
        self.source = source
        self.sink = sink
        self.add_node(source)
        self.add_node(sink)

    def __str__(self):
        #return str(self.network) + "(source:"+self.source+",sink:"+self.sink+")"
        return repr(self)

    def __repr__(self):
        s = ""
        for node in self.network:
            for edge in self.network[node]:
                s += str(edge) + "\n"
        return s

    def add_node(self, node):
        if node not in self.network:
            self.network[node] = []
            self.back[node] = []


    def add_edge(self, source, dest, capacity):
        self.add_node(source)
        self.add_node(dest)
        e = edge(source, dest, capacity)
        self.network[source].append(e)
        self.back[dest].append(e)


    def add_flow(self, source, dest, amount):
        added = False
        for e in self.network[source]:
            if e.dest==dest and e.flow+amount<=e.capacity:
                e.flow += amount
                added = True
                break
        if not added:
            for e in self.back[source]:
                if e.source == dest and e.flow >= amount:
                    e.flow -= amount
                    added = True
                    break
        return added


    def residual_neighbors(self, node):
        n = []
        for e in self.network[node]:
            if e.flow < e.capacity:
                n.append(e.dest)
        for e in self.back[node]:
            if e.flow > 0:
                n.append(e.source)
        return n


    def augmenting_path(self):
        parents = {}
        parents[self.source] = None
        toVisit = [self.source]
        sink_found = False
        while len(toVisit) > 0 and not sink_found:
            current = toVisit.pop(0)
            for neighbor in self.residual_neighbors(current):
                if neighbor == self.sink:
                    sink_found = True
                if neighbor not in parents:
                    parents[neighbor] = current
                    toVisit.append(neighbor)
        if not sink_found:
            return []
        path = [self.sink]
        while path[0] != self.source:
            current = path[0]
            previous = parents[current]
            path.insert(0, previous)
        return path


    def path_bottleneck(self, path):
        if len(path) < 2:
            return 0
        bottleneck = float('inf')
        current = path[0]
        next = path[1]
        for i in range(len(path)-1):
            current = path[i]
            next = path[i+1]
            forward = False
            for e in self.network[current]:
                if e.dest == next:
                    forward = True
                    bottleneck = min(bottleneck,e.capacity-e.flow)
            if not forward:
                for e in self.network[next]:
                    if e.dest == current:
                        bottleneck = min(bottleneck,e.flow)
        return bottleneck


    def push_flow(self,path,amount):
        for i in range(len(path)-1):
            current = path[i]
            next = path[i+1]
            self.add_flow(current, next, amount)


    def maxflow(self):
        path = self.augmenting_path()
        while len(path)>0:
            amount = self.path_bottleneck(path)
            self.push_flow(path, amount)
            path = self.augmenting_path()
        outflow = 0
        for e in self.network[self.source]:
            outflow += e.flow
        for e in self.back[self.source]:
            outflow -= e.flow
        return outflow


def main():
    graph = flownetwork("s", "t")
    graph.add_edge("s", "a", 20)
    graph.add_edge("s", "b", 10)
    graph.add_edge("a", "b", 30)
    graph.add_edge("a","t",10)
    graph.add_edge("b","t",23)
    graph.add_edge("s","x", 5)
    graph.add_edge("x", "a", 5)
    f = graph.maxflow()
    print(graph)
    print(f)
    # path = ['s','a','b','t']
    # amount = graph.path_bottleneck(path)
    # graph.push_flow(path, amount)
    # print(graph)
    # path = graph.augmenting_path()
    # amount = graph.path_bottleneck(path)
    # graph.push_flow(path, amount)
    # print(graph)

#main()


