def dfs(adjacency_matrix, node_label):
    n = len(adjacency_matrix)
    visited = [False] * n
    stack = [node_label]
    result = []

    while stack:
        current = stack.pop()

        if not visited[current]:
            visited[current] = True
            result.append(current)

            for neighbor in range(n):
                if adjacency_matrix[current][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

    return result
  
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
