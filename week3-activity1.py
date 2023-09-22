import heapq


class Node:
    def __init__(self, name: str, heuristic: int) -> None:
        self.name = name
        self.heuristic = heuristic

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __lt__(self, other: object) -> bool:
        return self.name < other.name

    def __le__(self, other: object) -> bool:
        return self.name <= other.name

    def __eq__(self, other: object) -> bool:
        return self.name == other.name

    def __ne__(self, other: object) -> bool:
        return self.name != other.name

    def __gt__(self, other: object) -> bool:
        return self.name > other.name

    def __ge__(self, other: object) -> bool:
        return self.name >= other.name

    def __hash__(self) -> int:
        return self.name.__hash__()


class Graph:
    def __init__(self) -> None:
        self._adjacency_list = {}

    def add_edge(self, node1: Node, node2: Node, cost: int) -> None:
        if (node1 not in self._adjacency_list):
            self._adjacency_list[node1] = {}

        if (node2 not in self._adjacency_list):
            self._adjacency_list[node2] = {}

        self._adjacency_list[node1][node2] = cost
        self._adjacency_list[node2][node1] = cost

    def __getitem__(self, node: Node):
        return self._adjacency_list[node]


def greedy_best_first_search(graph: Graph, start: Node, goal: Node) -> list[Node]:
    # initialize the starting state in the format (heuristic, node)
    frontier = [(0, start)]
    visited = set()
    solution = []

    while len(frontier) > 0:
        # take the state with the minimum heuristic in the frontier
        _, current = heapq.heappop(frontier)

        solution.append(current)
        visited.add(current)

        for neighbour in graph[current]:
            # insert a new state into the frontier heap if neighbour is not visited
            if neighbour not in visited:
                heapq.heappush(frontier, (neighbour.heuristic, neighbour))

        print('Current:', current, 'Frontier:', frontier)

        if current == goal:
            break

    return solution


def a_star_search(graph: Graph, start: Node, goal: Node, mode='graph') -> list[Node]:
    if mode not in ['graph', 'tree']:
        raise ValueError()

    # initialize the starting state in the format (f_cost, (node, g_cost))
    frontier = [(0, (start, 0))]
    visited = set()
    path_map = {}

    while len(frontier) > 0:
        # take the state with the minimum f_cost in the frontier
        _, (current, g_cost_current) = heapq.heappop(frontier)

        visited.add(current)

        for neighbour, current_to_neighbour_cost in graph[current].items():
            # avoid visiting the same node in the graph search mode
            if mode == 'graph' and neighbour in visited:
                continue

            # calculate the g_cost and f_cost of neighbour
            g_cost_neighbour = g_cost_current + current_to_neighbour_cost
            f_cost_neighbour = neighbour.heuristic + g_cost_neighbour
            neighbour_state = (f_cost_neighbour, (neighbour, g_cost_neighbour))

            if neighbour not in visited:
                path_map[neighbour] = current

            for idx, (f_cost_existing, (existing, _)) in enumerate(frontier):
                # update f_cost if neighbour is in the frontier and sort the frontier array
                if existing == neighbour and f_cost_existing >= f_cost_neighbour:
                    frontier[idx] = neighbour_state
                    heapq.heapify(frontier)
                    break
            else:
                # insert the new state into the frontier heap
                heapq.heappush(frontier, neighbour_state)

        print('Current:', current, 'Frontier:', frontier)

        if current == goal:
            break

    # reterive the optimal path from path_map
    solution = [goal]

    while solution[-1] != start:
        solution.append(path_map[solution[-1]])

    solution.reverse()

    return solution


def run_search():
    a_node = Node('A', 5)
    b_node = Node('B', 6)
    c_node = Node('C', 8)
    d_node = Node('D', 4)
    e_node = Node('E', 4)
    f_node = Node('F', 5)
    g_node = Node('G', 2)
    h_node = Node('H', 0)

    graph = Graph()
    graph.add_edge(a_node, b_node, 3)
    graph.add_edge(b_node, d_node, 2)
    graph.add_edge(d_node, e_node, 4)
    graph.add_edge(e_node, g_node, 2)
    graph.add_edge(g_node, h_node, 2)
    graph.add_edge(a_node, c_node, 3)
    graph.add_edge(c_node, f_node, 3)
    graph.add_edge(f_node, e_node, 1)
    graph.add_edge(f_node, g_node, 3)

    print('# Greedy Best-First Search')
    print('Solution:', greedy_best_first_search(graph, a_node, h_node))
    print()

    print('# A* Graph Search')
    print('Solution:', a_star_search(graph, a_node, h_node, mode='graph'))
    print()

    print('# A* Tree Search')
    print('Solution:', a_star_search(graph, a_node, h_node, mode='tree'))
    print()


run_search()
