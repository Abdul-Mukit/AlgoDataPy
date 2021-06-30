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
        if node1 in self.adjacentList.keys() and node2 in self.adjacentList.keys():
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)
            print("Added edge: {}".format([node1,node2]))
            return True
        else:
            print("Error: node(s) {} don't exists".format([node1, node2]))
            return False

myGraph = MyGraph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')

myGraph.add_edge('3', '1');
myGraph.add_edge('3', '4');
myGraph.add_edge('4', '2');
myGraph.add_edge('4', '5');
myGraph.add_edge('1', '2');
myGraph.add_edge('1', '0');
myGraph.add_edge('0', '2');
myGraph.add_edge('6', '5');


print(myGraph)