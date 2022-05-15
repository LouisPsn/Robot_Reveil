from obstacle import *
from LoadData import *
from graph import *
import numpy as np
# import matplotlib.pyplot 
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
np.set_printoptions(precision=3, linewidth=200)

def main():
    RobotStart, RobotCoords, Obstacles, Edges = load_data("data.txt")
    #reformating of obstacles and robots to be able to connect them
    obstacles = format_obstacles(Obstacles)
    robots = []
    robots.append(RobotStart)
    for i in range (len(RobotCoords)):
        robots.append(RobotCoords[i])

    #initializing adjacency matrix
    nb_vertices = len(robots) + len(obstacles)
    adjacency_matrix = np.zeros([nb_vertices, nb_vertices])
    adjacency_matrix = connect_all_vertices(robots, obstacles, adjacency_matrix)
    #display_graph(adjacency_matrix, robots, obstacles)
    adjacency_matrix = remove_edges_intersecting(adjacency_matrix, robots, obstacles)
    display_graph(adjacency_matrix, robots, obstacles)
    
    return 0

main()