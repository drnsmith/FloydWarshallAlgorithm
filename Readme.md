# Recursive implementation of the Floyd Warshall algorithm  
+ Based upon the orginal imperative version, available here (https://geeksforgeeks.org/floyd-warshall-dp-16)
+ In directed weighted networks (with no negative weight cycles and both positive and negative edge weights), this algorithm determines the shortest path (e.g., in terms of distance) between all pairs of nodes.
``
# Installation and use 
To get started, in the terminal use
this pip manager is for installing the package:
```
$ pip install Floyd
```
Import this function into the script.
```
from floyd.floyd_rec import Floyd
```
This pip manager is for installing dependencies:
```
$ pip install -r requirements.txt
```
# Testing
The tests used within this project are unit tests    
and performance tests. For unit tests, use:
```
python -m unittest 
``` 
For performance tests, use:
```
python -m time
```
and 
```
python -m cProfile 
``` 
# Contributing
Pull requests are welcome. 
Please update tests as appropriate. 
# License
This project is MIT licensed.
# Bibliography
Cormen, T.H., Leiserson, C.E., Rivest, R.L. and Stein, C. (2022) Introduction to algorithms, MIT press.

