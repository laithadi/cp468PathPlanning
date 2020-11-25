def readTextFile():
    """
    Reads the input.txt file and returns the room dim (list), robots and their starting positions (dictionary),
    target point (list), room (2d list)
    """
    f = open("input.txt", "r") # opening input.txt file to access the information 

    lines = f.readlines() # reads every line in input.txt file stores each line in a list 

    room_dim = lines[0].split(" ") # the dimensions of the room in a list data type 

    robots = {} 
    num_rob = int(lines[1]) # this gets the number of robots there. data type --> int
    start = 2 # 2 is the index of the position of the first robot 

    for i in range(0, num_rob): # adds the robot number and the starting coordinate for each robot in a dictionary 
        robots[i+1] = lines[start+i].split(" ")

    target_point = lines[start+num_rob].split(" ") # grabs the rendezvous point from the input.txt file. data type --> list 

    rows = int(room_dim[0])  # the number of rows in the room 
    cols = int(room_dim[1])  # the number of columns in the room 
    temp = lines[start+num_rob+1:] # this is a list of lines that contains the room points information from input.txt 

    room = [] # this is where we will store the 2d list of the room 

    for row in range(0, rows): # this for loop iterates over the amount of rows there are and creates a new [] within the room variable 
        room.append([])
        for col in range(0, cols): # this for loop iterates over the amount of columns there are and appends a 1 or 0 for each coordinate in the room 
            room[row].append(0)
            room[row][col] = int(temp[row][col])

    f.close() # close the reading of input.txt

    return room_dim, robots, target_point, room


def validMoves(room, pos, room_dim):
    """
    takes in a room (2d list), a pos (tuple) and room_dim (tuple).
    Returns a list of tuples of the neighbouring spots. 
    """

    possible_moves = [] # where we will store tuples of possible moves that are valid

    length = int(room_dim[0]) # the length of the room 
    width = int(room_dim[1]) # the width of the room 

    pos_row = int(pos[0]) # the pos row that we are moving from 
    pos_col = int(pos[1]) # the pos col that we are moving from 

    if pos_row - 1 >= 0: # checking if moving up is a valid move 
        if room[pos_row-1][pos_col] == 0: possible_moves.append((pos_row-1, pos_col))

    if pos_row + 1 <= length: # checking if moving down is a valid move 
        if room[pos_row+1][pos_col] == 0: possible_moves.append((pos_row+1, pos_col))
    
    if pos_col - 1 >= 0: # cheching if moving left is a valid move
        if room[pos_row][pos_col-1] == 0: possible_moves.append((pos_row, pos_col-1))

    if pos_col + 1 <= width: # checking if moving right is a valid move 
        if room[pos_row][pos_col+1] == 0: possible_moves.append((pos_row, pos_col+1))

    return possible_moves


def targetReached(x1y1, x2y2):
    """
    Checks if two coordinates are the same.
    x1y1 is a []
    x2y2 is a ()
    """

    x1y1[0] = int(x1y1[0]) # changing the str elemnts in the list to an int to compare 
    x1y1[1] = int(x1y1[1])

    temp = (x1y1[0], x2y2[1])   # putting the coordinates in a () since x2y2 is a () so we can compare 

    return temp == x2y2 
