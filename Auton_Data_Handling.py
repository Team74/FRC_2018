
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
                DriveCommand.DriveCommand(i[1], i[2], i[3], i[4]).runCommand()#It was a drive command! now it pulls all
                #of the data from the list and plugs it into the DriveCommand function
            elif i[0] == "turnCommand":#Repeat above process, just checking for a different variable
                TurnCommand.TurnCommand(i[1]).runCommand()

AutonHandling.readCommandList(None, "haha")
''' # Used to work with runCommands, need to update in order to test out readCommandList
commands = DriveCommand.DriveCommand("Fast","Forward","Test"), TurnCommand.TurnCommand("Slow","Left"), DriveCommand.DriveCommand("Slow", "Backwards", "Test")
AutonHandling().runCommands(commands)
'''
