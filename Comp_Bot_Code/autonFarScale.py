import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonFarScale(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'R':
            self.drive.autonMove(1, 0, 1, 145, 0, 0, 1, 0)

            self.drive.autonMove(2, 1, 0, 0, 90, .5, 2, 0)

            self.drive.autonMove(3, 0, 1, 120, 0, 0, 3, 0)

            self.drive.autonMove(4, 1, 0, 0, 100, .5, 3, 0)

            self.drive.autonMove(5, 0, 1, 16, 0, 0, 3, 0)

            self.drive.autonMove(6, 3, setLiftPosition = 3, intakeMode = 3)
        elif self.side == 'right' and self.scalePosition == 'L':
            self.drive.autonMove(1, 0, 1, 145, 0, 0, 1, 0)

            self.drive.autonMove(2, 1, 0, 0, -90, .5, 2, 0)

            self.drive.autonMove(3, 0, 1, 120, 0, 0, 3, 0)

            self.drive.autonMove(4, 1, 0, 0, 100, .5, 3, 0)

            self.drive.autonMove(5, 0, 1, 16, 0, 0, 3, 0)

            self.drive.autonMove(6, 3, setLiftPosition = 3, intakeMode = 3)
        else:
            pass
