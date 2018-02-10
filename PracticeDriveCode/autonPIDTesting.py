import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonPIDTesting(autonBaseInit):
    def run(self):
        if self.drive.autonMove(1, 1, 0, 0, 90, 0):
            pass
