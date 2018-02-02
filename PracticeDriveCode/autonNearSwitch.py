import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearSwitch(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.switchPosition == 'L':
            if self.drive.autonMove(1, 0, 1, 250, 0, 0):
                pass
            elif self.drive.autonMove(2, 1, 0, 0, 75, .5):
                pass
            elif self.drive.autonMove(3, 0, .5, 30, 0, 0):
                pass
            elif self.drive.autonMove(4, 2, 0, 0, 0, 0):
                pass

        elif self.side == 'right' and self.switchPosition == 'R':
                if self.drive.autonMove(1, 0, .5, 100, 0, 0):
                    pass
                elif self.drive.autonMove(2, 1, 0, 0, -90, .5):
                    pass
                elif self.drive.autonMove(3, 0, .5, 15, 0, 0):
                    pass
                elif self.drive.autonMove(4, 2, 0, 0, 0, 0):
                    pass

        else:
            pass
