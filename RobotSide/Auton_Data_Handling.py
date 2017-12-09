
speed="None"
direction="None"
angle="None"
testCommand ="None"
import DriveCommand, TurnCommand

class AutonHandling():

    def runCommands(self, commandList):
        for command in commandList:
            command.runCommand()

commands = DriveCommand.DriveCommand("Fast","Forward","Test"), TurnCommand.TurnCommand("Slow","Left"), DriveCommand.DriveCommand("Slow", "Backwards", "Test")
AutonHandling().runCommands(commands)
