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
    distance = 0
    sourceNodes = [sourceNode]
    while True:
        distance += 1
        nextNodes = []
        # print(sourceNodes)
        for sourceNode in sourceNodes:
            if destinationNode not in graph:
                raise IndexError("Node " + str(destinationNode) + " Not in Graph")
            if sourceNode not in graph:
                raise IndexError("Node " + str(sourceNode) + " Not in Graph")

            if sourceNode == destinationNode:
                return 0

            adjacentNodes = graph[sourceNode]
            if destinationNode in adjacentNodes:
                return distance

            nextNodes += adjacentNodes
        # Make sure we aren't in an infinite loop
        if sourceNodes == list(set(nextNodes)):
            return infinity
        # Only get unique nodes
        sourceNodes = list(set(nextNodes))


if __name__ == "__main__":
    # Our Directed Graph is represented as a dictionary with the
    # keys being the source nodes and the values being a list of
    # destination nodes.
    graph = readGraph('challengeInput.txt')
    eccs = eccentricities(graph)

    print("")
    # Radius is the smallest eccentricity
    print("Raidus: " + str(min(eccs)))
    # Diameter is the largest eccentricity
    print("Diameter: " + str(max(eccs)))
    print("")
