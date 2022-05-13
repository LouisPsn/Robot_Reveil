from enum import Flag
from tracemalloc import start
from turtle import distance
import numpy as np


def crossing_segments(seg1, seg2):
    a1 = (seg1[1][1] - seg1[0][1])/(seg1[1][0] - seg1[0][0])
    a2 = (seg2[1][1] - seg2[0][1])/(seg2[1][0] - seg2[0][0])

    b1 = seg1[0][1] - a1*seg1[0][0]
    b2 = seg2[0][1] - a2*seg2[0][0]

    A = np.array([  [-a1, 1],
                    [-a2, 1]])
    
    B = np.array([  [b1],
                    [b2]])

    X = np.linalg.solve(A,B)

    x = X[0]
    y = X[1]

    return ((x > seg1[0][0]) and (x < seg1[1][0]) and (x > seg2[0][0]) and (x < seg2[1][0]))


def edge_through_obstacle(edge, obs):
    for i in range (len(obs)):
        return 0



def calculate_distance_obstacle(grid, start, end):
    return 0


def test_crossing_segments():
    seg1 = [[0,0], [1,1]]
    seg2 = [[0,1], [1,0]]
    print(crossing_segments(seg1, seg2))


if __name__ == '__main__':
    grid = np.array([[24, 42],
                    ['R', 10, 10], 
                    [1, 3, 6], 
                    [2, 25, 4], 
                    ['X', (24,8), (26,24)]], dtype=object)

    # print(calculate_distance_obstacle(grid, (10, 10), (3, 6)))
    test_crossing_segments()