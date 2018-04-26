import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonPrepScaleScore(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'R':
            self.drive.autonMove(1, 0, speed = 1, distance = 145, setLiftPosition = 1)

            self.drive.autonMove(2, 1, turnAngle = 90, turnSpeed = .75, setLiftPosition = 1)

            self.drive.autonMove(3, 0, speed = 1, distance = 80, setLiftPosition = 1)
        elif self.side == 'right' and self.scalePosition == 'L':
            self.drive.autonMove(1, 0, speed = 1, distance = 155, setLiftPosition = 1)

            self.drive.autonMove(2, 1, turnAngle = -82, turnSpeed = .75, setLiftPosition = 1)

            self.drive.autonMove(3, 0, speed = 1, distance = 80, setLiftPosition = 1)
        elif self.side == 'right' and self.scalePosition == 'R':
            self.drive.autonMove(1, 0, speed = 1, distance = 115)
        elif self.side == 'left' and self.scalePosition == 'L':
            self.drive.autonMove(1, 0, speed = 1, distance = 115)
        else:
            self.drive.autonMove(1, 0, speed = 1, distance = 115)#If none of the other conditions are met and this one is called we drive
