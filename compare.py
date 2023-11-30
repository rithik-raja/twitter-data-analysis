from graph_builder import Graph
from display import draw_tbl
import argparse

def main():

    parser = argparse.ArgumentParser(
        description="A program to run BFS and Dijkstra's Search on Twitter social circle data to determine the shortest path between 2 users in terms of who follows who."
    )
    parser.add_argument(
        "--from-node",
        type=int,
        help="User ID of start node"
    )
    parser.add_argument(
        "--to-node",
        type=int,
        help="User ID of end node"
    )
    parser.add_argument(
        "-i",
        "--iterations",
        type=int,
        default=1,
        help="Number of times both of the algorithms are compared"
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        help="Maximum execuation time in seconds per search"
    )
    parser.add_argument(
        "--ignore-bfs",
        action="store_true",
        help="Whether to omit BFS"
    )
    parser.add_argument(
        "--ignore-dijkstra",
        action="store_true",
        help="Whether to omit Dijkstra's"
    )
    args = parser.parse_args()

    graph = Graph("twitter_combined.txt", timeout=args.timeout)
    graph.build()

    results = [
        ["Run no.", "From", "To", "Shortest Distance (BFS)", "Shortest Distance (Dijkstra's)", "BFS Runtime", "Dijkstra's Runtime", "Ratio"]
    ]
    ratio_sum = 0
    i = 0
    while i < args.iterations:
        try:
            print(f"Running iteration {i + 1}...")
            from_node = args.from_node if args.from_node is not None else graph.get_rand_user() # use source node if specified else random node
            to_node = args.to_node if args.to_node is not None else graph.get_rand_user() # use destination node if specified else random node
            dist, time_delta = graph.bfs(from_node, to_node) if not args.ignore_bfs else (float("nan"), float("nan")) # append nan if bfs ignored
            dist_2, time_delta_2 = graph.dijkstra(from_node, to_node) if not args.ignore_dijkstra else (float("nan"), float("nan")) # append nan if dijkstra ignored
            results.append([
                i + 1,
                from_node,
                to_node,
                dist,
                dist_2,
                time_delta,
                time_delta_2,
                time_delta / time_delta_2
            ])
            ratio_sum += time_delta / time_delta_2
            i += 1
        except TimeoutError:
            print("Timed out. Trying again...")

    print()
    draw_tbl(results)
    print()

    ratio_avg = ratio_sum / args.iterations
    if not args.ignore_bfs and not args.ignore_dijkstra:
        print(f"On average, BFS is {ratio_avg} times {'slower' if ratio_avg > 1 else 'faster'} than Dijkstra's.\n")


if __name__ == "__main__":
    main()