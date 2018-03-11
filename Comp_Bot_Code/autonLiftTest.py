import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonLiftTest(autonBaseInit):
    def run(self):
        #self.drive.autonMove(1, 0, 0, 1000000, 0, 0, 3, 0)
        #self.drive.autonMove(2, 2, 0, 0, 0, 0, 0, 0)
        #self.drive.autonMove(3, 2, 0, 0, 0, 0, 2, 0)
        #self.drive.autonMove(4, 2, 0, 0, 0, 0, 0, 0)
        self.drive.autonMove(1, 3, 0, 0, 0, 0, 0, 2)
