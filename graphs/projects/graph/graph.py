"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # pass  # TODO
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            return True

        return False

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        bftQueue = Queue()
        bftQueue.enqueue(starting_vertex)

        visited = set()

        while bftQueue.size() > 0:
            u = bftQueue.dequeue()

            for v in self.vertices[u]:
                if v not in visited:
                    bftQueue.enqueue(v)

            visited.add(u)
            print(u)
        print('------------------------------------')

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        dftStack = Stack()
        dftStack.push(starting_vertex)

        visited = set()

        while dftStack.size() > 0:
            u = dftStack.pop()

            for v in self.vertices[u]:
                if v not in visited and v not in dftStack.stack:
                    dftStack.push(v)

            visited.add(u)
            print(u)
        print('------------------------------------')

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # pass  # TODO
        s = Stack()
        s.push(starting_vertex)

        while s.size() > 0:
            u = s.pop()
            visited.add(u)
            print(u)

            for v in self.vertices[u]:
                if v not in visited:
                    self.dft_recursive(v, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        bftQueue = Queue()
        bftQueue.enqueue(starting_vertex)

        visited = set()

        while bftQueue.size() > 0:
            u = bftQueue.dequeue()

            if u == destination_vertex:
                return True

            for v in self.vertices[u]:
                if v not in visited:
                    bftQueue.enqueue(v)

            visited.add(u)
        return False

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            u = s.pop()

            if u == destination_vertex:
                return True

            for v in self.vertices[u]:
                if v not in visited:
                    s.push(v)

            visited.add(u)

    def bfs_path(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            path = q.dequeue()

            if path[-1] == destination_vertex:
                return path

            for v in self.vertices[path[-1]]:
                if v not in visited:
                    new_path = list(path)
                    new_path.append(v)
                    q.enqueue(new_path)

            visited.add(path[-1])

        return -1

    def dfs_path(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()

            if path[-1] == destination_vertex:
                return path

            for v in self.vertices[path[-1]]:
                if v not in visited and v not in s.stack:
                    new_path = list(path)
                    new_path.append(v)
                    s.push(new_path)

            visited.add(path[-1])

        return -1


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs_path(1, 6))
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs_path(1, 6))
    print(graph.dfs(1, 6))
