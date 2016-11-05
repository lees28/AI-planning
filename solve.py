# implements the graph coloring algorithm

from graph import Graph
import copy

class Solve:

    def __init__(self,graph,colors):
        self.graph = graph
        self.colors = colors


    "helper method to determine if two assignments are valid"
    def m_valid(self,one,two,color1,color2):
        graph=self.graph
        if graph.connected(one,two):
            if color1== color2:
                return False
            else:
                return True
        else:
            return True

    def solve(self):
        assignment = []
        'your implementation goes here: return a valid assignment, or an empty array if there is no feasible (valid) assignment'

        # a) check whether there exists a feasible coloring using the path consistency algorithm
        #    output "Feasible" if there is a feasible coloring and "Infeasible" if there is no feasible coloring
        # b) compute a coloring of the graph using the specified colors, or return "Infeasible" if no feasible coloring exists
        graph = self.graph
        colors = self.colors
        valid=[]
        "make a tmp list of all possible color assignments given a color list"
        for i in range(len(colors)):
            for j in range(len(colors)):
                tmp = [0, 0]
                tmp[0] = colors[i]
                tmp[1] = colors[j]
                valid.append(tmp)

        for i in range(graph.getNumNodes()):
            for j in range(i+1,graph.getNumNodes()):
                "for every element in the assign list"
                for k in range(len(valid)):
                    "check whether the assignment is valid on node i and node j"
                    if self.m_valid(i,j,valid[k][0],valid[k][1]):
                        for l in range(j+1,graph.getNumNodes()):
                            color=copy.deepcopy(colors)
                            for m in range(len(colors)):
                                "check whether there is a color assignment to node l satisfies constraints on (nodei,node l) and (node j and node l)"
                                if not((self.m_valid(i,l,valid[k][0],colors[m])
                                       and self.m_valid(j,l,valid[k][1],colors[m]))):
                                    color.remove(colors[m])
                            if len(color)==0:
                                return []
        return [1]
