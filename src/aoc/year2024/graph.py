#aoc.year2024.graph

class DirectedGraph:

    def __init__(self):
        self.dict = {}

    def add_path(self, start_node, end_node):
        if start_node in self.dict.keys():
            self.dict[start_node].append(end_node)
        else:
            self.dict[start_node] = [ end_node ]
        if end_node not in self.dict.keys():
            self.dict[end_node] = []

    def get_out_nodes(self, node):
        if node in self.dict.keys():
            return self.dict[node]

    def print(self):
        node_list = list(self.dict.keys())
        node_list.sort()
        for node in node_list:
            out_nodes = self.get_out_nodes(node)
            out_nodes.sort()
            print(f"{node}:{out_nodes}")