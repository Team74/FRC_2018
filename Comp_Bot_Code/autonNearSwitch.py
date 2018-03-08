import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearSwitch(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.switchPosition == 'L':
            if self.drive.autonMove(1, 0, 1, 145, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, 90, .5, 0, 0):
                pass
            elif self.drive.autonMove(3, 0, .5, 5, 0, 0, 0, 0):
                pass
            elif self.drive.autonMove(4, 0, 0, 1000000000000000000, 0, 0, 0, 0):
                pass

        elif self.side == 'right' and self.switchPosition == 'R':
                if self.drive.autonMove(1, 0, 1, 145, 0, 0, 2, 0):
                    pass
                elif self.drive.autonMove(2, 1, 0, 0, -90, .5, 2, 0):
                    pass
                elif self.drive.autonMove(3, 0, .5, 5, 0, 0, 2, 0):
                    pass
                elif self.drive.autonMove(4, 0, 0, 10000000000000, 0, 0, 2, 2):
                    pass

        else:
            pass
