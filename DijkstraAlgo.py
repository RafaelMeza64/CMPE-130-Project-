import heapq
import timeit

INF = 99999999

class Map:

    # class constructor
    def __init__(self, Graph, vertices, header):
        self.V = vertices
        self.G = Graph
        self.header = header

    # find the shortest from a node to all nodes
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

    # this function will print out the shortest path from the source node to the target node like:
    # source -> intermediate nodes ... -> target
    def printShortestPath(self, source, target):
        pathString = ""
        pathStack = []

        distanceList = []
        pathList = []

        time1 = timeit.default_timer()

        distanceList, pathList = self.findShortestPath(source)

        time2 = timeit.default_timer()
        total_time = time2-time1
        print("Total Time: " + str(total_time) + " seconds")

        stopFlag = True
        currentIndex = target

        while stopFlag != False: 
            pathStack.append(pathList[currentIndex])
            currentIndex = pathList[currentIndex]
            if currentIndex == source: 
                stopFlag = False
        
        while pathStack:
            pathString += self.header[int(pathStack[len(pathStack)-1])]
            pathStack.pop(len(pathStack)-1)
            # print(len(pathStack))
            if len(pathStack) <= 0:
                break
            else:
                pathString += " \u2192 "
        pathString += " \u2192 " + self.header[int(target)]
        return pathString

    def getTotalCost(self, source, target): 
        distanceList = []
        pathList = []

        distanceList, pathList = self.findShortestPath(source)

        return distanceList[target]
        
