import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonFarSwitch(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.switchPosition == 'R':
            self.drive.autonMove(1, 0, 1, 230, 0, 0, 0, 0):

            self.drive.autonMove(2, 1, 0, 0, 90, .5, 0, 0):

            self.drive.autonMove(3, 0, 1, 230, 0, 0, 0, 0):

            self.drive.autonMove(4, 1, 0, 0, 90, .5, 0, 0):

            self.drive.autonMove(5, 0, 1, 60, 0, 0, 0, 0):

            self.drive.autonMove(6, 1, 0, 0, 90, .5, 0, 0):

            self.drive.autonMove(7, 0, 1, 20, 0, 0, 0, 0):

        elif self.side == 'right' and self.switchPosition == 'L':
            self.drive.autonMove(1, 0, 1, 230, 0, 0, 0, 0):

            self.drive.autonMove(2, 1, 0, 0, -90, .5, 0, 0):

            self.drive.autonMove(3, 0, 1, 230, 0, 0, 0, 0):

            self.drive.autonMove(4, 1, 0, 0, -90, .5, 0, 0):

            self.drive.autonMove(5, 0, 1, 60, 0, 0, 0, 0):

            self.drive.autonMove(6, 1, 0, 0, -90, .5, 0, 0):

            self.drive.autonMove(7, 0, 1, 20, 0, 0, 0, 0):

        else:
