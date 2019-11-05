
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

        for key in range(1, keys+1):
            for i in self.vertices:
                if key in self.vertices[i]:
                    keys.remove(key)
                    break

        return keys


def earliest_ancestor(ancestors, starting_node):
    pass
