class MyGraph():
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def __str__(self):
        return str(self.__dict__)

    def add_vertex(self, node):
        if node not in self.adjacentList.keys():
            self.adjacentList[node] = []
            self.numberOfNodes += 1
            print("Added new node: {}".format(node))
            return True
        else:
            print("Failed to add node, as node already exists")
            return False

    def add_edge(self, node1, node2):
        print("Not implemented exception")

    def show_connections(self):
        print("Not implemented exception")

myGraph = MyGraph()
myGraph.add_vertex(0)
myGraph.add_vertex(1)
myGraph.add_vertex(0)
print(myGraph)