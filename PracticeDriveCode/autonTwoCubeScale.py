import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonTwoCubeScale(autonBaseInit):
#def autonMove(moveNumberPass, commandNumber, speed, distance, turnAngle):
    def run(self):
        if self.side == 'left' and self.position == 'left':
            self.drive.autonMove(1, 0, 1, 180, 0)
            self.drive.autonMove(2, 1, 0, 0, 15)
            self.drive.autonMove(3, 0, 1, 10, 0)
            self.drive.autonMove(4, 1, 0, 0, -15)
            self.drive.autonMove(5, 0, .5, 5, 0)
            self.drive.autonMove(6, 0, .5, -5, 0)
            self.drive.autonMove(7, 1, 0, 0, 180)
            self.drive.autonMove(8, 0, .5, 10, 0)
            self.drive.autonMove(9, 0, .5, -10, 0)
            self.drive.autonMove(10, 1, 0, 0, -180)
            self.drive.autonMove(11, 0, .5, 5, 0)


        elif self.side == 'right' and self.position == 'right':
            pass
        else:
            pass
