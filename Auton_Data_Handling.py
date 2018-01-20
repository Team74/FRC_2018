
speed="None"
direction="None"
angle="None"
testCommand ="None"
import DriveCommand, TurnCommand, AutonInterpreter
from PracticeDriveCode import driveTrain, operatorFunctions

class AutonHandling():

    def readCommandList(self, alist):
        i = 0 #Sets up iterator variable
        cmdList = AutonInterpreter.AutonInterpreter.getList(None, alist)
        for i in cmdList: #Basically, 'While i is less than or equal to the number or items in the list;'
            if i[0] == "driveCommand":#Checking first item in list to see if it's a drive command
                drive.autonDrawDrive(i[1], i[2], i[3], i[4])#It was a drive command! now it pulls all
                #of the data from the list and plugs it into the DriveCommand function
            elif i[0] == "turnCommand":#Repeat above process, just checking for a different variable
                drive.turnAngle(i[1], 1)#the second 1 indicates the speed of the turn, this can be tuned down

AutonHandling.readCommandList(None, "square")
''' # Used to work with runCommands, need to update in order to test out readCommandList
commands = DriveCommand.DriveCommand("Fast","Forward","Test"), TurnCommand.TurnCommand("Slow","Left"), DriveCommand.DriveCommand("Slow", "Backwards", "Test")
AutonHandling().runCommands(commands)
'''
