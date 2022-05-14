import numpy as np

def connect_all_vertices(robots, obstacles, adjacency_matrix):
    for i in range (len(robots)):
        for j in range (len(robots)):
            if i != j:
                adjacency_matrix[i][j] = distance(robots[i], robots[j])
    for i in range (len(robots), len(obstacles)+len(robots)):
        for j in range (len(robots), len(obstacles)+len(robots)):
            if i != j:
                adjacency_matrix[i][j] = distance(obstacles[i - len(robots)], obstacles[j - len(robots)])
    for i in range (len(robots)):
        for j in range (len(robots), len(obstacles) + len(robots)):
            adjacency_matrix[i][j] = distance(robots[i], obstacles[j - len(robots)])
            adjacency_matrix[j][i] = distance(robots[i], obstacles[j - len(robots)])
    return adjacency_matrix
    
def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
