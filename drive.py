"""
File Author: Jacob Harrelson
File Creation Date: 1/10/2018
File Purpose: To create and run our drive functions
"""

import wpilib
from wpilib.drive import DifferentialDrive

class driveTrain():

    def __init__(self, robot):
        self.lfMotor = wpilib.Talon(0)
        self.lbMotor = wpilib.Talon(1)
        self.rfMotor = wpilib.Talon(2)
        self.rbMotor = wpilib.Talon(3)

        self.left = wpilib.SpeedControllerGroup(self.lfMotor, self.lbMotor)
        self.right = wpilib.SpeedControllerGroup(self.rfMotor, self.rbMotor)

        self.robotDrive = DifferentialDrive(self.left, self.right)
    def drive(self, leftY, rightY):
        self.robotDrive.tankDrive(leftY, rightY)
