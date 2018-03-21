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
from operatorFunctions import *
from drive_2017 import driveTrain2017
from autonCenterEitherSwitchAngledTurningTesting import *
from autonNearSwitch import *
from autonCenterEitherSwitch import *
from autonFarSwitch import *
from autonTwoCubeScale import *
from autonNearScale import *
from autonDrive import *
from autonTurningTuning import *
from autonAngledTurnTesting import *
from autonLiftTest import *
import ctre
from robotpy_ext.common_drivers.navx.ahrs import AHRS
from autonSmartDashBoardInterpret import interpret
from AutonInterpreter import *
from timeOut import *
#import AutonHandling
#import Autoninterpret
from wpilib import RobotDrive
from wpilib.smartdashboard import SmartDashboard



class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.drive = driveTrain(self)
        self.time = timeOut()
        self.interpret = interpret()

        self.controllerOne = XboxController(0)
        self.controllerTwo = XboxController(1)
        self.speedLimiter = 1 #1 = standard speed, greater than 1 to slow down, less than 1 to speed up
        self.dashTimer = wpilib.Timer()     # Timer for SmartDashboard updating
        self.dashTimer.start()
        self.dash = SmartDashboard()

        self.positionChooser = wpilib.SendableChooser()
        self.positionChooser.addDefault('Position Chooser', '1')
        self.positionChooser.addObject('left', 'left')
        self.positionChooser.addObject('right', 'right')
        self.positionChooser.addObject('center', 'center')

        self.switchLscaleL = wpilib.SendableChooser()
        self.switchLscaleL.addDefault('Switch and Scale LEFT', '1')
        self.switchLscaleL.addObject('Scale', 'scale')
        self.switchLscaleL.addObject('Switch', 'switch')
        #switchLscaleL.addObject('PrepScaleScore', '4')
        self.switchLscaleL.addDefault('Drive', 'drive')##Default for all sendable Choosers
        self.switchLscaleL.addObject('Two Cube Scale', 'Two Cube Scale')

        self.switchRscaleR = wpilib.SendableChooser()
        self.switchRscaleR.addDefault('Switch and Scale RIGHT', '1')
        self.switchRscaleR.addObject('Scale', 'scale')
        self.switchRscaleR.addObject('Switch', 'switch')
        #switchRscaleR.addObject('PrepScaleScore', '4')
        self.switchRscaleR.addDefault('Drive', 'drive')
        self.switchRscaleR.addObject('Two Cube Scale', 'Two Cube Scale')

        self.switchRscaleL = wpilib.SendableChooser()
        self.switchRscaleL.addDefault('Switch RIGHT, Scale LEFT', '1')
        self.switchRscaleL.addObject('Scale', 'scale')
        self.switchRscaleL.addObject('Switch', 'switch')
        #switchRscaleL.addObject('PrepScaleScore', '4')
        self.switchRscaleL.addDefault('Drive', 'drive')
        self.switchRscaleL.addObject('Two Cube Scale', 'Two Cube Scale')

        self.switchLscaleR = wpilib.SendableChooser()
        self.switchLscaleR.addDefault('Switch LEFT, Scale RIGHT', '1')
        self.switchLscaleR.addObject('Scale', 'scale')
        self.switchLscaleR.addObject('Switch', 'switch')
        #switchLscaleR.addObject('PrepScaleScore', '4')
        self.switchLscaleR.addDefault('Drive', 'drive')
        self.switchLscaleR.addObject('Two Cube Scale', 'Two Cube Scale')

        #print('Dashboard Test')
        wpilib.SmartDashboard.putData('Starting Position', self.positionChooser)
        wpilib.SmartDashboard.putData('Switch and Scale Left', self.switchLscaleL)
        wpilib.SmartDashboard.putData('Switch Right, Scale Left', self.switchRscaleL)
        wpilib.SmartDashboard.putData('Switch and Scale Right', self.switchRscaleR)
        wpilib.SmartDashboard.putData('Switch Left, Scale Right', self.switchLscaleR)
        #self.dash.putData('Switch Left, Scale Right', switchLscaleR)
        self.dash.putString('SanityCheck', '1')

        self.dashTimer = wpilib.Timer()# Timer for SmartDashboard updating
        self.dashTimer.start()
        #self.drive.encoderReset()

    def interperetDashboard(self):
        startingPosition = self.positionChooser.getSelected()
        gameData = DriverStation.getInstance().getGameSpecificMessage()
        gameData = gameData[:-1]
        gameData = gameData.upper()
        switchPosition = gameData[0]
        scalePosition = gameData[1]
        objective = 'drive'
        if gameData == 'LL':
            objective = self.switchLscaleL.getSelected()
        elif gameData == 'LR':
            objective = self.switchLscaleR.getSelected()
        elif gameData == 'RL':
            objective = self.switchRscaleL.getSelected()
        elif gameData == 'RR':
            objective = self.switchRscaleR.getSelected()
        else:
            objective = 'drive'
        print(gameData)
        print(startingPosition)
        print(switchPosition)
        print(scalePosition)
        print(objective)
        if objective == 'switch':
            if (startingPosition == 'left' and switchPosition == 'L') or (startingPosition == 'right' and switchPosition == 'R'):
                self.auton = autonNearSwitch(startingPosition, switchPosition, scalePosition, self.drive)
            elif startingPosition == 'center':
                self.auton = autonCenterEitherSwitch(startingPosition, switchPosition, scalePosition, self.drive)
            elif (startingPosition == 'left' and switchPosition == 'R') or (startingPosition == 'right' and switchPosition == 'L'):
                #self.auton = autonFarSwitch(startingPosition, switchPosition, scalePosition, self.drive)
                self.auton = autonDrive('any', 'any', 'any', self.drive)
        elif objective == 'scale':
            if (startingPosition == 'left' and scalePosition == 'L') or (startingPosition == 'right' and scalePosition == 'R'):
                self.auton = autonNearScale(startingPosition, switchPosition, scalePosition, self.drive)
            elif (startingPosition == 'left' and scalePosition == 'R') or (startingPosition == 'right' and scalePosition == 'L'):
                #self.auton = autonFarScale(startingPosition, switchPosition, scalePosition, self.drive)
                self.auton = autonDrive('any', 'any', 'any', self.drive)
        elif objective == 'Two Cube Scale':
            if (startingPosition == 'left' and scalePosition == 'L') or (startingPosition == 'right' and scalePosition == 'R'):
                self.auton = autonTwoCubeSale(startingPosition, switchPosition, scalePosition, self.drive)
            elif (startingPosition == 'left' and scalePosition == 'R') or (startingPosition == 'right' and scalePosition == 'L'):
                self.auton = autonFarScale(startingPosition, switchPosition, scalePosition, self.drive)
        elif objective == 'drive':
            self.auton = autonDrive(startingPosition, switchPosition, scalePosition, self.drive)
        print(self.auton)

    def autonomousInit(self):
        self.autonCounter = 0
        self.drive.zeroGyro()
        self.drive.resetMoveNumber()
        self.drive.autonShift('low')#Forces into low gear at start of auton
        self.drive.operate.liftTilt(False, True)
        #print('reset moveNumber')
        self.interperetDashboard()
        #self.auton = AutonInterpreter(3,3,3,self.drive)
        #self.auton = autonAngledTurnTesting('any', 'any', 'any', self.drive)
        #self.auton = autonLiftTest('any', 'any', 'any', self.drive)
        #self.auton = autonTurningTuning('any', 'any', 'any', self.drive)
        #self.auton = autonNearSwitch('right', 'R', 'L', self.drive)
        #self.auton = autonFarSwitch('left', 'R', 'L', self.drive)
        #self.auton = autonCenterEitherSwitch('center', 'R', 'L', self.drive)
        #self.auton = autonCenterEitherSwitch('center', 'L', 'R', self.drive)
        #self.auton = autonTwoCubeScale('left', 'L', 'L', self.drive)
        #self.auton = autonNearScale('left', 'L', 'L', self.drive)
        #self.auton = autonDrive('any', 'any', 'any', self.drive)
        #self.auton = autonCenterEitherSwitchAngledTurningTesting('left', 'L', 'L', self.drive)
    def autonomousPeriodic(self):
        self.drive.operate.liftTilt(False, True)
        self.drive.autonShift('low')#Keeps it in low gear during auton
        #self.drive.printEncoderPosition()#Prints the position of the encoders
        #print(self.drive.getGyroAngle())
        if self.autonCounter >= 40:
            self.auton.run()
        else:
            self.drive.operate.liftTilt(False, True)
            self.drive.operate.autonIntakeControl(1)
            self.autonCounter = self.autonCounter + 1
        #self.AutonHandling.readCommandList(None, "square")
        wpilib.SmartDashboard.putNumber('Left Velocity', self.drive.lbMotor.getQuadratureVelocity())
        wpilib.SmartDashboard.putNumber('Right Velocity', self.drive.rbMotor.getQuadratureVelocity())
        wpilib.SmartDashboard.putNumber('Gyro Angle', self.drive.getGyroAngle())
        #self.drive.printer()
    def teleopPeriodic(self):
        wpilib.SmartDashboard.putNumber('Lift Encoder', self.drive.operate.liftMotor.getSelectedSensorPosition(0))
        #self.drive.operate.printLiftOutputCurrent()
        wpilib.SmartDashboard.putNumber('Left Drive Encoders', -(self.drive.lbMotor.getQuadraturePosition()))
        wpilib.SmartDashboard.putNumber('Right Drive Encders', self.drive.rbMotor.getQuadraturePosition())
        wpilib.SmartDashboard.putNumber('Left Velocity', self.drive.lbMotor.getQuadratureVelocity())
        wpilib.SmartDashboard.putNumber('Right Velocity', self.drive.rbMotor.getQuadratureVelocity())
        wpilib.SmartDashboard.putNumber('Left Current', self.drive.lbMotor.getOutputCurrent())
        wpilib.SmartDashboard.putNumber('Right Current', self.drive.rbMotor.getOutputCurrent())
        #print("Gyro Angle  ", self.drive.getGyroAngle())
        wpilib.SmartDashboard.putNumber('Gyro Angle', self.drive.getGyroAngle())
        #wpilib.SmartDashboard.putNumber('Number of Shits', self.drive.shiftCounterReturn())
        #wpilib.SmartDashboard.putString('Gear Mode', self.drive.gearMode())
        #self.drive.printer()
        #self.drive.operate.liftTest()
        self.drive.drivePass(self.controllerOne.getLeftY(), self.controllerOne.getRightY(), self.controllerOne.getLeftBumper(), self.controllerOne.getRightBumper(), self.controllerOne.getButtonA())
        self.drive.operate.operate(self.controllerTwo.getLeftY(), self.controllerTwo.getLeftX(), self.controllerTwo.getRightY(), self.controllerTwo.getRightX(), self.controllerTwo.getButtonA(),self.controllerTwo.getButtonB(), self.controllerTwo.getButtonX(), self.controllerTwo.getButtonY(), self.controllerTwo.getRightTrigger(), self.controllerTwo.getRightBumper(), self.controllerTwo.getLeftTrigger(), self.controllerTwo.getLeftBumper(), self.controllerTwo.getStart(), self.controllerTwo.getBack())
        #self.time.time += 1
if __name__ == "__main__":
    wpilib.run(MyRobot)
