file = open("TestFile.py","w")

file.write("1, 30, 4, \n")
file.write("2, 75, \n")
file.write("1, 20, -5, \n")
file.write("3, 1, \n")
file.close()
masterList = []
with open("TestFile.py", "r") as f:
    data = f.readlines()
    for line in data:
        temp = line.split(", ")
        temp.remove("\n")
        masterList.append(temp)
    print(masterList)
file.close()
for i in masterList:
    if i[0] == "1":
        i[0] = "driveCommand"
    elif i[0] == "2":
        i[0] = "turnCommand"
    elif i[0] == "3":
        i[0] = "genericCommand"
print(masterList)
#next try looping through the list, since each list is a
#list I can do what I need from inside the body of the loop
