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
from autonNearSwitch import *
from autonCenterEitherSwitch import *
from autonTwoCubeScale import *
from autonNearScale import *
import ctre
#import AutonHandling
import AutonInterpreter
#from operatorFunctions import operatorControl
from wpilib import RobotDrive
from wpilib.smartdashboard import SmartDashboard
from drive_2017 import driveTrain2017


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.drive = driveTrain2017(self)
        self.controllerOne = XboxController(0)
        self.controllerTwo = XboxController(1)
        self.speedLimiter = 1 #1 = standard speed, greater than 1 to slow down, less than 1 to speed up
        self.dashTimer = wpilib.Timer()     # Timer for SmartDashboard updating
        self.dashTimer.start()
        self.dash = SmartDashboard()
        #self.autonomous_modes = AutonomousModeSelector('autonomous', self.components)

        self.gameData=DriverStation.getInstance().getGameSpecificMessage()
        positionChooser = wpilib.SendableChooser()
        #positionChooser.addDefault('Position Chooser', '0')
        positionChooser.addObject('Left', '1')
        positionChooser.addObject('Right', '2')
        positionChooser.addObject('Center', '3')

        switchLscaleL = wpilib.SendableChooser()
        #switchLscaleL.addDefault('Switch and Scale LEFT', '0')
        switchLscaleL.addObject('Scale', '1')
        switchLscaleL.addObject('Switch', '2')
        switchLscaleL.addObject('PrepScaleScore', '3')
        switchLscaleL.addDefault('Drive', '4')##Create Default for all sendable Choosers

        switchRscaleR = wpilib.SendableChooser()
        #switchRscaleR.addDefault('Switch and Scale RIGHT', '0')
        switchRscaleR.addObject('Scale', '1')
        switchRscaleR.addObject('Switch', '2')
        switchRscaleR.addObject('PrepScaleScore', '3')
        switchRscaleR.addDefault('Drive', '4')

        switchRscaleL = wpilib.SendableChooser()
        #switchRscaleL.addDefault('Switch RIGHT, Scale LEFT', '0')
        switchRscaleL.addObject('Scale', '1')
        switchRscaleL.addObject('Switch', '2')
        switchRscaleL.addObject('PrepScaleScore', '3')
        switchRscaleL.addDefault('Drive', '4')

        switchLscaleR = wpilib.SendableChooser()
        #switchLscaleR.addDefault('Switch LEFT, Scale RIGHT', '0')
        switchLscaleR.addObject('Scale', '1')
        switchLscaleR.addObject('Switch', '2')
        switchLscaleR.addObject('PrepScaleScore', '3')
        switchLscaleR.addDefault('Drive', '4')

        #print('Dashboard Test')
        #self.dash.putData('Switch and Scale Left', switchLscaleL)
        #self.dash.putData('Switch Right, Scale Left', switchRscaleL)
        #self.dash.putData('Switch and Scale Right', switchRscaleR)
        wpilib.SmartDashboard.putData('Switch Right, Scale Left', switchRscaleL)
        #self.dash.putData('Switch Left, Scale Right', switchLscaleR)
        self.dash.putString('SanityCheck', '1')

        self.dashTimer = wpilib.Timer()# Timer for SmartDashboard updating
        self.dashTimer.start()

    def autonomousInit(self):


        '''
        #self.dash.updateValues()
        #print('Dashboard putData Test')


    def autonomousInit(self):
        self.gameData=DriverStation.getInstance().getGameSpecificMessage()

        print(self.gameData)
        #print("autonInit")
        self.drive.zeroGyro()
        '''
        #self.auton = autonNearSwitch('left', 'left', self.drive)
        self.auton = autonCenterEitherSwitch('left', 'left', self.drive)
        #self.auton = autonTwoCubeScale('left', 'left', self.drive)
        #self.auton = autonNearScale('left', 'left', self.drive)

    def autonomousPeriodic(self):
        self.gameData=DriverStation.getInstance().getGameSpecificMessage()

        self.auton.run()
        #self.AutonHandling.readCommandList(None, "square")

    def teleopPeriodic(self):
        print("Gyro Angle", self.drive.getGyroAngle())
        self.drive.drivePass(self.controllerOne.getLeftY(), self.controllerOne.getRightY(), self.controllerOne.getLeftX(), self.controllerOne.getLeftBumper())
        #self.operatorControl.operate(self.controllerTwo.getLeftY, self.controllerTwo.getLeftX(), self.controllerTwo.getRightY(), self.controllerTwo.getRightX(), self.controllerTwo.getButtonA(),self.controllerTwo.getButtonB(), self.controllerTwo.getButtonX(), self.controllerTwo.getButtonY(), self.controllerTwo.getRightTrigger(), self.controllerTwo.getRightBumper(), self.controllerTwo.getLeftTrigger(), self.controllerTwo.getLeftBumper())
if __name__ == "__main__":
    wpilib.run(MyRobot)
