import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonLiftTest(autonBaseInit):
    def run(self):
        #self.drive.autonMove(1, 0, 0, 1000000, 0, 0, 3, 0)
        #self.drive.autonMove(1, 2, 0, 0, 0, 0, 0, 0)
        self.drive.autonMove(1, 0, 0, 10000000000, 0, 0, 3, 0)
        #self.drive.autonMove(1, 2, 0, 0, 0, 0, 0, 0)
        #self.drive.autonMove(1, 2, 0, 0, 0, 0, 3, 0)
        #pass
