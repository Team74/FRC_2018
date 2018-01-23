import wpilib
#from PracticeDriveCode import drive, operatorFunctions, robot

class AutonInterpreter():

    def getList(self, name):
        masterList = []
        with open("/home/lvuser/py/convert/" + name, "r") as f:
            data = f.readlines()
            for line in data:
                line = line[:-1]
                temp = line.split(",")
                #temp.remove("\n")
                masterList.append(temp)
            #print(masterList)
        f.close()
        for i in masterList:
            if i[0] == "0":
                i[0] = "driveCommand"
            elif i[0] == "1":
                i[0] = "turnCommand"
            elif i[0] == "2":
                i[0] = "genericCommand"
        return(masterList)
