import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonLiftTest(autonBaseInit):
    def run(self):
        #self.drive.autonMove(1, 0, 0, 1000000, 0, 0, 3, 0)
        #self.drive.autonMove(1, 2, 0, 0, 0, 0, 0, 0)
        self.drive.autonMove(1, 0, speed = .25, distance = 100000000, setLiftPosition = 3)
        self.drive.autonMove(2, 3, setLiftPosition = 3, intakeMode = 3)
        #self.drive.autonMove(1, 2, 0, 0, 0, 0, 0, 0)
        #self.drive.autonMove(1, 2, 0, 0, 0, 0, 3, 0)
        #pass
