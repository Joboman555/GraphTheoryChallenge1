

def readGraph(fileName):
    with open('testInput.txt', 'r') as file:
        # The first line of the file indicates the length of the file.
        # Since we are using a for loop, we do not need to know the length.
        graphSize = int(file.readline())

        # Python indices start at 0, but our graph node ID's start at 1
        # So we add 1 to each id.
        graph = {k + 1: [] for k in range(graphSize)}
        for line in file:
            sourceNode = int(line[0])
            destinationNode = int(line[2])
            graph[sourceNode].append(destinationNode)
        return graph

if __name__ == "__main__":
    print(readGraph('testInput.txt'))
