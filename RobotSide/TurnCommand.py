
speed="None"
direction="None"
angle="None"
testCommand ="None"


class TurnCommand():
    def __init__(self, speed, angle):
        self.speed = speed
        self.angle=angle
        
    def runCommand(self):

        print ("We're turning " + self.speed + " in direction: " + self.angle)
