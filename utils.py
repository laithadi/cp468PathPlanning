def readTextFile():

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


