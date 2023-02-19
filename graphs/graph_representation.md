### Graph Representation

A graph is a data structure used to represent a set of objects and the relationships between them. It consists of a set of vertices (also called nodes) and a set of edges, where each edge connects two vertices.

#### Adjacency matrix representation using 2d numpy array
```python
# Adjacency matrix representation using 2d numpy array

import numpy as np

V = [0,1,2,3,4,5]
E = [(0,1),(0,2),(1,3),(1,4),(2,4),(2,3),(2,4),(5,1),(0,5)]

#representing edge from u to v

size = len(V)

AMat = np.zeros(shape = (size, size))
for (i,j) in E:
    AMat[i,j] = 1

print(AMat)
```
#### Adjacency matrix representation without numpy

```python
#Adjacency matrix creation - without numpy

V = [0,1,2,3,4,5]
E = [(0,1),(0,2),(1,3),(1,4),(2,4),(2,3),(2,4),(5,1),(0,5)]

size = len(V)
AMat = list()
f = ([0]*size)
for i in range(size):
    AMat.append(f)

for(i,j) in E:
    AMat[i][j] = 1

print(AMat)
```

#### Applications:
 social network analysis, route planning, computer networks, and many more. Many algorithms have been developed for various graph problems, such as finding the shortest path between two vertices, finding a minimum spanning tree, and detecting cycles in a graph.