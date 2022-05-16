# from enum import Flag
# from tracemalloc import start
# from turtle import distance
import numpy as np


def format_obstacles(obstacles):
    new_format = []
    i = 0
    while i < len(obstacles):
        new_format.append([obstacles[i][0], obstacles[i][1]])
        new_format.append([obstacles[i][0], obstacles[i+1][1]])
        new_format.append([obstacles[i+1][0], obstacles[i+1][1]])
        new_format.append([obstacles[i+1][0], obstacles[i][1]])
        i += 2
    return new_format

def check_point_between_coords(point, coord1, coord2):
    if coord1 > coord2:
        coord1, coord2 = coord2, coord1
    return bool(coord1 < point < coord2)

def crossing_segments(seg1, seg2):

    #if the segments are vertical
    if seg1[0][0] == seg1[1][0]:
        prop_1x = check_point_between_coords(seg1[0][0], seg2[0][0], seg2[1][0])
        prop_2x = check_point_between_coords(seg1[1][0], seg2[0][0], seg2[1][0])
        prop_1y = check_point_between_coords(seg2[0][1], seg1[0][1], seg1[1][1])
        prop_2y = check_point_between_coords(seg2[1][1], seg1[0][1], seg1[1][1])
        return prop_1x and prop_2x and prop_1y and prop_2y
    
    elif seg2[0][0] == seg2[1][0]:
        return crossing_segments(seg2, seg1)

    #check if the segments are parallel
    vect1 = np.array([seg1[1][0] - seg1[0][0], seg1[1][1] - seg1[0][1]])
    vect2 = np.array([seg2[1][0] - seg2[0][0], seg2[1][1] - seg2[0][1]])
    if np.cross(vect1, vect2) == 0:
        return False     

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
    #checking if the intersection is on the segment.
    return check_point_between_coords(x, seg1[0][0], seg1[1][0]) and check_point_between_coords(y, seg1[0][1], seg1[1][1]) and check_point_between_coords(x, seg2[0][0], seg2[1][0]) and check_point_between_coords(y, seg2[0][1], seg2[1][1])

def edge_through_obstacle(edge, obs):
    for i in range (len(obs)):
        return 0

def calculate_distance_obstacle(grid, start, end):
    return 0

if __name__ == '__main__':
    grid = np.array([[24, 42],
                    ['R', 10, 10], 
                    [1, 3, 6], 
                    [2, 25, 4], 
                    ['X', (24,8), (26,24)]], dtype=object)
    # print(calculate_distance_obstacle(grid, (10, 10), (3, 6)))