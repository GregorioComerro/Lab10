import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()

    def buildGraph(self, anno):
        self._graph.clear()

        nodes = DAO.getAllNodes(anno)
        edges = DAO.getAllEdges(anno)

        self._graph.add_nodes_from(nodes)
        self._graph.add_edges_from(edges)

    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return len(self._graph.edges)

    def getGradi(self):
        result = []

        for stato in self._graph.nodes:
            grado = self._graph.degree[stato]
            result.append((stato, grado))

        result.sort(key=lambda x: x[0].StateNme)
        return result

    def getNumComponentiConnesse(self):
        return nx.number_connected_components(self._graph)

    def getAllNodes(self):
        result = list(self._graph.nodes)
        result.sort(key=lambda x: x.StateNme)
        return result
