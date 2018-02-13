
speed="None"
direction="None"
angle="None"
testCommand ="None"


class DriveCommand():

    def __init__(self, lspeed, ldistance, rspeed, rdistance):
        self.lspeed = lspeed
        self.ldistance = ldistance
        self.rspeed = rspeed
        self.rdistance = rdistance
    def runCommand(self):
        print ("LeftSpeed: " + self.lspeed + ", LeftDistance " + self.ldistance + "RightSpeed: " + self.rspeed + ", RightDistance: " + self.rdistance)
