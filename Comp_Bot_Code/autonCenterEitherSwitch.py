import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonCenterEitherSwitch(autonBaseInit):
    def run(self):
        if self.side == 'center':
            if self.switchPosition == 'L':
                self.drive.autonMove(1, 0, speed = .6, distance = 12, setLiftPosition = 0, intakeMode = 0)

                self.drive.autonMove(2, 1,turnAngle = -35, turnSpeed = .5, setLiftPosition = 0, intakeMode = 0)

                self.drive.autonMove(3, 0, 1, 65, 0, 0, 2, 0)

                self.drive.autonMove(4, 1, 0, 0, 48, .5, 2, 0)

                self.drive.autonMove(5, 0, .5, 10, 0, 0, 2, 0)

                self.drive.autonMove(6, 0, 0, 1000, 0, 0, 2, 2)

                self.drive.autonMove(7, 4, 0, 0, 0, 0, 0, 0)
            elif self.switchPosition == 'R':
                self.drive.autonMove(1, 0, .6, 12, 0, 0, 0, 0)

                self.drive.autonMove(2, 1, 0, 0, 45, .5, 0, 0)

                self.drive.autonMove(3, 0, 1, 55, 0, 0, 2, 0)

                self.drive.autonMove(4, 1, 0, 0, -45, .5, 2, 0)

                self.drive.autonMove(5, 0, .75, 5, 0, 0, 2, 2)

                self.drive.autonMove(6, 0, 0, 1000, 0, 0, 2, 2)

                self.drive.autonMove(7, 4, 0, 0, 0, 0, 0, 0)
            else:
                pass
