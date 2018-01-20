import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonSideSwitch(autonBaseInit):
    def run(self):
        if self.moveNumber == 1:
            if self.drive.autonDriveStraight(.6, 60):
                pass
            else:
                print('1st straight done')
                self.moveNumber = 2

        if self.moveNumber == 2:
            if self.drive.autonPivot(90):
                pass
            else:
                print('1st Turn done')
                self.moveNumber = 3

        if self.moveNumber == 3:
            if self.drive.autonDriveStraight(.6, 15):
                pass
            else:
                print('2nd straight done')
                self.moveNumber = 4
