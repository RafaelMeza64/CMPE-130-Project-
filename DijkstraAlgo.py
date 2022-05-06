from concurrent.futures import process
import heapq

class Graph: 
    def __init__(self, Graph, vertices):
        self.V = vertices
        self.G = Graph

    def findShortestPath(self, source):
        INF = 1e7
        distance = [INF for i in range(self.V)]
        previous = [None for i in range(self.V)]
        processed = [False for i in range(self.V)]

        distance[source] = 0
        Q = []

        heapq.heappush(Q, [distance[source], 0])

        
        while Q: 
            u = heapq.heappop(Q)[1]
            processed[u] = True
            for i, N in enumerate(self.G[u]): 
                if N != 0 and processed[i] == False and distance[u] != INF: 
                    temporaryDistance = distance[u] + N
                    if temporaryDistance < distance[i]: 
                        distance[i] = temporaryDistance
                        previous[i] = u
                        heapq.heappush(Q, [distance[i], i])
        return distance
