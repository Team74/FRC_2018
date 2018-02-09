import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonFarSwitch(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.switchPosition == 'R':
            if self.drive.autonMove(1, 0, 1, 275, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, 75, .5):
                pass
            elif self.drive.autonMove(3, 0, 1, 600, 0, 0):
                pass
            elif self.drive.autonMove(4, 1, 0, 0, 75, .5):
                pass
            elif self.drive.autonMove(5, 0, 1, 20, 0, 0):
                pass
            elif self.drive.autonMove(6, 1, 0, 0, 90, .5):
                pass
            elif self.drive.autonMove(7, 0, 1, 20, 0, 0):
                pass
        elif self.side == 'right' and self.switchPosition == 'L':
            if self.drive.autonMove(1, 0, 1, 230, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, -90, .5):
                pass
            elif self.drive.autonMove(3, 0, 1, 235, 0, 0):
                pass
            elif self.drive.autonMove(4, 1, 0, 0, -90, .5):
                pass
            elif self.drive.autonMove(5, 0, 1, 65, 0, 0):
                pass
            elif self.drive.autonMove(6, 1, 0, 0, -92, .5):
                pass
            elif self.drive.autonMove(7, 0, 1, 20, 0, 0):
                pass
        else:
            pass
