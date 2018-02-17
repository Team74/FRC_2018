import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonTwoCubeScale(autonBaseInit):
#def autonMove(moveNumberPass, commandNumber, speed, distance, turnAngle):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'L':
            if self.drive.autonMove(1, 0, 1, 250, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, 25, .5, 0, 0):
                pass
            elif self.drive.autonMove(3, 0, .75, 20, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(4, 1, 0, 0, 135, .5, 0, 0):
                pass
            elif self.drive.autonMove(5, 0, .75, 42, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(6, 0, -.75, 22, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(7, 1, 0, 0, -135, .45, 0, 0):
                pass
            elif self.drive.autonMove(8, 0, .75, 17.5, 0, 0, 0, 0):
                pass
        elif self.side == 'right' and self.scalePosition == 'R':
            pass
        else:
            pass
