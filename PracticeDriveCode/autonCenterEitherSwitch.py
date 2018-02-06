import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonCenterEitherSwitch(autonBaseInit):
    def run(self):
        if self.side == 'center':
            if self.switchPosition == 'L':
                if self.drive.autonMove(1, 0, 1, 24, 0, 0):
                    print('In 1')
                elif self.drive.autonMove(2, 1, 0, 0, -35, .5):
                    print('In 2')
                elif self.drive.autonMove(3, 0, 1, 85, 0, 0):
                    print('In 3')
                elif self.drive.autonMove(4, 1, 0, 0, 40, .5):
                    print('In 4')
                elif self.drive.autonMove(5, 0, .5, 10, 0, 0):
                    print('In 5')
                elif self.drive.autonMove(6, 2, 0, 0, 0, 0):
                    pass

            elif self.switchPosition == 'R':
                if self.drive.autonMove(1, 0, 1, 24, 0, 0):
                    print('In 1')
                elif self.drive.autonMove(2, 1, 0, 0, 45, .5):
                    print('In 2')
                elif self.drive.autonMove(3, 0, 1, 90, 0, 0):
                    print('In 3')
                elif self.drive.autonMove(4, 1, 0, 0, -45, .5):
                    print('In 4')
                elif self.drive.autonMove(5, 0, .5, 10, 0, 0):
                    print('In 5')
                elif self.drive.autonMove(6, 2, 0, 0, 0, 0):
                    pass
            else:
                pass
