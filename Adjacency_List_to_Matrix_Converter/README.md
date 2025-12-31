## Objective: Build a function that converts an adjacency list representation of a graph into an adjacency matrix. An adjacency list is a dictionary where each key represents a node, and the corresponding value is a list of nodes that the key node is connected to.
An adjacency matrix is a 2D array where the entry at position `[i][j]` is `1` if there's an edge from node `i` to node `j`, and `0` otherwise.

For example, given the adjacency list:
```
{
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}
```
The corresponding adjacency matrix would be:
```
[
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
]
```

# User Stories:

1. You should define a function named `adjacency_list_to_matrix` to convert an adjacency list to an adjacency matrix.
2. The function should take a dictionary representing the adjacency list of an unweighted (either undirected or directed) graph as its argument.
3. The function should:
   - Convert the adjacency list to an adjacency matrix.
   - Print each row in the adjacency matrix.
   - Return the adjacency matrix.
