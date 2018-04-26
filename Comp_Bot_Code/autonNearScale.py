import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearScale(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'L':
            self.drive.autonMove(1, 0, 1, 193, 0, 0, 3, 0)

            self.drive.autonMove(2, 1, 0, 0, 33, .75, 3, 0)

            self.drive.autonMove(3, 0, speed = -.5, distance = 40, setLiftPosition = 3, intakeMode = 3)

            self.drive.autonMove(4, 1, turnAngle = -15, turnSpeed = .75, setLiftPosition = 3)

            #self.drive.autonMove(4, 1, turnSpeed = .75, turnAngle = 70, setLiftPosition = 0)

            #self.drive.autonMove(4, 0, speed = -.75, distance = 30, setLiftPosition = 0)

            #self.drive.autonMove(6, 1, turnAngle = 90, turnSpeed = .75, setLiftPosition = 3, intakeMode = 0)

            #self.drive.autonMove(7, 0, speed = .5, distance = 20, setLiftPosition = 0, intakeMode = 0)

            #self.drive.autonMove(8, 2, setLiftPosition = 0)

        if self.side == 'right' and self.scalePosition == 'R':
            self.drive.autonMove(1, 0, 1, 187, 0, 0, 3, 0)

            self.drive.autonMove(2, 1, 0, 0, -34, .75, 3, 0)


            self.drive.autonMove(3, 0, speed = -.5, distance = 30, setLiftPosition = 3, intakeMode = 3)

            self.drive.autonMove(4, 2, setLiftPosition = 0)

            self.drive.autonMove(5, 1, turnAngle = 15, turnSpeed = .75, setLiftPosition = 0)

            #self.drive.autonMove(4, 0, speed = -.75, distance = 30, setLiftPosition = 0)

            #self.drive.autonMove(6, 1, turnAngle = -90, turnSpeed = .75, setLiftPosition = 3, intakeMode = 0)

            #self.drive.autonMove(7, 0, speed = .5, distance = 20, setLiftPosition = 0, intakeMode = 0)

            #self.drive.autonMove(8, 2, setLiftPosition = 0)
        else:
            pass
