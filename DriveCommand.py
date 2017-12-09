
speed="None"
direction="None"
angle="None"
testCommand ="None"


class DriveCommand():

    def __init__(self, speed, direction, testCommand):
        self.speed = speed
        self.direction = direction
        self.testCommand = testCommand
    def runCommand(self):
        print ("We're driving " + self.speed + " in direction: " + self.direction + " heres the test: " + self.testCommand)
