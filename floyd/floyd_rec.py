import time
import sys
NO_PATH = sys.maxsize
path = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

def Floyd(path):
    # n is the number of nodes in the graph
    n = len(path)
    def Shortest(u, v, k): # with no intermediary node; since first node = 0, k = -1
        if k == -1:
            return path[u][v] # Return shortest path, when walking through k is shorter
        else:
            return min(Shortest(u, v, k-1), Shortest(u, k,  k-1) +
                       Shortest(v, k, k-1))

    # Shortest path for every pair of nodes/update.
  
    for k in range(n):
        for u in range(n):
            for v in range(n):
                path[u][v] = Shortest(u, v, k)
    
    return path

#
print(path)




