from concurrent.futures import process
import heapq
from turtle import distance

INF = 99999999

class Map: 
    def __init__(self, Graph, vertices):
        self.V = vertices
        self.G = Graph

    def findShortestPath(self, source):
        INF = 1e7
        distance = [INF for i in range(self.V)]
        previous = [None for i in range(self.V)]
        processed = [False for i in range(self.V)]

        distance[source] = 0
        previous[source] = source
        Q = []

        heapq.heappush(Q, [distance[source], source])

        
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
        return distance, previous

    #this function will print out the shortest path from the source node to the target node like: source -> intermediate nodes ... -> target
    def printShortestPath(self, source, target): 
        pathStack = []

        distanceList = []
        pathList = []

        distanceList, pathList = self.findShortestPath(source)

        stopFlag = True
        currentIndex = target

        while stopFlag != False: 
            pathStack.append(pathList[currentIndex])
            currentIndex = pathList[currentIndex]
            if currentIndex == source: 
                stopFlag = False
        

        while pathStack: 
            print(pathStack.pop(), "-> ", end='')
        
        print(target)

    def getTotalCost(self, source, target): 
        distanceList = []
        pathList = []

        distanceList, pathList = self.findShortestPath(source)

        return distanceList[target]
        
