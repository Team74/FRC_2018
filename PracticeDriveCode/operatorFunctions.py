"""
File Author: Jacob Harrelson
File Name: operator.py
File Creation Date: 1/11/2018
File Purpose: To create and run our operator functions
"""
import wpilib
from wpilib import Encoder, RobotDrive

class operatorControl():

    def __init__(self, robot, drive):

        self.drive = drive
        #Set each motor to a talon
        #Note that these are theoretical and subject to change as of 1-13-2018
        self.liftMotorOne = ctre.wpi_talonsrx.WPI_TalonSRX(4)
        self.liftMotorTwo = ctre.wpi_talonsrx.WPI_TalonSRX(5)

        self.liftRotationMotor = ctre.wpi_talonsrx.WPI_TalonSRX(6)

        self.leftWinchMotorOne = ctre.wpi_talonsrx.WPI_TalonSRX(7)
        self.leftWinchMotorTwo = ctre.wpi_talonsrx.WPI_TalonSRX(8)

        self.rightWinchMotorOne = ctre.wpi_talonsrx.WPI_TalonSRX(9)
        self.rightWinchMotorTwo = ctre.wpi_talonsrx.WPI_TalonSRX(10)

        self.leftManipulatorMotor = ctre.wpi_talonsrx.WPI_TalonSRX(11)
        self.rightManipulatorMotor = ctre.wpi_talonsrx.WPI_TalonSRX(12)

        self.leftPlatformDeployMotor = ctre.wpi_talonsrx.WPI_TalonSRX(13)
        self.rightPlatformDeployMotor = ctre.wpi_talonsrx.WPI_TalonSRX(14)

        self.manipulatorFoldUpDownMotor = ctre.wpi_talonsrx.WPI_TalonSRX(15)

        self.manipulatorPowerCubeReleaseMotor = ctre.wpi_talonsrx.WPI_TalonSRX(16)

        self.doWeHaveACube = wpilib.DigitalInput(0)#Initilizes a proximity sensor used to see if we have a cube secured in the manipulator, sets it to read from digital input 0

        self.aToggle = False#Initilizes the A toggle to an off state
        #Set motors that are apired to do the same task to a control group
        #Note that these are theoretical and subject to change as of 1-13-2018

        self.liftMotorControlGroup = wpilib.SpeedControllerGroup(self.liftMotorOne, self.liftMotorTwo)

        self.leftWinchMotorControlGroup = wpilib.SpeedControllerGroup(self.leftWinchMotorOne, self.leftWinchMotorTwo)

        self.rightWinchMotorControlGroup = wpilib.SpeedControllerGroup(self.rightWinchMotorOne, self.rightWinchMotorTwo)

    def operate(aButton, bButton, xButton, yButton, leftY, leftX, rightY, rightX, rightTrigger, leftTrigger, rightBumper, leftBumper):
        self.raiseLowerLift(leftY)
        self.liftRotation(leftX)
        self.winchUp(rightY)
        self.manipulatorCubeRelease(whateverButtonThisEndsUpBeingInstanceOne)
        self.platformDeploy(whateverButtonThisEndsUpBeingInstanceTwo)
        self.manipulatorFold(whateverButtonThisEndsUpBeingInstanceThree)
        self.manipulatorIntake(aButton)

    def raiseLowerLift(self, leftY):
        self.liftMotorControlGroup.set(leftY)

    def liftRotation(self, leftX):
        self.liftRotationMotor.set(leftX)

    def winchUp(self, rightY):#Operator can use right stick to raise the winch for climbing
        #if rightY <= 0:#Allows for only positive values to be passed to the motors
            #rightY = rightY*-1
        self.leftWinchMotorControlGroup.set(rightY)
        self.rightWinchMotorControlGroup.set(rightY)

    def manipulatorCubeRelease(self, whateverButtonThisEndsUpBeingInstanceOne):
        pass

    def platformDeploy(self, whateverButtonThisEndsUpBeingInstanceTwo):
        pass

    def manipulatorFold(self, whateverButtonThisEndsUpBeingInstanceThree):
        pass
        
    def manipulatorIntake(self, aButton):#operator can toggle the intake using A, the intake will run until it detects that it has a cube, or the operator can toggle if off using A
        self.cubeInManinpulator = self.doWeHaveACube.get()#Gets input from proximity sensor and setes it to self.cubeInManinpulator
        if self.aButton:#Runs when a is pressed
            if self.aToggle:#If a has been toggled, it untoggles A
                self.aToggle = False
            else:#If a has not been toggled, it toggles A
                self.aToggle = True
        if self.aToggle and not self.cubeInManinpulator:#If A has been toggled and we have no cube, it will intake cubes
            self.leftManipulatorMotor.set(1)
            self.rightManipulatorMotor.set(-1)
