
class Graph:
    def __init__(self):
        self.graph={}

    def AddVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def AddEdge(self, V1, V2, isDirected=False):
        self.AddVertex(V1)
        self.AddVertex(V2)

        self.graph[V1].append(V2)
        if not isDirected:
            self.graph[V2].append(V1)

    def Display(self):
        for key,value in self.graph.items():
            print(f"{key} => {value}")

    def getVertices(self):
        for i in self.graph:
            print(i)

    def getEdges(self):
        for key,value in self.graph.items():
            for vertex in value:
                print(f"{key},{vertex}")

    def remove(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]

        for key,value in self.graph.items():
            if vertex in value:
                value.remove(vertex)

    def removeEdge(self,v1,v2):
        if self.isEdge(v1,v2):
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)

    def isEdge(self,v1,v2):
        return v1 in self.graph[v2] or v2 in self.graph[v1]


graph = Graph()
graph.AddEdge("x","y")
graph.AddEdge("x","z")
graph.AddEdge("z","w")
graph.AddEdge("x","w")


graph.getEdges()
print()
print()
graph.removeEdge("x","w")
graph.getEdges()