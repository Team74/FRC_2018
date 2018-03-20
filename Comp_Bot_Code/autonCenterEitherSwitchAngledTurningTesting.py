import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonCenterEitherSwitchAngledTurningTesting(autonBaseInit):
    def run(self):
        if self.side == 'center':
            if self.switchPosition == 'L':
                self.drive.autonMove(1, 5, turnSpeed = 1, turnAngle = -25, radius = 30, setLiftPosition = 1, intakeMode = 0)

                self.drive.autonMove(2, 0 , speed =1, distance = 55, setLiftPosition = 2, intakeMode = 0)

                self.drive.autonMove(3 , 5, turnSpeed = 1, turnAngle = 25, radius = 30, setLiftPosition = 2, intakeMode = 0)

                self.drive.autonMove(4, 0, speed = .5, distance = 10, setLiftPosition = 2, intakeMode = 0)

                self.drive.autonMove(5, 3, setLiftPosition = 2, intakeMode = 2)

                self.drive.autonMove(6, 5,turnSpeed = -.5, radius = 27.5, turnAngle = 180)

                self.drive.autonMove(7, 0, speed = -1, distance = 36, setLiftPosition = 0, intakeMode = 0)

                self.drive.autonMove(8, 4)
            if self.switchPosition == 'R':
                self.drive.autonMove(1, 5, turnSpeed = 1, turnAngle = 30, radius = 30, setLiftPosition = 1, intakeMode = 0)

                self.drive.autonMove(2, 0 , speed =1, distance = 55, setLiftPosition = 2, intakeMode = 0)

                self.drive.autonMove(3 , 5, turnSpeed = 1, turnAngle = -30, radius = 30, setLiftPosition = 2, intakeMode = 0)

                self.drive.autonMove(4, 0, speed = .5, distance = 10, setLiftPosition = 2, intakeMode = 0)

                self.drive.autonMove(5, 3, setLiftPosition = 2, intakeMode = 2)

                self.drive.autonMove(6, 5,turnSpeed = -.5, radius = 27.5, turnAngle = -180)

                self.drive.autonMove(7, 0, speed = -1, distance = 36, setLiftPosition = 0, intakeMode = 0)

                self.drive.autonMove(8, 4)
            else:
                pass
