from graph_builder import Graph

if __name__ == "__main__":
    graph = Graph("twitter_combined.txt")
    graph.build()
    dist = graph.bfs(
        graph.get_rand_user(),
        graph.get_rand_user()
    )
    print(dist)