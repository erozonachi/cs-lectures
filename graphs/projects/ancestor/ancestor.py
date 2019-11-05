class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


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
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)

        self.vertices[v1].add(v2)

    def get_strict_parents(self):
        keys = list(self.vertices.keys())

        for key in range(1, len(keys)+1):
            for i in self.vertices:
                if key in self.vertices[i]:
                    keys.remove(key)
                    break

        return keys

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

        return []

    def get_earliest_ancestor(self, child_node):
        ancestors = self.get_strict_parents()

        if child_node in ancestors:
            return -1

        path = []

        for ancestor in ancestors:
            temp = self.dfs_path(ancestor, child_node)
            if len(temp) > 0 and len(path) < len(temp):
                path = temp
        if len(path) > 0:
            return path[0]

        return -1


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for val_set in ancestors:
        graph.add_edge(val_set[0], val_set[1])

    return graph.get_earliest_ancestor(starting_node)
