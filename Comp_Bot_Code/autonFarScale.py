import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonFarScale(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'R':
            if self.drive.autonMove(1, 0, 1, 230, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, 90, .5, 0, 0):
                pass
            elif self.drive.autonMove(3, 0, 1, 210, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(4, 1, 0, 0, -90, .5, 0, 0):
                pass
            elif self.drive.autonMove(5, 0, 1, 60, 0, 0, 0, 0):
                pass
        elif self.side == 'right' and self.scalePosition == 'L':
            if self.drive.autonMove(1, 0, 1, 230, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, -90, .5, 0, 0):
                pass
            elif self.drive.autonMove(3, 0, 1, 210, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(4, 1, 0, 0, 90, .5, 0, 0):
                pass
            elif self.drive.autonMove(5, 0, 1, 60, 0, 0, 0, 0):
                pass
        else:
            pass
