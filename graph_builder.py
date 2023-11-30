from collections import defaultdict
from queue import Queue
import random
import heapq
from time import time

class Graph:

    def __init__(self, file_path, timeout):
        self.path = file_path
        self.graph = defaultdict(list) # adjacency list
        self.keys = []
        self.timeout = timeout

    def build(self):
        print("Building graph...")
        with open(self.path) as f:
            edges = f.readlines()
        for edge in edges:
            from_vertex, to_vertex = edge.split() # unpack from and to from edge list item
            from_vertex = int(from_vertex)
            to_vertex = int(to_vertex)
            self.graph[from_vertex] += [to_vertex] # concatenate to adjacency list element
            self.keys.append(from_vertex)

    def get_rand_user(self):
        return random.choice(self.keys)
    
    def bfs(self, start, end):
        start_time = time()
        q = Queue()
        visited = set()
        q.put((start, 0)) # (current_vertex, num_steps_taken)
        while not q.empty():
            if self.timeout is not None and time() - start_time > self.timeout:
                raise TimeoutError
            current_vertex, num_steps_taken = q.get()
            visited.add(current_vertex)
            if current_vertex == end:
                end_time = time()
                return num_steps_taken, end_time - start_time
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    q.put((neighbor, num_steps_taken + 1))
        end_time = time()
        return -1, end_time - start_time # not found
    
    def dijkstra(self, start, end):
        start_time = time()
        priority_q = [(0, start)] # (current_vertex, num_steps_taken)
        inf_float = lambda: float("inf") # function that initializes a float to infinity
        distances = defaultdict(inf_float) # we don't need to maintain the predecessor as we are not reconstructing the path
        distances[start] = 0
        while priority_q:
            if self.timeout is not None and time() - start_time > self.timeout:
                raise TimeoutError
            num_steps_taken, current_vertex = heapq.heappop(priority_q) # get the next node with the shortest distance (this works because in tuple comparisons the first element is compared)
            if current_vertex == end:
                break # preemptively terminate dijkstra's as we don't need the distances for other nodes
            for neighbor in self.graph[current_vertex]:
                new_steps = num_steps_taken + 1
                if new_steps < distances[neighbor]:
                    distances[neighbor] = new_steps
                    heapq.heappush(priority_q, (new_steps, neighbor))
        dist = -1 if distances[end] == float("inf") else distances[end]
        end_time = time()
        return dist, end_time - start_time