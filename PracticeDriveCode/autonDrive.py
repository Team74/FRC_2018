import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonDrive(autonBaseInit):
    def run(self):
        self.drive.autonMove(1, 0, .5, 50, 0, 0)
        self.drive.autonMove(2, 2, 0, 0, 0, 0)
