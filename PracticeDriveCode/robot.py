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
from autonSmartDashBoardInterpret import interpret

#import AutonHandling
#import Autoninterpret
#from operatorFunctions import operatorControl
from wpilib import RobotDrive
from wpilib.smartdashboard import SmartDashboard



class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.drive = driveTrain(self)
        self.interpret = interpret()

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
        positionChooser.addObject('left', 'left')
        positionChooser.addObject('right', 'right')
        positionChooser.addObject('center', 'center')

        switchLscaleL = wpilib.SendableChooser()
        switchLscaleL.addDefault('Switch and Scale LEFT', '1')
        switchLscaleL.addObject('Scale', 'scale')
        switchLscaleL.addObject('Switch', 'switch')
        #switchLscaleL.addObject('PrepScaleScore', '4')
        switchLscaleL.addDefault('Drive', 'drive')##Default for all sendable Choosers
        switchLscaleL.addObject('Two Cube Scale', 'Two Cube Scale')

        switchRscaleR = wpilib.SendableChooser()
        switchRscaleR.addDefault('Switch and Scale RIGHT', '1')
        switchRscaleR.addObject('Scale', 'scale')
        switchRscaleR.addObject('Switch', 'switch')
        #switchRscaleR.addObject('PrepScaleScore', '4')
        switchRscaleR.addDefault('Drive', 'drive')
        switchRscaleR.addObject('Two Cube Scale', 'Two Cube Scale')

        switchRscaleL = wpilib.SendableChooser()
        switchRscaleL.addDefault('Switch RIGHT, Scale LEFT', '1')
        switchRscaleL.addObject('Scale', 'scale')
        switchRscaleL.addObject('Switch', 'switch')
        #switchRscaleL.addObject('PrepScaleScore', '4')
        switchRscaleL.addDefault('Drive', 'drive')
        switchRscaleL.addObject('Two Cube Scale', 'Two Cube Scale')

        switchLscaleR = wpilib.SendableChooser()
        switchLscaleR.addDefault('Switch LEFT, Scale RIGHT', '1')
        switchLscaleR.addObject('Scale', 'scale')
        switchLscaleR.addObject('Switch', 'switch')
        #switchLscaleR.addObject('PrepScaleScore', '4')
        switchLscaleR.addDefault('Drive', 'drive')
        switchLscaleR.addObject('Two Cube Scale', 'Two Cube Scale')

        #print('Dashboard Test')
        wpilib.SmartDashboard.putData('Starting Position', positionChooser)
        wpilib.SmartDashboard.putData('Switch and Scale Left', switchLscaleL)
        wpilib.SmartDashboard.putData('Switch Right, Scale Left', switchRscaleL)
        wpilib.SmartDashboard.putData('Switch and Scale Right', switchRscaleR)
        wpilib.SmartDashboard.putData('Switch Left, Scale Right', switchRscaleL)
        #self.dash.putData('Switch Left, Scale Right', switchLscaleR)
        self.dash.putString('SanityCheck', '1')

        self.dashTimer = wpilib.Timer()# Timer for SmartDashboard updating
        self.dashTimer.start()
        #self.drive.encoderReset()

    def interperetDashboard(self):
        startingPosition = wpilib.SmartDashboard.getString('Starting Position', 'center')
        fieldLL = wpilib.SmartDashboard.getString('Switch and Scale Left', 'drive')
        fieldRL = wpilib.SmartDashboard.getString('Switch Right, Scale Left', 'drive')
        fieldRR = wpilib.SmartDashboard.getString('Switch and Scale Right', 'drive')
        fieldRL = wpilib.SmartDashboard.getString('Switch Left, Scale Right', 'drive')
        gameData = DriverStation.getInstance().getGameSpecificMessage()
        gameData = self.gameData[:-1]
        switchPosition = self.gameData[0]
        scalePosition = self.gameData[1]
        objective = 'drive'
        if gameData == 'LL':
            objective = fieldLL
        elif gameData == 'LR':
            objective = fieldLR
        elif gameData == 'RL':
            objective = fieldRL
        elif gameData == 'RR':
            objective = fieldRR
        else:
            objective = 'drive'
        if objective == 'switch':
            if (startingPosition == 'left' and switchPosition == 'L') or (startingPosition == 'right' and switchPosition == 'R'):
                self.auton = autonNearSwitch(startingPosition, switchPosition, scalePosition, self.drive)
            elif startingPosition == 'center':
                self.auton = autonCenterEitherSwitch(startingPosition, switchPosition, scalePosition, self.drive)
            elif (startingPosition == 'left' and switchPosition == 'R') or (startingPosition == 'right' and switchPosition == 'L'):
                self.auton = autonFarSwitch(startingPosition, switchPosition, scalePosition, self.drive)
        elif objective == 'scale':
            if (startingPosition == 'left' and scalePosition == 'L') or (startingPosition == 'right' and scalePosition == 'R'):
                self.auton = autonNearScale(startingPosition, switchPosition, scalePosition, self.drive)
            elif (startingPosition == 'left' and scalePosition == 'R') or (startingPosition == 'right' and scalePosition == 'L'):
                self.auton = autonFarScale(startingPosition, switchPosition, scalePosition, self.drive)
        elif objective == 'Two Cube Scale':
            if (startingPosition == 'left' and scalePosition == 'L') or (startingPosition == 'right' and scalePosition == 'R'):
                self.auton = autonTwoCubeSale(startingPosition, switchPosition, scalePosition, self.drive)
            elif (startingPosition == 'left' and scalePosition == 'R') or (startingPosition == 'right' and scalePosition == 'L'):
                self.auton = autonFarScale(startingPosition, switchPosition, scalePosition, self.drive)
        elif objective == 'drive':
            self.auton = autonDrive(startingPosition, switchPosition, scalePosition, self.drive)

    def autonomousInit(self):
        self.gameData=DriverStation.getInstance().getGameSpecificMessage()

        print(self.gameData)
        self.autonCounter = 0
        self.drive.zeroGyro()
        self.drive.resetMoveNumber()
        self.drive.autonShift('low')#Forces into low gear at start of auton
        print('reset moveNumber')
        #self.interperetDashboard()

        #self.auton = autonNearSwitch('right', 'R', 'L', self.drive)
        #self.auton = autonFarSwitch('left', 'R', 'L', self.drive)
        #self.auton = autonCenterEitherSwitch('center', 'L', 'L', self.drive)
        self.auton = autonCenterEitherSwitch('center', 'R', 'R', self.drive)
        #self.auton = autonTwoCubeScale('left', 'L', 'L', self.drive)
        #self.auton = autonNearScale('left', 'L', 'L', self.drive)
        #self.auton = autonDrive('any', 'any', 'any', self.drive)
    def autonomousPeriodic(self):
        self.gameData=DriverStation.getInstance().getGameSpecificMessage()
        #self.drive.printEncoderPosition()#Prints the position of the encoders
        #print(self.drive.getGyroAngle())
        if self.autonCounter >= 5:
            self.auton.run()
        else:
            self.autonCounter = self.autonCounter + 1
        #self.AutonHandling.readCommandList(None, "square")
        lfEncoderPosition = -(self.drive.lfMotor.getQuadraturePosition())
        rbEncoderPosition = self.drive.rbMotor.getQuadraturePosition()
        averageEncoder = (lfEncoderPosition + rbEncoderPosition) / 2
        wpilib.SmartDashboard.putNumber('Left Encoder Position', lfEncoderPosition)
        wpilib.SmartDashboard.putNumber('Right Encoder Position', rbEncoderPosition)
        wpilib.SmartDashboard.putNumber(' Average Encodes', averageEncoder)

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
