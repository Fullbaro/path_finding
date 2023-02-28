from num import Num
import pickle
import math

class Map:

    def __init__(self, x_min: Num=0.0, y_min: Num=0.0, x_max: Num=0.0, y_max: Num=0.0, step_size: Num=0.000001):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.step_size = step_size

        self.graph = {}
        self.obsticles = []

    # Generate the full geographical coordinate system
    def generate(self):
        x = self.x_min
        while x <= self.x_max:
            y = self.y_min
            while y <= self.y_max:
                self.neighbors(x, y)
                self.graph[(x, y)] = self.neighbors(x, y)
                y += self.step_size
            x += self.step_size

    # Return the neighbors of a coordinate in a radius
    def neighbors(self, x: float, y: float, radius: int=1):
        check_next_node = lambda x, y: True if self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max else False # Embeded function

        ways = []
        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                if i == 0 and j == 0:
                    continue
                distance = math.sqrt(i**2 + j**2)
                if distance < radius or radius == 1:
                    ways.append([self.step_size * i, self.step_size * j])

        return [((x + dx, y + dy), 1) for dx, dy in ways if check_next_node(x + dx, y + dy)]

    # Add obsticle to map = remove node
    def add_obsticle(self, node_to_remove):
        all_node_to_remove = self.neighbors(Num(node_to_remove[0]), Num(node_to_remove[1]), 5)
        all_node_to_remove.append(((node_to_remove), None))
        self.obsticles.append(node_to_remove) # display only obsticle
        for ntr in all_node_to_remove:
            ntr = ntr[0]
            #self.obsticles.append(ntr) # display neigbors

            # Remove any paths that include the removed node
            for node, paths in self.graph.items(): # TODO Csak a szomszédait nézze, ne az egész gráfot
                paths_to_remove = [path for path in paths if ntr in path]
                for path in paths_to_remove:
                    paths.remove(path)

            try:
                # Remove the removed node from the dictionary
                del self.graph[ntr]
            except:
                pass # Already removed

    # Saves the Map class and it's state to file
    def save(self):
        with open('./assets/map.pkl', 'wb') as file:
            pickle.dump(self, file, pickle.HIGHEST_PROTOCOL)

    # Loads the Map class and it's state from file
    @staticmethod
    def load():
        with open('./assets/map.pkl', 'rb') as file:
            return pickle.load(file)