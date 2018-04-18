import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonTurningTuning(autonBaseInit):
    def run(self):
        self.drive.autonMove(1, 1, turnAngle = 40, turnSpeed = .75)
