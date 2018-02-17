import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearScale(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition== 'L':
            if self.drive.autonMove(1, 0, 1, 200, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, 30, .3):
                pass
            elif self.drive.autonMove(3, 0, .5, 80, 0, 0):
                pass
        elif self.position == 'R' and self.side == 'R':
            if self.drive.autonMove(1, 0, .5, 180, 0, 0):
                pass
            #elif self.drive.autonMove(2, 2, 0, 0, 0, 0):
            #    pass
            elif self.drive.autonMove(2, 1, 0, 0, -90, .3):
                pass
            elif self.drive.autonMove(4, 0, .5, 20, 0, 0):
                pass
            elif self.drive.autonMove(4, 2, 0, 0, 0, 0):
                pass
        else:
            pass
