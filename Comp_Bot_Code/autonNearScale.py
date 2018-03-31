import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearScale(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'L':
            self.drive.autonMove(1, 0, 1, 187, 0, 0, 3, 0)

            self.drive.autonMove(2, 1, 0, 0, 22, .75, 3, 0)

            self.drive.autonMove(3, 3, setLiftPosition = 3, intakeMode = 3)

            #self.drive.autonMove(6, 1, turnAngle = 90, turnSpeed = .75, setLiftPosition = 3, intakeMode = 0)

            #self.drive.autonMove(7, 0, speed = .5, distance = 20, setLiftPosition = 0, intakeMode = 0)

            #self.drive.autonMove(8, 2, setLiftPosition = 0)

        if self.side == 'right' and self.scalePosition == 'R':
            self.drive.autonMove(1, 0, 1, 187, 0, 0, 3, 0)

            self.drive.autonMove(2, 1, 0, 0, -28, .75, 3, 0)

            self.drive.autonMove(3, 3, setLiftPosition = 3, intakeMode = 3)

            #self.drive.autonMove(6, 1, turnAngle = -90, turnSpeed = .75, setLiftPosition = 3, intakeMode = 0)

            #self.drive.autonMove(7, 0, speed = .5, distance = 20, setLiftPosition = 0, intakeMode = 0)

            #self.drive.autonMove(8, 2, setLiftPosition = 0)
        else:
            pass
