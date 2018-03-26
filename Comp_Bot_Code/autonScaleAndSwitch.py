import wpilib
from drive import driveTrain
from autonBaseInit import *

class autonScaleAndSwitch(autonBaseInit):
#def autonMove(moveNumberPass, commandNumber, speed, distance, turnAngle, turnspeed, liftposition, intakemode):
    def run(self):
        if self.side == 'left' and self.scalePosition == 'L' and self.switchPosition == 'L':
            self.drive.autonMove(1, 0, speed = 1, distance = 230, setLiftPosition = 3, gear = 'high')

            self.drive.autonMove(2, 1, turnangle = 38, turnSpeed = .75, setLiftPosition = 3, gear = 'low')

            self.drive.autonMove(3, 0, speed = 1, distance = 5, setLiftPosition = 3, gear = 'low')

            self.drive.autonMove(4, 3,  setLiftPosition = 3, intakeMode = 2)

            self.drive.autonMove(5, 1, turnagle = 135, turnSpeed = .75, setLiftPosition = 0)

            self.drive.autonMove(6, 0, speed = 75, distance = 42, setLiftPosition = 0, intakeMode = 1)
        elif self.side == 'right' and self.scalePosition == 'R' and self.switchPosition == 'R':
            self.drive.autonMove(1, 0, speed = 1, distance = 230, setLiftPosition = 3, gear = 'high')

            self.drive.autonMove(2, 1, turnangle = -38, turnSpeed = .75, setLiftPosition = 3, gear = 'low')

            self.drive.autonMove(3, 0, speed = 1, distance = 5, setLiftPosition = 3, gear = 'low')

            self.drive.autonMove(4, 3, setLiftPosition = 3, intakeMode = 2)

            self.drive.autonMove(5, 1, 0, 0, -135, .5, 0, 0)

            self.drive.autonMove(6, 0, .75, 42, 0, 0, 0, 0)
