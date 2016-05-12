# Our Directed Graph is represented as a dictionary with the
# keys being the source nodes and the values being a list of
# destination nodes.

infinity = float("inf")

def eccentricity(node, graph):
    """The greatest distance from a node in a graph to any other node"""
    dist = lambda distanceNode: distance(node, distanceNode, graph)
    distances = map(dist, graph)
    filteredDistances = filter(lambda dist: dist != infinity, distances)
    return max(filteredDistances)


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
    testNodes = {1: [2, 3], 2: [1], 3: []}
    print(eccentricity(3, testNodes))
