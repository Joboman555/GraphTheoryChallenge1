

def readGraph(fileName):
    with open(fileName, 'r') as file:
        # The first line of the file indicates the length of the file.
        # Since we are using a for loop, we do not need to know the length.
        numLines = int(file.readline())

        connections = []
        IDs = []
        for line in file:
            sourceNode, destinationNode = map(int, line.split())
            connections.append((sourceNode, destinationNode))
            # The largest ID will give us the graph size
            if sourceNode not in IDs:
                IDs.append(sourceNode)
            if destinationNode not in IDs:
                IDs.append(destinationNode)

        maxID = max(IDs)
        # Python indices start at 0, but our graph node ID's start at 1
        # So we add 1 to each id.
        graph = {k + 1: [] for k in range(maxID)}
        for sourceNode, destinationNode in connections:
            graph[sourceNode].append(destinationNode)
        return graph

if __name__ == "__main__":
    print(readGraph('challengeInput.txt'))
