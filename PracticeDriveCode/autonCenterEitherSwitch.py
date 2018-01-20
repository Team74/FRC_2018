import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonCenterEitherSwitch(autonBaseInit):
    def run(self):
        if self.position == 'left':
            """
            if self.moveNumber == 1:
                if self.drive.autonDriveStraight(.5, 12):
                    pass
                else:
                    self.moveNumber = 2
            """
            if self.moveNumber == 1:
                if self.drive.autonPivot(45):
                    pass
                else:
                    self.moveNumber = 2

            if self.moveNumber == 2:
                if self.drive.autonDriveStraight(.5, 24):
                    pass
                else:
                    self.moveNumber = 3

            if self.moveNumber == 4:
                if self.drive.autonPivot(45):
                    pass
                else:
                    self.moveNumber = 5

            if self.moveNumber == 5:
                if self.drive.autonDriveStraight(.3, 5):
                    pass
                else:
                    self.moveNumber = 6


        elif self.position == 'right':
            pass

        else:
            pass
