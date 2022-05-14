from obstacle import *
from LoadData import *
from graph import *
import numpy as np
import matplotlib.pyplot 
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def print_matrix(matrix):
    for i in range (len(matrix)):
        print(matrix[i])

def test_format_obstacles():
    print("\nTesting format_obstacles()")
    print("--------------------------------------------------------------------------------\n")
    Obstacles = load_data("data.txt")[2]
    print(format_obstacles(Obstacles))
    
def test_load_file():
    print("\nTesting load_file()")
    print("--------------------------------------------------------------------------------\n")
    print(load_data("data.txt"))

def test_crossing_segments():
    print("\nTesting crossing_segments()")
    print("--------------------------------------------------------------------------------\n")
    seg1 = [[0,0], [1,1]]
    seg2 = [[0,1], [1,0]]
    print("[0,0], [1,1] and [0,1], [1,0]:", crossing_segments(seg1, seg2), "(should be TRUE)")

    seg3 = [[2, 2], [3, 4]]
    seg4 = [[5, 2], [4, 4]]
    print("[2, 2], [3, 4] and [5, 2], [4, 4]:", crossing_segments(seg3, seg4), "(should be FALSE)")

    seg5 = [[4, 4], [6, 5]]
    seg6 = [[4, 3], [6, 2]]
    print("[4, 4], [6, 5] and [4, 3], [6, 2]:", crossing_segments(seg5, seg6), "(should be FALSE)")

    seg7 = [[1,1], [0,0]]
    seg8 = [[1,0], [0,1]]
    print("[1,1], [0,0] and [1,0], [0,1] :", crossing_segments(seg7, seg8), "(should be TRUE)")

def main():

    test_format_obstacles()
    test_crossing_segments()
    test_load_file()

main()