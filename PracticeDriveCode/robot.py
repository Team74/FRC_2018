"""
File Author: Jacob Harrelson
File Creation Date: 1/8/2018
File Purpose: To create our drive functions
"""
import wpilib
from xbox import XboxController
from drive import driveTrain
from wpilib import RobotDrive
from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.drive = driveTrain(self)
        self.controller = XboxController(0)

        #self.speedLimiter = 1 #1 = standard speed, greater than 1 to slow down, less than 1 to speed up

        self.dashTimer = wpilib.Timer()# Timer for SmartDashboard updating
        self.dashTimer.start()

    def teleopPeriodic(self):
        self.drive.drive(self.controller.getLeftY(),self.controller.getRightY())

if __name__ == "__main__":
    wpilib.run(MyRobot)
