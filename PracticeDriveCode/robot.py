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
from autonDrive import *
import ctre
#import AutonHandling
#import AutonInterpreter
#from operatorFunctions import operatorControl
from wpilib import RobotDrive
from wpilib.smartdashboard import SmartDashboard
from drive_2017 import driveTrain2017



class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        #self.drive = driveTrain(self)
        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.lbMotor = ctre.wpi_victorspx.WPI_VictorSPX(11)
        self.rfMotor = ctre.wpi_victorspx.WPI_VictorSPX(9)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)
        self.left=wpilib.SpeedControllerGroup(self.lfMotor, self.lbMotor)
        self.right=wpilib.SpeedControllerGroup(self.rfMotor, self.rbMotor)
        self.drive = DifferentialDrive(self.left, self.right)

        self.lfMotor.setNeutralMode(2)
        self.lbMotor.setNeutralMode(2)
        self.rfMotor.setNeutralMode(2)
        self.rbMotor.setNeutralMode(2)


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
        switchLscaleL.addDefault('Drive', '5')##Create Default for all sendable Choosers

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

    def autonomousInit(self):
        self.gameData=DriverStation.getInstance().getGameSpecificMessage()

        print(self.gameData)
        self.drive.zeroGyro()

        #self.auton = autonNearSwitch('left', 'left', 'left', self.drive)
        self.auton = autonCenterEitherSwitch('left', 'left', 'left', self.drive)
        #self.auton = autonTwoCubeScale('left', 'left', 'left', self.drive)
        #self.auton = autonNearScale('left', 'left', 'left', self.drive)

    def autonomousPeriodic(self):
        self.gameData=DriverStation.getInstance().getGameSpecificMessage()

        self.auton.run()
        #self.AutonHandling.readCommandList(None, "square")

    def teleopPeriodic(self):
        #print("Gyro Angle", self.drive.getGyroAngle())
        self.drive.arcadeDrive(self.controllerOne.getLeftY(), self.controllerOne.getRightX())
        #self.drive.drivePass(self.controllerOne.getLeftY(), self.controllerOne.getRightY(), self.controllerOne.getLeftX(), self.controllerOne.getLeftBumper(), self.controllerOne.getRightX(), self.controllerOne.getRightTrigger(), self.controllerOne.getLeftTrigger())
        #self.operatorControl.operate(self.controllerTwo.getLeftY, self.controllerTwo.getLeftX(), self.controllerTwo.getRightY(), self.controllerTwo.getRightX(), self.controllerTwo.getButtonA(),self.controllerTwo.getButtonB(), self.controllerTwo.getButtonX(), self.controllerTwo.getButtonY(), self.controllerTwo.getRightTrigger(), self.controllerTwo.getRightBumper(), self.controllerTwo.getLeftTrigger(), self.controllerTwo.getLeftBumper())
if __name__ == "__main__":
    wpilib.run(MyRobot)
