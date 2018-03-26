import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonDrive(autonBaseInit):
    def run(self):
        self.drive.autonMove(1, 0, 1, 200, 0, 0, 0, 0)#Actual Drive Code
        #self.drive.autonMove(1, 0, .5, 50, 0, 0, 0, 0)#Set distance testing
