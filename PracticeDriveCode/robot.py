"""
File Author: Jacob Harrelson
File Name: robot.py
File Creation Date: 1/8/2018
File Purpose: To create our drive functions
"""
import wpilib
from xbox import XboxController
from wpilib.drive import DifferentialDrive
from wpilib import DriverStation
from drive import driveTrain
from drive_2017 import driveTrain2017
from autonNearSwitch import *
from autonCenterEitherSwitch import *
from autonFarSwitch import *
from autonTwoCubeScale import *
from autonNearScale import *
from autonDrive import *
import ctre
from robotpy_ext.common_drivers.navx.ahrs import AHRS

#import AutonHandling
#import AutonInterpreter
#from operatorFunctions import operatorControl
from wpilib import RobotDrive
from wpilib.smartdashboard import SmartDashboard



class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.drive = driveTrain(self)

        self.controllerOne = XboxController(0)
        self.controllerTwo = XboxController(1)
        self.speedLimiter = 1 #1 = standard speed, greater than 1 to slow down, less than 1 to speed up
        self.dashTimer = wpilib.Timer()     # Timer for SmartDashboard updating
        self.dashTimer.start()
        self.dash = SmartDashboard()
        #self.autonomous_modes = AutonomousModeSelector('autonomous', self.components)

        self.gameData=DriverStation.getInstance().getGameSpecificMessage()


        positionChooser = wpilib.SendableChooser()
        positionChooser.addDefault('Position Chooser', '1')
        positionChooser.addObject('Left', '2')
        positionChooser.addObject('Right', '3')
        positionChooser.addObject('Center', '4')

        switchLscaleL = wpilib.SendableChooser()
        switchLscaleL.addDefault('Switch and Scale LEFT', '1')
        switchLscaleL.addObject('Scale', '2')
        switchLscaleL.addObject('Switch', '3')
        switchLscaleL.addObject('PrepScaleScore', '4')
        switchLscaleL.addDefault('Drive', '5')##Default for all sendable Choosers

        switchRscaleR = wpilib.SendableChooser()
        switchRscaleR.addDefault('Switch and Scale RIGHT', '1')
        switchRscaleR.addObject('Scale', '2')
        switchRscaleR.addObject('Switch', '3')
        switchRscaleR.addObject('PrepScaleScore', '4')
        switchRscaleR.addDefault('Drive', '5')

        switchRscaleL = wpilib.SendableChooser()
        switchRscaleL.addDefault('Switch RIGHT, Scale LEFT', '1')
        switchRscaleL.addObject('Scale', '2')
        switchRscaleL.addObject('Switch', '3')
        switchRscaleL.addObject('PrepScaleScore', '4')
        switchRscaleL.addDefault('Drive', '5')

        switchLscaleR = wpilib.SendableChooser()
        switchLscaleR.addDefault('Switch LEFT, Scale RIGHT', '1')
        switchLscaleR.addObject('Scale', '2')
        switchLscaleR.addObject('Switch', '3')
        switchLscaleR.addObject('PrepScaleScore', '4')
        switchLscaleR.addDefault('Drive', '5')

        #print('Dashboard Test')
        wpilib.SmartDashboard.putData('Starting Position', positionChooser)
        wpilib.SmartDashboard.putData('Switch and Scale Left', switchLscaleL)
        wpilib.SmartDashboard.putData('Switch Right, Scale Left', switchRscaleL)
        wpilib.SmartDashboard.putData('Switch and Scale Right', switchRscaleR)
        wpilib.SmartDashboard.putData('Switch Right, Scale Left', switchRscaleL)
        #self.dash.putData('Switch Left, Scale Right', switchLscaleR)
        self.dash.putString('SanityCheck', '1')

        self.dashTimer = wpilib.Timer()# Timer for SmartDashboard updating
        self.dashTimer.start()
        self.drive.encoderReset()
    def autonomousInit(self):
        self.gameData=DriverStation.getInstance().getGameSpecificMessage()

        print(self.gameData)
        self.autonCounter = 0
        self.drive.zeroGyro()
        self.drive.resetMoveNumber()
        self.drive.autonShift('low')
        print('reset moveNumber')
        #self.interprater.interprate(self)

        #self.auton = autonNearSwitch('left', 'L', 'L', self.drive)
        #self.auton = autonFarSwitch('left', 'R', 'L', self.drive)
        #self.auton = autonCenterEitherSwitch('center', 'L', 'L', self.drive)
        #self.auton = autonCenterEitherSwitch('center', 'R', 'R', self.drive)
        #self.auton = autonTwoCubeScale('left', 'L', 'L', self.drive)
        #self.auton = autonNearScale('left', 'L', 'L', self.drive)
        self.auton = autonDrive('any', 'any', 'any', self.drive)
    def autonomousPeriodic(self):
        self.gameData=DriverStation.getInstance().getGameSpecificMessage()
        #self.drive.printEncoderPosition()#Prints the position of the encoders
        #print(self.drive.getGyroAngle())
        if self.autonCounter >= 5:
            self.auton.run()
        else:
            self.autonCounter = self.autonCounter + 1
        #self.AutonHandling.readCommandList(None, "square")

    def teleopPeriodic(self):
        lfEncoderPosition = -(self.drive.lfMotor.getQuadraturePosition())
        rfEncoderPosition = self.drive.rbMotor.getQuadraturePosition()
        #self.drive.printEncoderPosition()
        #print(self.drive.getGyroAngle())
        wpilib.SmartDashboard.putNumber('Left Encoder Position', lfEncoderPosition)
        wpilib.SmartDashboard.putNumber('Right Encoder Position', rfEncoderPosition)
        self.drive.drivePass(self.controllerOne.getLeftY(), self.controllerOne.getRightX(), self.controllerOne.getLeftBumper(), self.controllerOne.getRightBumper(), self.controllerOne.getButtonA())
        #self.operatorControl.operate(self.controllerTwo.getLeftY, self.controllerTwo.getLeftX(), self.controllerTwo.getRightY(), self.controllerTwo.getRightX(), self.controllerTwo.getButtonA(),self.controllerTwo.getButtonB(), self.controllerTwo.getButtonX(), self.controllerTwo.getButtonY(), self.controllerTwo.getRightTrigger(), self.controllerTwo.getRightBumper(), self.controllerTwo.getLeftTrigger(), self.controllerTwo.getLeftBumper())
if __name__ == "__main__":
    wpilib.run(MyRobot)
