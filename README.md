# Graph Radius and Diameter Challenge

An introductory graph theory challenge taken from [/r/dailyprogrammer](https://www.reddit.com/r/dailyprogrammer/)'s [Challenge #266](https://www.reddit.com/r/dailyprogrammer/comments/4iut1x/20160511_challenge_266_intermediate_graph_radius/?ref=share&ref_source=link)
The challenge description is as follows:
## Description
Graph theory has a relatively straightforward way to calculate the size of a graph, using a few definitions:
* The eccentricity ecc(v) of vertex (aka node) v in graph G is the greatest distance from v to any other node.
* The radius rad(G) of G is the value of the smallest eccentricity.
* The diameter diam(G) of G is the value of the greatest eccentricity.
* The center of G is the set of nodes v such that ecc(v)=rad(G).

So, given a graph, we can calculate its size.

## Input Description


You'll be given a single integer on a line telling you how many lines to read, then a list of n lines telling you nodes of a directed graph as a pair of integers. Each integer pair is the source and destination of an edge. The node IDs will be stable. 
Example:
```
3
1 2
1 3
2 1
```

## Output Description
