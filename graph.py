from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

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

def display_graph(adjacency_matrix, robots, obstacles):
    plt.figure(figsize=(10,10))
    for k in range(len(robots)):
        plt.plot(robots[k][0], robots[k][1], 'rx')
    for k in range(0, len(obstacles), 4):
        obs_x = [obstacles[k][0], obstacles[k+1][0], obstacles[k+2][0], obstacles[k+3][0], obstacles[k][0]]
        obs_y = [obstacles[k][1], obstacles[k+1][1], obstacles[k+2][1], obstacles[k+3][1], obstacles[k][1]]
        plt.plot(obs_x, obs_y, '-bo')
    for i in range(len(robots)):
        for j in range(len(robots)):
            if adjacency_matrix[i][j] != 0:
                plt.plot([robots[i][0], robots[j][0]], [robots[i][1], robots[j][1]], '-k')
    for i in range(len(robots), len(robots)+len(obstacles)):
        for j in range(len(robots), len(robots)+len(obstacles)):
            if adjacency_matrix[i][j] != 0:
                plt.plot([obstacles[i - len(robots)][0], obstacles[j - len(robots)][0]], [obstacles[i - len(robots)][1], obstacles[j - len(robots)][1]], '-k')
    for i in range(len(robots)):
        for j in range(len(robots), len(robots)+len(obstacles)):
            if adjacency_matrix[i][j] != 0:
                plt.plot([robots[i][0], obstacles[j - len(robots)][0]], [robots[i][1], obstacles[j - len(robots)][1]], '-k')

    plt.title('Start position')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('img/start_pos.png')
    