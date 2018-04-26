import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonNearSwitch(autonBaseInit):
    def run(self):
        if self.side == 'left' and self.switchPosition == 'L':
            self.drive.autonMove(1, 0, speed = 1, distance = 95, setLiftPosition = 2)

            self.drive.autonMove(2, 1, turnAngle = 89, turnSpeed = .75, setLiftPosition = 2)

            self.drive.autonMove(3, 0, speed = .5, distance = 10, setLiftPosition = 2)

            self.drive.autonMove(4, 0, speed = -.6, distance = 15, setLiftPosition = 2, intakeMode = 3)
            '''
            self.drive.autonMove(5, 1, turnAngle = 90, turnSpeed = .7, setLiftPosition = 0)
            if self.scalePosition == 'R':
                self.drive.autonMove(6, 0, speed = -.5, distance = 16, setLiftPosition = 0)

                self.drive.autonMove(7, 1, turnAngle = -25, turnSpeed = .65, setLiftPosition = 0)

                self.drive.autonMove(8, 0, speed = .5, distance = 25, setLiftPosition = 0, intakeMode = 1)

                self.drive.autonMove(9, 0, speed = -.5, distance = 15, setLiftPosition = 2, intakeMode = 0)

                self.drive.autonMove(10, 0, speed = .5, distance = 15, setLiftPosition = 2)

                self.drive.autonMove(11, 3, setLiftPosition = 2, intakeMode = 3)
            '''
        elif self.side == 'right' and self.switchPosition == 'R':
            self.drive.autonMove(1, 0, speed = 1, distance = 95, setLiftPosition = 2)

            self.drive.autonMove(2, 1, turnAngle = -89, turnSpeed = .75, setLiftPosition = 2)

            self.drive.autonMove(3, 0, speed = .5, distance = 10, setLiftPosition = 2)

            self.drive.autonMove(4, 0, speed = -.6, distance = 15, setLiftPosition = 2, intakeMode = 3)
            '''
            self.drive.autonMove(5, 1, turnAngle = -90, turnSpeed = .7, setLiftPosition = 0)
            if self.scalePosition == 'L':
                self.drive.autonMove(6, 0, speed = -.5, distance = 16, setLiftPosition = 0)

                self.drive.autonMove(7, 1, turnAngle = 25, turnSpeed = .65, setLiftPosition = 0)

                self.drive.autonMove(8, 0, speed = .5, distance = 25, setLiftPosition = 0, intakeMode = 1)

                self.drive.autonMove(9, 0, speed = -.5, distance = 15, setLiftPosition = 2, intakeMode = 0)

                self.drive.autonMove(10, 0, speed = .5, distance = 15, setLiftPosition = 2)
            '''
        else:
            pass
