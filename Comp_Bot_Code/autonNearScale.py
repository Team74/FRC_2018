import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearScale(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'L':
            if self.drive.autonMove(1, 0, 1, 200, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, 20, .5, 0, 0):
                pass
            elif self.drive.autonMove(3, 0, .75, 70, 0, 0, 0, 0):
                pass
        if self.side == 'right' and self.scalePosition == 'R':
            if self.drive.autonMove(1, 0, 1, 200, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, -20, .5, 0, 0):
                pass
            elif self.drive.autonMove(3, 0, .75, 70, 0, 0, 0, 0):
                pass
        else:
            pass
