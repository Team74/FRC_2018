import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonFarSwitch(autonBaseInit):
    def run(self):
        if self.side == 'L' and self.switchPosition == 'R':
            if self.drive.autonMove(1, 0, .5, 60, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, 90, .5):
                pass
            elif self.drive.autonMove(3, 0, .3, 120, 0, 0):
                pass
            elif self.drive.autonMove(4, 1, 0, 0, 90, .5):
                pass
            elif self.drive.autonMove(5, 0, .5, 20, 0, 0):
                pass
            elif self.drive.autonMove(6, 1, 0, 0, 90, .5):
                pass
            elif self.drive.autonMove(7, 2, 0, 0, 0, 0):
                pass
        elif self.side == 'R' and self.switchPosition == 'L':
            if self.drive.autonMove(1, 0, .5, 60, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, -90, .5):
                pass
            elif self.drive.autonMove(3, 0, .3, 120, 0, 0):
                pass
            elif self.drive.autonMove(4, 1, 0, 0, -90, .5):
                pass
            elif self.drive.autonMove(5, 0, .5, 20, 0, 0):
                pass
            elif self.drive.autonMove(6, 1, 0, 0, -90, .5):
                pass
            elif self.drive.autonMove(7, 2, 0, 0, 0, 0):
                pass
        else:
            pass
