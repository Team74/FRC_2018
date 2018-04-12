import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonCenterEitherSwitch(autonBaseInit):
    def run(self):
        if self.side == 'center':
            if self.switchPosition == 'L':
                self.drive.autonMove(1, 0, speed = .6, distance = 12, setLiftPosition = 1, intakeMode = 0)

                self.drive.autonMove(2, 1,turnAngle = -40, turnSpeed = 1, setLiftPosition = 1, intakeMode = 0)

                self.drive.autonMove(3, 0, 1, 47, 0, 0, 2, 0)

                self.drive.autonMove(4, 1, 0, 0, 40, .75, 2, 0)

                self.drive.autonMove(5, 0, speed = .8, distance = 8, setLiftPosition = 2)

                self.drive.autonMove(6, 0, speed = -.75, distance = 35, setLiftPosition = 2, intakeMode = 3)

                self.drive.autonMove(7, 1, turnSpeed = .65, turnAngle = 49, setLiftPosition = 0)

                self.drive.autonMove(8, 0, speed = .4, distance = 40, setLiftPosition = 0, intakeMode = 1)

                self.drive.autonMove(9, 0, speed = -.5, distance = 40)

                self.drive.autonMove(10, 1, turnSpeed = .75, turnAngle = -49, setLiftPosition = 2)

                self.drive.autonMove(11, 0, speed = 1, distance = 35, setLiftPosition = 2)

                self.drive.autonMove(12, 3, setLiftPosition = 2, intakeMode = 2)

                self.drive.autonMove(13, 0, speed = -1, distance = 40, setLiftPosition = 0)
            elif self.switchPosition == 'R':
                self.drive.autonMove(1, 0, speed = .6, distance = 12, setLiftPosition = 1)

                self.drive.autonMove(2, 1, turnAngle = 45, turnSpeed = .75)

                self.drive.autonMove(3, 0, speed = 1, distance = 42, setLiftPosition = 2)

                self.drive.autonMove(4, 1, turnAngle = -37, turnSpeed = .84, setLiftPosition = 2)

                self.drive.autonMove(5, 0, speed = .8, distance = 12, setLiftPosition = 2, intakeMode = 3)

                self.drive.autonMove(6, 0, speed = -.75, distance = 30, setLiftPosition = 0, intakeMode = 3)

                self.drive.autonMove(7, 1, turnSpeed = .65, turnAngle = -49)

                self.drive.autonMove(8, 0, speed = .4, distance = 40, intakeMode = 1)

                self.drive.autonMove(9, 0, speed = -.5, distance = 40)

                self.drive.autonMove(10, 1, turnSpeed = .75, turnAngle = 49, setLiftPosition = 2)

                self.drive.autonMove(11, 0, speed = 1, distance = 35, setLiftPosition = 2)

                self.drive.autonMove(12, 3, setLiftPosition = 2, intakeMode = 2)

                self.drive.autonMove(13, 0, speed = -1, distance = 40, setLiftPosition = 0)
            else:
                pass
