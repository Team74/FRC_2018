import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonCenterEitherSwitch(autonBaseInit):
    def run(self):
        if self.side == 'center':
            if self.switchPosition == 'L':
                self.drive.autonMove(1, 0, speed = .6, distance = 12, setLiftPosition = 0, intakeMode = 0)

                self.drive.autonMove(2, 1,turnAngle = -35, turnSpeed = .75, setLiftPosition = 0, intakeMode = 0)

                self.drive.autonMove(3, 0, 1, 44, 0, 0, 2, 0)

                self.drive.autonMove(4, 1, 0, 0, 40, .75, 2, 0)

                self.drive.autonMove(5, 0, 1, 6, 0, 0, 2, 2)

                self.drive.autonMove(6, 3, setLiftPosition = 2, intakeMode = 2)

                self.drive.autonMove(7, 0, speed = -1, distance = -40, setLiftPosition = 0)
            elif self.switchPosition == 'R':
                self.drive.autonMove(1, 0, .6, 12, 0, 0, 0, 0)

                self.drive.autonMove(2, 1, 0, 0, 45, .84, 0, 0)

                self.drive.autonMove(3, 0, 1, 58, 0, 0, 2, 0)

                self.drive.autonMove(4, 1, 0, 0, -40, .84, 2, 0)

                self.drive.autonMove(5, 0, 1, 2, 0, 0, 2, 2)

                self.drive.autonMove(6, 3, setLiftPosition = 2, intakeMode = 2)

                self.drive.autonMove(7, 0, speed = -1, distance = -40, setLiftPosition = 0)
            else:
                pass
