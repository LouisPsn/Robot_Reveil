import numpy as np



def load_data(file_name):
    """
    Loads the data from the file and returns a numpy array.
    :param file_name: The name of the file to load.
    :return: The data as a numpy array.
    """
    file = open(file_name, 'r')
    nb_robots = int(file.readline())
    Edges = np.zeros([nb_robots, nb_robots]);
    RobotStart = []
    RobotCoords = []
    Obstacles = []
    for line in file:
        numb = ""
        if line[0] == 'R':
            RobotStart.append(int(line.split(':')[1].split(',')[0].split('(')[1]))
            RobotStart.append(int(line.split(':')[1].split(',')[1].split(')')[0]))
        elif line[0] == 'X':
            Obstacles.append([int(line.split(':')[1].split(';')[0].split(',')[0].split('(')[1]), int(line.split(':')[1].split(';')[0].split(',')[1].split(')')[0])])

            Obstacles.append([int(line.split(':')[1].split(';')[1].split(',')[0].split('(')[1]), int(line.split(':')[1].split(';')[1].split(',')[1].split(')')[0])])
        elif 48 <= ord(line[0]) <= 57:
            numb += line[0]
            k = 1
            while(line[k] != ':'):
                numb += line[k]
                k += 1
            RobotCoords.append([int(line.split(':')[1].split(',')[0].split('(')[1]), int(line.split(':')[1].split(',')[1].split(')')[0])])
        elif line[0] == 'E':
            O, T = line.split(':')[1].split(',')[0].split('(')[1], line.split(':')[1].split(',')[1].split(')')[0]
            if O == 'R':
                O = '0'
            if T == 'R':
                T = '0' 
            Edges[int(O), int(T)] = 1
        
    file.close()
    return RobotStart, RobotCoords, Obstacles, Edges

