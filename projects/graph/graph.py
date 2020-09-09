"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex hasn't been appended")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def remove_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices and v2 in self.vertices[v1]:
            self.vertices[v1].remove(v2)
        else: 
            raise IndexError("Vertices are not neighbors")

    def bft(self, starting_vertex):
        # init
        q = Queue()
        q.enqueue(starting_vertex)

        #set for visited nodes
        has_been_visited = set()

        #ensure the queue is not empty
        while q.size() > 0:
            # dequeue, add value to 'has_been_visited', apppend neighbors that aren't visited
            v = q.dequeue()

            if v not in has_been_visited:
                has_been_visited.add(v)
                print(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        #init
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        #ensure stack is not empty
        while s.size() > 0:
            #if not pop node, append to visited, add neighbors that arent'visited (like BFT)
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)



    def dft_recursive(self, vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None: 
            visited = []
        visited.append(vertex)
        # add neighbors to visited list if not already visited
        for neighbor in self.get_neighbors(vertex):
            if neighbor not in visited:
                visited = self.dft_recursive(neighbor, visited)
        return visited

    def bfs(self, start, target):

        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # init Q [start]
        q = Queue()
        q.enqueue([start])
        
        visited = list()
        # ensure q is not empty
        while q.size() > 0:
            v = q.dequeue()
            #last node in path
            node = v[-1]
            if node not in visited:
                for neighbor in self.get_neighbors(node):
                    path = list(v)
                    # enqueue list of path to neighbors ([start, 2], [start, 3], etc)
                    path.append(neighbor)
                    q.enqueue(path)
                # return path if neighbor is target
                    if neighbor == target:
                        return path
                visited.append(node)
        

    def dfs(self, start, target):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([start])

        visited = list()

        while s.size() > 0:
            v = s.pop()
            #find last
            node = v[-1]

            if node not in visited:
                for neighbor in self.get_neighbors(node):
                    path = list(v)
                    # appened list of neighbors 
                    path.append(neighbor)
                    s.push(path)

                    if neighbor == target:
                        return path # return path if neighbor is target
                visited.append(node)

    def dfs_recursive(self, start, target, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path == None:
            path = []
        if visited == None:
            visited = []

        # recurse time
        visited.append(start)

        path = path + [start]

        # case 1
        if start == target:
            return path

        # else
        for neighbor in self.get_neighbors(start):
            if neighbor not in visited:
                #recurse
                new_path = self.dfs_recursive(neighbor, target, visited, path)
                if new_path is not None:
                    return new_path
        # other wise
        return None


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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
