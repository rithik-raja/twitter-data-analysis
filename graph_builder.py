from collections import defaultdict
from queue import Queue
import random

class Graph:

    def __init__(self, file_path):
        self.path = file_path
        self.graph = defaultdict(list) # adjacency list
        self.keys = []

    def build(self):
        with open(self.path) as f:
            edges = f.readlines()
        for edge in edges:
            from_vertex, to_vertex = edge.split() # unpack from and to from edge list item
            from_vertex = int(from_vertex)
            to_vertex = int(to_vertex)
            self.graph[from_vertex] += [to_vertex] # concatenate to adjacency list element
            self.keys.append(from_vertex)
        print(len(self.graph))

    def get_rand_user(self):
        return random.choice(self.keys)
    
    def bfs(self, start, end):
        q = Queue()
        visited = set()
        q.put((start, 0)) # (current_vertex, num_steps_taken)
        while not q.empty():
            current_vertex, num_steps_taken = q.get()
            visited.add(current_vertex)
            if current_vertex == end:
                return num_steps_taken
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    q.put((neighbor, num_steps_taken + 1))
        return -1 # not found