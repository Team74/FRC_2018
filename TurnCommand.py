
speed="None"
direction="None"
angle="None"
testCommand ="None"


class TurnCommand():
    def __init__(self, angle):
        self.angle=angle

    def runCommand(self):

        print ("We're turning in direction: ")
        print(self.angle)
