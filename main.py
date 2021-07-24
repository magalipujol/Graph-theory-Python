# %%
vertices = {'a', 'b', 'c', 'd'}
edges = set([('a', 'b'), ('c', 'a'), ('d', 'b'), ('d', 'c')])

# %%


class Graph:
    def __init__(self, vertices: set, edges: set) -> None:
        self.vertices = vertices
        self.edges = edges
        assert(self.edgesConsistency())

    def edgesConsistency(self):
        for edge in self.edges:
            if edge[0] not in vertices or edge[1] not in self.vertices:
                print(f'This edge iw wrong :( {edge}')
                return False
        return True

    def neighboursVertex(self, vertex):
        neighbours = set()
        for edge in self.edges:
            if vertex == edge[0]:
                neighbours.add(edge[1])
            if vertex == edge[1]:
                neighbours.add(edge[0])
        return neighbours
    
    def addVertex(self, vertex):
        self.vertices.add(vertex)
    
    def addEdge(self, edge):
        assert(edge[0] not in vertices or edge[1] not in self.vertices)
        self.edges.add(edge)
    
    def removeVertex(self, vertex):        
        self.vertices.discard(vertex)
        edgesToRemove = []
        for edge in self.edges:
            if edge[0] == vertex or edge[1] == vertex:
                edgesToRemove.append(edge)     
        for edge in edgesToRemove:
            self.edges.remove(edge)
               
    def removeEdge(self, edge):
        self.vertices.discard(edge)
# %%
graph = Graph(vertices, edges)

# %%
assert(graph.neighboursVertex('a') == {'b', 'c'})
# %%
print(graph.vertices)
print(graph.edges)

# %%
graph.removeVertex('a')

# %%
print(graph.vertices)
print(graph.edges)

# %%
