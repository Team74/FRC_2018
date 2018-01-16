width = 100		#width in whatever units you want it to be
height = 100		#height, same
print_to_console = False    #if false, stores in convert/<name>, where <name> is the chosen save from save/<name> typed into input


 #---------------------------------------------------------------------

import math

commandOptions = {}
comm = open("commands.dat", "r")
for i in comm:
    x = i.split(":")
    commandOptions[x[0]] = x[1][0:-1]

filename = input("Save Name> ")
file = open("save/" + filename, "r")

nodepos = file.readline(); nodepos = nodepos[6:].split(", "); nodepos = [float(nodepos[0].split(":")[1])*width, float(nodepos[1].split(":")[1])*height]
angle = 0
commandlist = []

for line in file:
    if line[:6] == "Node> ":
        x = line[6:-1].split(", ")
        temp = [float(x[0].split(":")[1])*width, float(x[1].split(":")[1])*height]
        new_angle = math.degrees(math.atan2(-(temp[0] - nodepos[0]), (temp[1] - nodepos[1])))
        commandlist.append("[1," + str((angle - new_angle + 180) % 360 - 180) + "]") #assuming the robot points forward on the field, do -x, y for y,x to account for 90 degree rotation
        commandlist.append("[0," + str(math.sqrt((nodepos[0] - temp[0])**2 + (nodepos[1] - temp[1])**2)) + "]")
        nodepos = temp
        angle = new_angle
    elif line[:6] == "Comm> ":
        commandlist.append("[" + commandOptions[line[6:-1]] + "]")
    else:
        print("Type Not Found")

outputstring = ""

for i in commandlist:
    outputstring += (i + "\n")
if print_to_console:
    print(outputstring)
else:
    zing = open("convert/" + filename, "w" )
    zing.write(outputstring)
