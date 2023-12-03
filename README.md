# Twitter Data Analysis

A program to run BFS and Dijkstra's Search on Twitter social circle data to determine the shortest path between 2 users in terms of who follows who.
- Clone the repository
- Run `python compare.py` with the desired flags

### Usage:

```
compare.py [-h] [--from-node FROM_NODE] [--to-node TO_NODE] [-i ITERATIONS] [-t TIMEOUT] [--ignore-bfs] [--ignore-dijkstra]

options:
  -h, --help            show this help message and exit
  --from-node FROM_NODE
                        User ID of start node
  --to-node TO_NODE     User ID of end node
  -i ITERATIONS, --iterations ITERATIONS
                        Number of times both of the algorithms are compared
  -t TIMEOUT, --timeout TIMEOUT
                        Maximum execuation time in seconds per search
  --ignore-bfs          Whether to omit BFS
  --ignore-dijkstra     Whether to omit Dijkstra's
```

The dataset was downloaded from [here](https://snap.stanford.edu/data/ego-Twitter.html).
