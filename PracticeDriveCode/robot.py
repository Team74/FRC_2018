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
import ctre
#import AutonHandling
import AutonInterpreter
#from operatorFunctions import operatorControl
from wpilib import RobotDrive

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.drive = driveTrain(self)
        self.controllerOne = XboxController(0)
        self.controllerTwo = XboxController(1)
        #self.speedLimiter = 1 #1 = standard speed, greater than 1 to slow down, less than 1 to speed up

        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(7)
        self.lbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(6)
        self.rfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)

        self.lfMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.lbMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.rfMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.rbMotor.configSelectedFeedbackSensor(0, 0, 0)

        self.lfMotor.setSensorPhase(True)
        self.lbMotor.setSensorPhase(True)
        self.rfMotor.setSensorPhase(False)
        self.rbMotor.setSensorPhase(False)

        self.lfMotor.setSelectedSensorPosition(0, 0, 0)
        self.lbMotor.setSelectedSensorPosition(0, 0, 0)
        self.rfMotor.setSelectedSensorPosition(0, 0, 0)
        self.rbMotor.setSelectedSensorPosition(0, 0, 0)

        self.dashTimer = wpilib.Timer()# Timer for SmartDashboard updating
        self.dashTimer.start()

    def autonomousInit(self):
        self.gameData=DriverStation.getInstance().getGameSpecificMessage()
        print(self.gameData)
        #print("autonInit")
        self.drive.zeroGyro()

        self.moveNumber = 1
        #self.auton = autonNearSwitch('left', 'left', self.drive)
        #self.auton = autonCenterEitherSwitch('left', 'left', self.drive)
        self.auton = autonTwoCubeScale('left', 'left', self.drive)

    def autonomousPeriodic(self):
        self.gameData=DriverStation.getInstance().getGameSpecificMessage()

        self.lfEncoderPosition = self.lfMotor.getSelectedSensorPosition(0)
        self.lbEncoderPosition = self.lbMotor.getSelectedSensorPosition(0)
        self.rfEncoderPosition = self.rfMotor.getSelectedSensorPosition(0)
        self.rbEncoderPosition = self.rbMotor.getSelectedSensorPosition(0)



        #self.auton.run()
        #self.AutonHandling.readCommandList(None, "square")


    def teleopPeriodic(self):
        print("Gyro Angle", self.drive.getGyroAngle())
        self.drive.drivePass(self.controllerOne.getLeftY(), self.controllerOne.getRightY(), self.controllerOne.getLeftX(), self.controllerOne.getLeftBumper())
        #self.operatorControl.operate(self.controllerTwo.getLeftY, self.controllerTwo.getLeftX(), self.controllerTwo.getRightY(), self.controllerTwo.getRightX(), self.controllerTwo.getButtonA(),self.controllerTwo.getButtonB(), self.controllerTwo.getButtonX(), self.controllerTwo.getButtonY(), self.controllerTwo.getRightTrigger(), self.controllerTwo.getRightBumper(), self.controllerTwo.getLeftTrigger(), self.controllerTwo.getLeftBumper())
if __name__ == "__main__":
    wpilib.run(MyRobot)
