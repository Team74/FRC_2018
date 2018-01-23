import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonCenterEitherSwitch(autonBaseInit):
    def run(self):
        if self.position == 'left':

            if self.moveNumber == 1:
                if self.drive.autonDriveStraight(.5, 12):
                    pass
                else:
                    print('Move #1 done')
                    self.moveNumber = 2

            if self.moveNumber == 2:
                if self.drive.autonPivot(-35):
                    pass
                else:
                    print('Move #2 done')
                    self.moveNumber = 3

            if self.moveNumber == 3:
                if self.drive.autonDriveStraight(.5, 36):
                    pass
                else:
                    print('Move #3 done')
                    self.moveNumber = 4

            if self.moveNumber == 4:
                if self.drive.autonPivot(25):
                    pass
                else:
                    print('Move #4 done')
                    self.moveNumber = 5

            if self.moveNumber == 5:
                if self.drive.autonDriveStraight(.5, 5):
                    pass
                else:
                    print('Move #5 done')
                    self.moveNumber = 6


        elif self.position == 'right':

            if self.moveNumber == 1:
                if self.drive.autonDriveStraight(.5, 12):
                    pass
                else:
                    print('Move #1 done')
                    self.moveNumber = 2

            if self.moveNumber == 2:
                if self.drive.autonPivot(35):
                    pass
                else:
                    print('Move #2 done')
                    self.moveNumber = 3

            if self.moveNumber == 3:
                if self.drive.autonDriveStraight(.5, 36):
                    pass
                else:
                    print('Move #3 done')
                    self.moveNumber = 4

            if self.moveNumber == 4:
                if self.drive.autonPivot(-25):
                    pass
                else:
                    print('Move #4 done')
                    self.moveNumber = 5

            if self.moveNumber == 5:
                if self.drive.autonDriveStraight(.5, 5):
                    pass
                else:
                    print('Move #5 done')
                    self.moveNumber = 6

        else:
            pass
