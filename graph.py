# Graphs can be implemented using an adjacency list or an adjacency matrix. 
# Graphs are either directed or undirected; the way they are implemented determines how this is handled

class Neighbor: 
    def __init__(self, name, weight) :
        self.name = name
        self.weight = weight
    def __repr__(self) :
        return "({}, {})".format(self.name, self.weight)
class Node :
    def __init__(self, name, neighbors=[]) : # augment with more attributes ad hoc
        self.name = name # name is included for simplicity. In more comprehensive implementation, it would be better to generate IDs so names of nodes can be changed
        self.neighbors = neighbors
    def is_neighbor(self, name_of_other_node) :
        for neighbor in self.neighbors :
            if neighbor.name == name_of_other_node : return True
        return False
    def get_neighbor_weight(self, name_of_other_node) :
        for neighbor in self.neighbors :
            if neighbor.name == name_of_other_node : return neighbor.weight
        return False
    def change_neighbor_weight(self, name_of_other_node, new_weight) :
        for neighbor in self.neighbors :
            if neighbor.name == name_of_other_node : 
                neighbor.weight = new_weight
                return True
        return False



class AL_Graph :
    def __init__(self, graph={}, directed=True) :
        self.graph = graph
        self.directed = directed
    
    def __repr__(self) :
        if len(self.graph) == 0:
            return '{EMPTY GRAPH}'
        else :
            rep = "-------\n"

            for node_name, node in self.graph.items():
                rep += "{} -> {}\n".format(node_name, node.neighbors)

            rep += "-------"
            return rep

    def add_node(self, name, new_neighbors=False) :
        '''
        Adds a vertex to the graph, including the list of the vertices it points to. Edges are mirrored if undirected
        '''
        if not new_neighbors : new_neighbors = list()
        self.graph[name] = Node(name, new_neighbors)

        if not self.directed :
            for neighbor in new_neighbors :
                #match weight of neighboors to its weight
                neighbor_node = self.graph[neighbor.name]
                neighbor_node.neighbors.append(Neighbor(name, neighbor.weight))

    def add_neighbor(self, node_name, neighbor_name, neighbor_weight) : 
        '''
        Takes a vertex and makes anther vertex it's neighbor. If the second node is already it's neighbor, it simply updates the weight
        '''
        node = self.graph[node_name]

        if not node.change_neighbor_weight(neighbor_name, neighbor_weight) :
            new_neighbor = Neighbor(neighbor_name, neighbor_weight)
            self.graph[node_name].neighbors.append(new_neighbor)
    
        neighbor = self.graph[neighbor_name]

        if not self.directed and not neighbor.change_neighbor_weight(node_name, neighbor_weight):
            new_neighbor = Neighbor(node_name, neighbor_weight)
            neighbor.neighbors.append(new_neighbor)
                    
    #implemented using Djjkstra's algorithm
    def cheapest_path(self, start_node, goal_node) :
        visited = {}
        unvisited = {vertex_name:[float('inf'), start_node] for vertex_name in self.graph.keys()}
        unvisited[start_node][0] = 0

        def get_cheapest_so_far() :
            cheapest_path, lowest_cost = None, float('inf')
            for name, cost_and_path in unvisited.items():
                if cost_and_path[0] < lowest_cost:
                    cheapest_path = name
                    lowest_cost = cost_and_path[0]

            return cheapest_path, lowest_cost

        while goal_node in unvisited or bool(unvisited) :
            curnode, cost = get_cheapest_so_far()

            for neighbor in filter(lambda n: n.name in unvisited, self.graph[curnode].neighbors) :
                if cost + neighbor.weight < unvisited[neighbor.name][0] :
                    unvisited[neighbor.name][0] = cost + neighbor.weight
                    unvisited[neighbor.name][1] = unvisited[curnode][1] + ' -> ' + neighbor.name
            
            visited[curnode] = unvisited.pop(curnode)
        return visited[goal_node][0], visited[goal_node][1]
           
# TEMPLATE GRAPH
# CCgraph = AL_Graph(directed=False)
# CCgraph.add_node('Winterfall')
# CCgraph.add_node('Pyke')
# CCgraph.add_node('Riverrun')
# CCgraph.add_node('The Trident')
# CCgraph.add_node('Kings Landing')
# CCgraph.add_node('Highgarden')
# CCgraph.add_neighbor('Winterfall', 'Pyke', 18)
# CCgraph.add_neighbor('Winterfall', 'The Trident', 10)
# CCgraph.add_neighbor('Pyke', 'Highgarden', 14)
# CCgraph.add_neighbor('The Trident', 'Kings Landing', 5)
# CCgraph.add_neighbor('Kings Landing', 'Highgarden', 8)
# CCgraph.add_neighbor('Riverrun', 'The Trident', 2)
# CCgraph.add_neighbor('Riverrun', 'Pyke', 3)
# CCgraph.add_neighbor('Riverrun', 'Highgarden', 10)
# CCgraph.add_neighbor('Riverrun', 'Kings Landing', 25)
