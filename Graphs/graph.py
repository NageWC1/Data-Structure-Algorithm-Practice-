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

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dec:
            return []
        
        paths = []

        for node in self.graph_dec[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

    def shortest_path(self,start,end,path=[]):
        path = path + [start]
        if start not in self.graph_dec:
            return None
        
        if start == end:
            return path
        
        shortest_path = None
        for node in self.graph_dec[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path
                
if __name__ == "__main__":
    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto"),
    ]

    # starting and ending is same
    # start = "Mumbai"
    # end = "Mumbai"

    # there is no flight from toronto - check this case 
    # start = "Toronto"
    # end = "Mumbai"

    # check whether possible paths between 2 distinations
    start = "Mumbai"
    end = "New York"

    # check whether shortest path
    start_ = "Mumbai"
    end_ = "New York"

    route_graph = Graph(routes)
    print(f"Route between {start} and {end}:",route_graph.get_paths(start,end))
    print()
    print(f"Route between {start_} and {end_}:",route_graph.shortest_path(start,end))