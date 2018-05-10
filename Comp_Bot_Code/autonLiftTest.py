import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonLiftTest(autonBaseInit):
    def run(self):
        self.drive.autonMove(1, 0, speed = .5, distance  = 200, setLiftPosition = 3)
        self.drive.autonMove(2, 0, speed = -.5, distance = -200, setLiftPosition = 0)
