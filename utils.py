def readTextFile():
    """
    Reads and retrieves the infromation from input.txt. 

    returns:
        new_room_dim: a tuple (i,j) of the room dimension. 
        robots: a dictionary {} with 1,2,.. with each respective starting coordinates as the value, as tuples (i,j).
        new_target_point: a tuple (i,j) with the rendezvous coordinate.
        room: a 2D list with the museum.
    """

    # opening input.txt file to access the information 
    f = open("input.old.txt", "r") 
    # reads every line in input.txt file stores each line in a list 
    lines = f.readlines() 

    # the dimensions of the room in a list data type
    room_dim = lines[0].split(" ")  
    # switching the elements for the room_dim to data tpe -> int 
    room_dim[0] = int(room_dim[0])
    room_dim[1] = int(room_dim[1])
    room_dim.remove('\n')
    # final tuple with int x,y coordinates 
    new_room_dim = (room_dim[0], room_dim[1])

    # robot dictionary we will store the starting coordinates for each robot 
    robots = {} 
    # the number of robots in the museum. data type --> int
    num_rob = int(lines[1]) 
    # 2 is the index of the FIRST robots starting coordinates 
    start = 2 

    # adds the robot number (1,2,3,4) and the starting coordinate for each robot in the robots dictionary 
    for i in range(0, num_rob): 
        robots[i+1] = lines[start+i].split(" ")

    # change the values in the robots dictionary into tuples of ints 
    # keys of robots dictionary 
    keys = robots.keys()

    for key in keys:
        # value is a list of str elements 
        value = robots[key]
        # take the first and second element of value (the coordinates of the robot) and change the data type to int
        value[0] = int(value[0])
        value[1] = int(value[1])
        # place the coordinates in a tuple to make it easier for us to use later on 
        new_val = (value[0], value[1])
        # replace the value with the new tuple of int coordinates 
        robots[key] = new_val


    # grabs the rendezvous point from the input.txt file. data type --> list 
    target_point = lines[start+num_rob].split(" ") 
    # change the coordinates to int data type 
    target_point[0] = int(target_point[0])
    target_point[1] = int(target_point[1])
    # remove the extra line at the end of the list 
    target_point.remove("\n")
    # place the coordinates into a tuple to make it easier for us to use later on 
    new_target_point = (target_point[0], target_point[1])

    # room 
    # the number of rows in the room
    rows = new_room_dim[0]   
    # the number of columns in the room 
    cols = new_room_dim[1]  
    # this is a list of lines that contains the room points information from input.txt
    temp = lines[start+num_rob+1:]  
    # this is where we will store the 2d list of the room 
    room = [] 

    # this for loop iterates over the amount of rows there are and creates a new [] within the room variable 
    for row in range(0, rows): 
        room.append([])
        # this for loop iterates over the amount of columns there are and appends a 1 or 0 for each coordinate in the room 
        for col in range(0, cols): 
            room[row].append(0)
            room[row][col] = int(temp[row][col])

    # close the reading of input.txt
    f.close() 

    return new_room_dim, robots, new_target_point, room


def validMoves(room, pos, room_dim):
    """
    parameters: 
        room: a 2D list of the room filled with 1 or 0.
        pos: a tuple (i,j) of where we are trying to find valid moves from.
        room_dim: a tuple (i,j) of the room dimension.

    returns: 
        possible_moves: a list of tuples [(i,j), (l,k), ...].
                tuples are coordinates of valid moves. Meaning a coordinate contains
                a 0 in the room. tuples stored in a list. 
    """

    # where we will store tuples of possible moves that are valid
    possible_moves = [] 

    # the length of the room 
    max_row = room_dim[0] 
    # the width of the room 
    max_col = room_dim[1] 

    # the pos row that we are moving from 
    pos_row = pos[0] 
    # the pos col that we are moving from 
    pos_col = pos[1] 

    # checking if moving up is a valid move 
    if (pos_row - 1 >= 0) and (0 <= pos_col < max_col): 
        if room[pos_row-1][pos_col] == 0: possible_moves.append((pos_row-1, pos_col))

    # checking if moving down is a valid move 
    if (pos_row + 1 < max_row) and (0 <= pos_col < max_col): 
        if room[pos_row+1][pos_col] == 0: possible_moves.append((pos_row+1, pos_col))
    
    # cheching if moving left is a valid move
    if (pos_col - 1 >= 0) and (0 <= pos_row < max_row): 
        if room[pos_row][pos_col-1] == 0: possible_moves.append((pos_row, pos_col-1))

    # checking if moving right is a valid move 
    if (pos_col + 1 < max_col) and (0 <= pos_row < max_row): 
        if room[pos_row][pos_col+1] == 0: possible_moves.append((pos_row, pos_col+1))

    return possible_moves


def validRendezvousPoint(room, target_point):
    """
    parameters: 
        room: a 2D list of the museum containing 1 and 0. 
        target_point: a tuple (i,j). coordinates of the rendezvous point.
    
    returns:
        boolean: True if rendezvous point is valid (0). 
        False otherwise. 
    """
    
    # x and y coordinates of the rendezvous point 
    x_cor = target_point[0]
    y_cor = target_point[1]

    # check if the point in the room is an invalid point (1 or not a 0)
    if room[x_cor][y_cor] != 0: return False

    return True 