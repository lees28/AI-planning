

from graph import Graph

class Solve:

    def __init__(self,graph,colors):
        self.graph = graph
        self.colors = colors

    def solve(self):
        assignment = []
        graph = self.graph
        colors = self.colors
        for i in range(graph.getNumNodes()):
            for j in range(i,graph.getNumNodes()):
                for k in range(j,graph.getNumNodes()):
                    if graph.connected(i,j) and graph.connected(i,k) and graph.connected(j,k):
                        if len(colors)<3:
                            return []

                        else:
                            return [1]
        return [1]


for i in range(len(colors) ^ 2):
    tmp = [0, 0]
    for j in range(len(colors)):
        for k in range(len(colors)):
            tmp[0] = colors[j]
            tmp[1] = colors[k]
            valid.append(tmp)
            tmp = [0, 0]
print valid

invalid = []
for i in range(len(colors)):
    tmp[0] = colors[i]
    tmp[1] = colors[i]
    invalid.append(tmp)
    tmp = [0, 0]
print invalid