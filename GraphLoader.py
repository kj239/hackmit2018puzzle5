from Graph import Graph
from apiPoster import apiPoster

class GraphLoader():

    def __init__(self):
        self.gps = apiPoster()
        self.adjList = self.gps.getadjList()
        self.graph = Graph()
        
        for i in range(0,22500):
            self.graph.add_vertex(i)
        
        for i in range(0,22500):
            toList = self.adjList[i]
            for vertex in toList:
                self.graph.add_edge(i, vertex, 1)
         
    def __str__(self):
         return 'Graph loaded!'
