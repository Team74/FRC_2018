import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonTwoCubeScale(autonBaseInit):
#def autonMove(moveNumberPass, commandNumber, speed, distance, turnAngle):
    def run(self):
        if self.side == 'left' and self.position == 'left':
            if self.drive.autonMove(1, 0, .5, 180, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, 15, .5):
                pass
            elif self.drive.autonMove(3, 0, .5, 30, 0, 0):
                pass
            elif self.drive.autonMove(4, 1, 0, 0, -15, .5):
                pass
            elif self.drive.autonMove(5, 0, .5, 15, 0, .5):
                pass
            elif self.drive.autonMove(6, 0, .5, -15, 0, 0):
                pass
            elif self.drive.autonMove(7, 1, 0, 0, 180, .5):
                pass
            elif self.drive.autonMove(8, 0, .5, 30, 0, 0):
                pass
            elif self.drive.autonMove(9, 0, .5, -30, 0, 0):
                pass
            elif self.drive.autonMove(10, 1, 0, 0, -180, .5):
                pass
            elif self.drive.autonMove(11, 0, .5, 15, 0, 0):
                pass
            elif self.drive.autonMove(12, 2, 0, 0, 0, 0):
                pass

        elif self.side == 'right' and self.position == 'right':
            if self.drive.autonMove(1, 0, .5, 180, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, -15, .5):
                pass
            elif self.drive.autonMove(3, 0, .5, 30, 0, 0):
                pass
            elif self.drive.autonMove(4, 1, 0, 0, 15, .5):
                pass
            elif self.drive.autonMove(5, 0, .5, 15, 0, 0):
                pass
            elif self.drive.autonMove(6, 0, .5, -15, 0, 0):
                pass
            elif self.drive.autonMove(7, 1, 0, 0, -180, .5):
                pass
            elif self.drive.autonMove(8, 0, .5, 30, 0, 0):
                pass
            elif self.drive.autonMove(9, 0, .5, -30, 0, 0):
                pass
            elif self.drive.autonMove(10, 1, 0, 0, 180, .5):
                pass
            elif self.drive.autonMove(11, 0, .5, 15, 0, 0):
                pass
            elif self.drive.autonMove(12, 2, 0, 0, 0, 0):
                pass

        else:
            pass
