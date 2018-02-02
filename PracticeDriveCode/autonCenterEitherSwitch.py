import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonCenterEitherSwitch(autonBaseInit):
    def run(self):
        if self.side == 'center':
            if self.switchPosition == 'L':
                if self.drive.autonMove(1, 0, .5, 36, 0, 0):
                    pass
                elif self.drive.autonMove(2, 1, 0, 0, -35, .5):
                    pass
                elif self.drive.autonMove(3, 0, .5, 85, 0, 0):
                    pass
                elif self.drive.autonMove(4, 1, 0, 0, 40, .5):
                    pass
                elif self.drive.autonMove(5, 0, 1, 85, 0, 0):
                    pass
                elif self.drive.autonMove(6, 2, 0, 0, 0, 0):
                    pass

            elif self.switchPosition == 'R':
                if self.drive.autonMove(1, 0, .5, 36, 0, 0):
                    pass
                elif self.drive.autonMove(2, 1, 0, 0, 35, .5):
                    pass
                elif self.drive.autonMove(3, 0, .5, 125, 0, 0):
                    pass
                elif self.drive.autonMove(4, 1, 0, 0, -30, .5):
                    pass
                elif self.drive.autonMove(5, 0, 1, 85, 0, 0):
                    pass
                elif self.drive.autonMove(6, 2, 0, 0, 0, 0):
                    pass
            else:
                pass
