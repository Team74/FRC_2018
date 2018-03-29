import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonTwoCubeScale(autonBaseInit):
#def autonMove(moveNumberPass, commandNumber, speed, distance, turnAngle, turnspeed, liftposition, intakemode):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'L':
            self.drive.autonMove(1, 0, speed = 1, distance  = 187, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(2, 1, turnAngle = 22, turnSpeed = .75, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(3, 2, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(4, 0, speed = -1, distance = -42, setLiftPosition = 0, intakeMode = 3)

            self.drive.autonMove(5, 1, turnAngle = 100, turnSpeed = .75, setLiftPosition = 0, intakeMode = 1)

            self.drive.autonMove(6, 0, speed = .5, distance = 22, setLiftPosition = 0, intakeMode = 1)

            self.drive.autonMove(7, 0, speed = -.5, distance  = -22, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(8, 1, turnAngle = -100, turnSpeed = .75, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(9, 0, speed = 1, distance  = 42, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(10, 3, setLiftPosition = 3, intakeMode = 3)
        elif self.side == 'right' and self.scalePosition == 'R':
            self.drive.autonMove(1, 0, speed = 1, distance  = 187, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(2, 1, turnAngle = 22, turnSpeed = .75, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(3, 2, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(4, 0, speed = -1, distance = -42, setLiftPosition = 0, intakeMode = 3)

            self.drive.autonMove(5, 1, turnAngle = -100, turnSpeed = .75, setLiftPosition = 0, intakeMode = 1)

            self.drive.autonMove(6, 0, speed = .5, distance = 22, setLiftPosition = 0, intakeMode = 1)

            self.drive.autonMove(7, 0, speed = -.5, distance  = -22, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(8, 1, turnAngle = 100, turnSpeed = .75, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(9, 0, speed = 1, distance  = 42, setLiftPosition = 3, intakeMode = 0)

            self.drive.autonMove(10, 3, setLiftPosition = 3, intakeMode = 3)
        else:
            pass
