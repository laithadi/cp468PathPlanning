from utils import readTextFile

room_dim, robots, target_point, room = readTextFile() # calling the readTextFile() to grab all the important information from the input.txt file 

# ----------------------------------------------This code right here is to just test and show that what the readTextFile() returns---------------------------------#
print('This is the room dimensions: ')
print(room_dim)
print('\n')
print("this is a dictionary of the robots and their starting points: ")
print(robots)
print('\n')
print("this is the target point or rendezvous point: ")
print(target_point)
print('\n')
print("this is the room in a 2d list:")
print(room)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------#
