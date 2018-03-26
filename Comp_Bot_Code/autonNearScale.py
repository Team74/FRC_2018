import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearScale(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'L':
            self.drive.autonMove(1, 0, speed = 1, distance = 230, setLiftPosition = 3, gear = 'high')

            self.drive.autonMove(2, 1, turnangle = 38, turnSpeed = .75, setLiftPosition = 3, gear = 'low')

            self.drive.autonMove(3, 0, speed = 1, distance = 5, setLiftPosition = 3, gear = 'low')

            self.drive.autonMove(4, 3,  setLiftPosition = 3, intakeMode = 2)
        if self.side == 'right' and self.scalePosition == 'R':
            self.drive.autonMove(1, 0, speed = 1, distance = 230, setLiftPosition = 3, gear = 'high')

            self.drive.autonMove(2, 1, turnangle = -38, turnSpeed = .75, setLiftPosition = 3, gear = 'low')

            self.drive.autonMove(3, 0, speed = 1, distance = 5, setLiftPosition = 3, gear = 'low')

            self.drive.autonMove(4, 3, setLiftPosition = 3, intakeMode = 2)
        else:
            pass
