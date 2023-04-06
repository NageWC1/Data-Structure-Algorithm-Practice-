class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dec = {}

        for start, end in self.edges:
            # if the key is already in the dectionary 
            if start in self.graph_dec:
                self.graph_dec[start].append(end)
            else:
                self.graph_dec[start] = [end]
        print("The dictionary is:",self.graph_dec)

if __name__ == "__main__":
    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto"),
    ]

    route_graph = Graph(routes)