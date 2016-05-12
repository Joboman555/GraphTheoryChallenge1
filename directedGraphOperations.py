from readGraph import readGraph
infinity = float("inf")

def eccentricities(graph):
    """Calculates the eccentricity of each node"""
    ecc = lambda node: eccentricity(node, graph)
    notZero = lambda n: n != 0

    # Eccentricity of a node connected to nothing will be zero.
    # The radius only counts connected pathways, so we will discard
    # These zeroes.
    eccentricities = filter(notZero, map(ecc, graph))
    return eccentricities


def eccentricity(node, graph):
    """The greatest distance from a node in a graph to any other node"""
    dist = lambda distanceNode: distance(node, distanceNode, graph)
    notInf = lambda dist: dist != infinity

    # Distance of a node connected to nothing will be infinity.
    # Eccentricity only counts connected pathways, so we will discard
    # These infinities.
    distances = filter(notInf, map(dist, graph))
    return max(distances)


def distance(sourceNode, destinationNode, graph):
    """calculates the distance from one node in a graph to another"""
    if destinationNode not in graph:
        raise IndexError("Node " + str(destinationNode) + " Not in Graph")
    if sourceNode not in graph:
        raise IndexError("Node " + str(sourceNode) + " Not in Graph")

    if sourceNode == destinationNode:
        return 0

    adjacentNodes = graph[sourceNode]
    if destinationNode in adjacentNodes:
        return 1
    if not adjacentNodes:
        return infinity
    distances = []
    for adjacentNode in adjacentNodes:
        distances.append(1 + distance(adjacentNode, destinationNode, graph))
    return min(distances)


if __name__ == "__main__":
    # Our Directed Graph is represented as a dictionary with the
    # keys being the source nodes and the values being a list of
    # destination nodes.
    graph = readGraph('testInput.txt')
    eccs = eccentricities(graph)
    print("")
    # Radius is the smallest eccentricity
    print("Raidus: " + str(min(eccs)))
    # Diameter is the largest eccentricity
    print("Diameter: " + str(max(eccs)))
    print("")
