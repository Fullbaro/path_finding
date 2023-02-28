from map import Map
from num import Num
import random
from path_finder import A_star
from timer import Timer

step_size = Num(0.000001)
x_min = Num(46.770698)
y_min = Num(17.242968)
x_max = Num(46.770902)
y_max = Num(17.243393)

# Generate
# M = Map(x_min, y_min, x_max, y_max, step_size)
# M.generate()
# for i in range(150): # Add random obstocles
#     M.add_obsticle(random.choice(list(M.graph.keys())))
# M.save()


# OR load from save
M = Map().load()



# Find path
A = A_star(M)
t = Timer()
p = A.find_path((x_min, y_min), (x_max, y_max))
t.stop("Finding path")



A.visualize()
