An example program using the **A*** path finding algorithm with **geographic coordinates.** Coordinates can be used to define an area, place obstacles on it, and then the algorithm calculates the shortest path between two points. 

This module can be used for example for GPS based waypoint mission vehicles

# Example:
Define a geographical bounding box

    step_size = Num(0.000001) # Precision
    x_min = Num(46.770698)
    y_min = Num(17.242968)
    x_max = Num(46.770902)
    y_max = Num(17.243393)
 
 Generate map and place obstacles

    M = Map(x_min, y_min, x_max, y_max, step_size)
    M.generate()
    for i in range(150): # Add random obstacles
        M.add_obsticle(random.choice(list(M.graph.keys())))

Save or load map    

    M.save()     
    M = Map().load()
    
    
    
Run path finder

    A = A_star(M)
    p = A.find_path((x_min, y_min), (x_max, y_max)) 
    A.visualize()


