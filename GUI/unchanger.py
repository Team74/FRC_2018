import math

width = 27*12*2        #width in whatever units you want it to be
height = 27*12        #height, same

commandOptions = {}
comm = open("commands.dat", "r")
for i in comm:
    x = i.split(":")
    commandOptions[x[1][0:-1]] = x[0]
print(commandOptions)

filename = input("Convert Name> ")
file = open("convert/" + filename, "r")

angle = 0
position = [None, None]
commandlist = []
def add_node():
    commandlist.append("Node> x:" + str(position[0]) + ", y:" + str(position[1]))
def add_command(inp):
    commandlist.append("Comm> " + commandOptions[inp])

exit = True
for _line in file:
    full_line = _line.strip('[]\n\t ')
    line = full_line.split(',')
    if exit:
        exit = False
        position = [float(line[0])/width,float(line[1])/height]
        add_node()
        continue
    if line[0] == "0":
        #ldist = line[2]; rdist = line[4]; #For the moment, we are not using separate left and right distances.
        dist = float(line[2])
        y = dist/height*math.cos(math.radians(angle))
        x = dist/width*math.sin(math.radians(angle))
        position[0] += x; position[1] += y
        add_node()
    elif line[0] == "1":
        angle += float(line[1])
    else:
        add_command(full_line)

for i in commandlist:
    print(i)
