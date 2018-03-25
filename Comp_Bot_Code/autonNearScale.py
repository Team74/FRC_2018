import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearScale(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'L':
            self.drive.autonMove(1, 0, 1, 230, 0, 0, 3, 0)

            self.drive.autonMove(2, 1, 0, 0, 45, .75, 3, 0)

            self.drive.autonMove(3, 0, 1, 5, 0, 0, 3, 0)

            self.drive.autonMove(4, 3, 0, 0, 0, 0, 3, 2)
        if self.side == 'right' and self.scalePosition == 'R':
            self.drive.autonMove(1, 0, 1, 230, 0, 0, 3, 0)

            self.drive.autonMove(2, 1, 0, 0, -38, .75, 3, 0)

            self.drive.autonMove(3, 0, 1, 5, 0, 0, 3, 0)

            self.drive.autonMove(4, 3, 0, 0, 0, 0, 3, 2)
        else:
            pass
