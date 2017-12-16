
speed="None"
direction="None"
angle="None"
testCommand ="None"
import DriveCommand, TurnCommand# also need to import data from Jacobs classes, just don't know how to quantify that yet

class AutonHandling():
'''
    def runCommands(self, commandList):# Just a testing function, proof of concept
        for command in commandList:
            command.runCommand()
'''
    def readCommandList(self, jacobsList):
        counter = 0 #Sets up iterator variable (posibly an unnessicary holdout from java)
        for counter in '''define class here''' jacobsList: #Basically, 'While counter is less than or equal to the number or items in the list;'
            if jacobsList[counter[1]] == "driveCommand":#Checking first item in list to see if it's a drive command
                DriveCommand.DriveCommand(jacobsList[counter[2]], jacobsList[counter[3]], jacobsList[counter[4]]):#It was a drive command! now it pulls all
                                                                                    #of the data from the list and plugs it into the DriveCommand function
            elif jacobsList[counter[1]] == "turnCommand":#Repeat above process, just checking for a different variable
                TurnCommand.TurnCommand(jacobsList[counter[2]], jacobsList[counter[3]]):#Note how it only pulls 2 items from the list instead of 3,
                                                                                        #because TurnCommand only needs 2 variables
            counter+=1#once it finishes this check, add another number to the counter and check that location (we just checked location 0, now
                      #we add 1 to it and check location 1 next. This goes on until you've searched the whole list)

''' # Used to work with runCommands, need to update in order to test out readCommandList
commands = DriveCommand.DriveCommand("Fast","Forward","Test"), TurnCommand.TurnCommand("Slow","Left"), DriveCommand.DriveCommand("Slow", "Backwards", "Test")
AutonHandling().runCommands(commands)
'''
