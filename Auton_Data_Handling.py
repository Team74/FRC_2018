'''
speed="None"
direction="None"
angle="None"
testCommand ="None"
import AutonInterpreter

class AutonHandling():

    def __init__(self):
        self.stageNumber = 0

    def readCommandList(self, alist, drive):
        i = self.stageNumber #Sets up iterator variable
        cmdList = AutonInterpreter.AutonInterpreter.getList(None, alist)
        #for i in range(0, len(cmdList()): #Basically, 'While i is less than or equal to the number or items in the list;'
        if cmdList[i][0] == "driveCommand":#Checking first item in list to see if it's a drive command
            self.advanceStage(drive.autonDriveStraight(float(cmdList[i][2]), int(cmdList[i][1])))#, cmdList[i][3], cmdList[i][4])#It was a drive command! now it pulls all
                #of the data from the list and plugs it into the DriveCommand function
        elif cmdList[i][0] == "turnCommand":#Repeat above process, just checking for a different variable
            self.advanceStage(drive.autonPivot(float(cmdList[i][1])))#the second 1 indicates the speed of the turn, this can be tuned down

    def advanceStage(self, incomplete):
        if not incomplete:
            self.stageNumber +=1
'''
''' Used to work with runCommands, need to update in order to test out readCommandList
commands = DriveCommand.DriveCommand("Fast","Forward","Test"), TurnCommand.TurnCommand("Slow","Left"), DriveCommand.DriveCommand("Slow", "Backwards", "Test")
AutonHandling().runCommands(commands)
'''
