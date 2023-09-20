class DirectedGraph():
    def __init__(self) -> None:
        self._adjacency_list = {}

    def add_edge(self, from_node: int, to_node: int) -> None:
        if from_node not in self._adjacency_list:
            self._adjacency_list[from_node] = set()
        
        self._adjacency_list[from_node].add(to_node)

    def bfs(self, start_node: int) -> None:
        if start_node not in self._adjacency_list:
            return

        queue = [start_node]
        visited = set()
        while (len(queue) > 0):
            current = queue.pop()
            visited.add(current)
            queue.extend(filter(lambda node: node not in visited, self._adjacency_list[current]))
            print(f'{current}')


dg = DirectedGraph()
dg.add_edge(1, 1)
dg.add_edge(1, 2)
dg.add_edge(1, 3)
dg.add_edge(2, 1)
dg.add_edge(2, 2)
dg.add_edge(2, 6)
dg.add_edge(3, 3)
dg.add_edge(3, 4)
dg.add_edge(3, 3)
dg.add_edge(4, 3)
dg.add_edge(4, 4)
dg.add_edge(4, 8)
dg.add_edge(5, 5)
dg.add_edge(5, 6)
dg.add_edge(5, 7)
dg.add_edge(6, 5)
dg.add_edge(6, 6)
dg.add_edge(6, 6)
dg.add_edge(7, 7)
dg.add_edge(7, 8)
dg.add_edge(7, 7)
dg.add_edge(8, 7)
dg.add_edge(8, 8)
dg.add_edge(8, 8)
dg.bfs(1)
