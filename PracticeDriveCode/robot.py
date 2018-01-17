"""
File Author: Jacob Harrelson
File Name: robot.py
File Creation Date: 1/8/2018
File Purpose: To create our drive functions
"""
import wpilib
from xbox import XboxController
from wpilib.drive import DifferentialDrive
from drive import driveTrain
#from operatorFunctions import operatorControl
from wpilib import RobotDrive

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.drive = driveTrain(self)
        self.controllerOne = XboxController(0)
        self.controllerTwo = XboxController(1)
        #self.speedLimiter = 1 #1 = standard speed, greater than 1 to slow down, less than 1 to speed up

        self.dashTimer = wpilib.Timer()# Timer for SmartDashboard updating
        self.dashTimer.start()

    def autonomousInit(self):
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        if self.auto_loop_counter < 100:#~50 loops a second
            self.drive.autonDrive(.5, -.5) # Drive forwards at half speed
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)
    def teleopPeriodic(self):
        self.drive.drivePass(self.controllerOne.getLeftY(), self.controllerOne.getRightY(), self.controllerOne.getLeftX(), self.controllerOne.getLeftBumper())
        #self.operatorControl.operate(self.controllerTwo.getLeftY, self.controllerTwo.getLeftX(), self.controllerTwo.getRightY(), self.controllerTwo.getRightX(), self.controllerTwo.getButtonA(),self.controllerTwo.getButtonB(), self.controllerTwo.getButtonX(), self.controllerTwo.getButtonY(), self.controllerTwo.getRightTrigger(), self.controllerTwo.getRightBumper(), self.controllerTwo.getLeftTrigger(), self.controllerTwo.getLeftBumper())
if __name__ == "__main__":
    wpilib.run(MyRobot)
