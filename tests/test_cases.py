""" This file contains different test cases for a recursive Floyd Warshall algorithm
a function that identifies the shortest path (e.g., in terms of distance)
between all node pairs in directed weighted networks
with positive and negative edge weights but no negative weight cycles.
Expected input and outputs are shown.
"""
import sys
NO_PATH = sys.maxsize # When edges do not exist

# Test case A: Recursive function
"""Title: Floyd Warshall Algorithm | DP-16
  Author:Geeksforgeeks
  Availability: http://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
"""


input_a = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]


output_a = [[0, 7, 12, 8],
          [NO_PATH, 0, 5, 7],
          [NO_PATH, NO_PATH, 0, 2],
          [NO_PATH, NO_PATH, NO_PATH, 0]]


# Test case B: Graph with negative edges


input_b = [[0, -7, NO_PATH, -8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]


output_b = [[0, -7, -2, -8],
           [NO_PATH, 0, 5, 7],
           [NO_PATH, 9223372036854775800, 0, 2],
           [NO_PATH, 9223372036854775800, 9223372036854775805, 0]]
              

# Test case C: Graph with added 0 node and all positive edges

input_c = [[0, 1, 2, 3],
                 [NO_PATH, 0, 2, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 5],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]

output_c = [[0, 1, 2, 3],
           [NO_PATH, 0, 2, 7],
           [NO_PATH, NO_PATH, 0, 5],
           [NO_PATH, NO_PATH, NO_PATH, 0]]

# Test case D: Graph with added 0 node and all negative edges

input_d = [[0, -1, NO_PATH, NO_PATH],
                 [NO_PATH, 0, -2, NO_PATH],
                 [NO_PATH, NO_PATH, 0, -5],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]


output_d = [[0, -1, -3, -8],
           [9223372036854775800, 0, -2, -7],
           [9223372036854775802,9223372036854775801, 0, -5],
           [NO_PATH,9223372036854775806, 9223372036854775804, 0]]
