from tracemalloc import start
from turtle import distance
import numpy as np


def find_obstacles(grid):
    obstacles = []
    for i in range(len(grid)):
        if (grid[i][0] == 'X'):
            obstacles.append([grid[i][1], grid[i][2]])
    return obstacles


def calculate_distance_obstacle(grid, start, end):
    obstacles = find_obstacles(grid)
    

if __name__ == '__main__':
    grid = np.array([['R', 10, 10], 
                    [1, 3, 6], 
                    [2, 25, 4], 
                    ['X', (24,8), (26,24)]], dtype=object)

    obs = find_obstacles(grid)
    print(obs)