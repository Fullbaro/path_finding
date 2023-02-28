from math import radians, sin, cos, sqrt, atan2
import heapq
from matplotlib import pyplot as plt

class A_star:

    def __init__(self, map):
        self.map = map
        self.graph = map.graph
        self.path = []

    # Haversine formula for calculating distance between two geographic coordinates
    def haversine(self, coord1, coord2):
        R = 6371  # radius of the Earth in kilometers

        lat1, lon1 = coord1[0], coord1[1]
        lat2, lon2 = coord2[0], coord2[1]

        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)

        a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return R * c

    # A* path finding algorithm
    def find_path(self, start: tuple, goal: tuple):
        if start not in self.graph:
            raise ValueError("Start not in graph")
        if goal not in self.graph:
            raise ValueError("Goal not in graph")

        frontier = [(0, start)]
        came_from = {}
        cost_so_far = {start: 0}

        while frontier:
            _, current = heapq.heappop(frontier)

            if current == goal:
                break

            for neighbor, cost in self.graph[current]:
                new_cost = cost_so_far[current] + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.haversine(neighbor, goal)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

        if goal not in came_from: # There is no path
            self.path = []
            return self.path

        path = [goal]
        current = goal

        while current != start:
            current = came_from[current]
            path.append(current)


        self.path = path[::-1]
        return self.path


    def visualize(self):
        w = 10
        h = 60

        plt.rcParams["figure.figsize"] = [w, h]
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams['axes.facecolor'] = 'black'

        plt.scatter(x=[key[0] for key, _ in self.graph.items()], y=[key[1] for key, _ in self.graph.items()],  color='gray', s=1, marker='o',) # Available paths
        plt.scatter(x=[point[0] for point in self.map.obsticles], y=[point[1] for point in self.map.obsticles],  color='red', s=10, marker="X") # Obscticles
        plt.scatter(x=[coord[0] for coord in self.path], y=[coord[1] for coord in self.path],  color='yellow', s=5, marker='o',) # Path


        plt.show()