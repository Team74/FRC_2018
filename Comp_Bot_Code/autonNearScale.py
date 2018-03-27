import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearScale(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'L':
            self.drive.autonMove(1, 2, setLiftPosition = 2, intakeMode = 0)

            self.drive.autonMove(2, 0, 1, 187, 0, 0, 3, 0)

            self.drive.autonMove(3, 1, 0, 0, 22, .75, 3, 0)

            self.drive.autonMove(4, 2, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(5, 3, 0, 0, 0, 0, 3, 3)
        if self.side == 'right' and self.scalePosition == 'R':
            self.drive.autonMove(1, 2, setLiftPosition = 2, intakeMode = 0)

            self.drive.autonMove(2, 0, 1, 187, 0, 0, 3, 0)

            self.drive.autonMove(3, 1, 0, 0, -22, .75, 3, 0)

            self.drive.autonMove(4, 2, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(5, 3, 0, 0, 0, 0, 3, 3)
        else:
            pass
