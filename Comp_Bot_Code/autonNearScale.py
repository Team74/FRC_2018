import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearScale(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'L':
            if self.drive.autonMove(1, 0, 1, 230, 0, 0, 3, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, 90, .3, 3, 0):
                pass
            elif self.drive.autonMove(3, 0, .75, 10, 0, 0, 3, 0):
                pass
            elif self.drive.autonMove(4, 3, 0, 0, 0, 0, 3, 2):
                pass
        if self.side == 'right' and self.scalePosition == 'R':
            if self.drive.autonMove(1, 0, 1, 230, 0, 0, 3, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, -90, .3, 3, 0):
                pass
            elif self.drive.autonMove(3, 0, .75, 10, 0, 0, 3, 0):
                pass
            elif self.drive.autonMove(4, 3, 0, 0, 0, 0, 3, 2):
                pass
        else:
            pass
