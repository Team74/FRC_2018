import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearSwitch(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.switchPosition == 'L':
            self.drive.autonMove(1, 0, 1, 125, 0, 0, 1, 0)

            self.drive.autonMove(2, 1, 0, 0, 93, .75, 2, 0)

            self.drive.autonMove(3, 0, .5, 17, 0, 0, 2, 0)

            self.drive.autonMove(4, 3, 0, 0, 0, 0, 2, 3)
        elif self.side == 'right' and self.switchPosition == 'R':
            self.drive.autonMove(1, 0, 1, 130, 0, 0, 2, 0)

            self.drive.autonMove(2, 1, 0, 0, -90, .5, 2, 0)

            self.drive.autonMove(3, 0, .5, 17, 0, 0, 2, 0)

            self.drive.autonMove(4, 3, 0, 0, 0, 0, 2, 3)
        else:
            pass
