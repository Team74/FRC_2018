"""
File Author: Jacob Harrelson
File Name: operator.py
File Creation Date: 1/11/2018
File Purpose: To create and run our operator functions
"""
import wpilib
from wpilib import Encoder, RobotDrive
import timeOut

class operatorControl():

    def __init__(self, robot, drive):

        self.drive = drive
        #Set each motor to a talon
        #Note that these are theoretical and subject to change as of 1-13-2018
        self.liftMotor = ctre.wpi_talonsrx.WPI_TalonSRX(4)
        self.liftMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.liftMotor.setSelectedSensorPosition(0, 0, 0)

        self.winchMotorOne = ctre.wpi_talonsrx.WPI_TalonSRX(5)
        self.winchMotorTwo = ctre.wpi_talonsrx.WPI_TalonSRX(6)
        self.winchMotorThree = ctre.wpi_talonsrx.WPI_TalonSRX(7)

        self.leftManipulatorMotor = ctre.wpi_talonsrx.WPI_TalonSRX(8)
        self.rightManipulatorMotor = ctre.wpi_talonsrx.WPI_TalonSRX(9)

        self.doWeHaveACube = wpilib.DigitalInput(0)#Initilizes a proximity sensor used to see if we have a cube secured in the manipulator, sets it to read from digital input 0

        self.aToggle = False#Initilizes the A toggle to an off state
        self.xToggle = False#Initilizes the X toggle to an off state
        #Set motors that are apired to do the same task to a control group
        #Note that these are theoretical and subject to change as of 1-13-2018

        self.winchMotorControlGroup = wpilib.SpeedControllerGroup(self.winchMotorOne, self.winchMotorTwo, self.winchMotorThree)

    def operate(leftY, leftX, rightY, rightX, aButton, bButton, xButton, yButton, rightTrigger,rightBumper, leftTrigger, leftBumper, startButton, backButton):
        #Passes inputs from operator controller to the appropriate operator functions
        self.raiseLowerLift(leftY)
        self.winchUp(rightY)
        self.manipulatorIntake(aButton)
        self.ejectCube(xButton)
        self.deployClimber(startButton, backButton)

    def raiseLowerLift(self, leftY):
        self.liftMotor.set(leftY)

    def autonRaiseLowerLift(self, raiseHeight):#raiseHeight is in inches
    finalEncoderPosition = (raiseHeight/wheelCircumfrence)  * amount of encoder codes per rotation of the shaft after reductions
    math.sqrt(1-(currentEncoderPosition/finalEncoderPosition))
    def deployClimber(self, startButton, backButton):
            if (startButton or backButton) and (self.timeOut.time >= 5250):#If start button or back button is pressed and we are in endgame, the climber will deploy
                pass
            else:
                pass

    def winchUp(self, rightY):#Operator can use right stick to raise the winch for climbing
        if self.timeOut.time >= 5250:#Prevents climber from being deployed until the endgame starts
            self.winchMotorControlGroup.set(rightY)
        else:
            pass

    def manipulatorIntake(self, aButton):#operator can toggle the intake using A, the intake will run until it detects that it has a cube, or the operator can toggle if off using A
        self.cubeInManinpulator = self.doWeHaveACube.get()#Gets input from proximity sensor and setes it to self.cubeInManinpulator
        if self.aButton:#Runs when A is pressed
            if self.aToggle:#If A has been toggled, it untoggles A
                self.aToggle = False
            else:#If A has not been toggled, it toggles A
                self.aToggle = True
        if self.aToggle and not self.cubeInManinpulator:#If A has been toggled and we have no cube, it will intake cubes
            self.leftManipulatorMotor.set(1)
            self.rightManipulatorMotor.set(-1)

    def ejectCube(self, xButton):#Ejects cube from the manipulator
        if self.xButton:#Runs when X is pressed
            if self.xToggle:#If X has been toggled, it untoggles X
                self.xToggle = False
            else:#If X has not been toggled, it toggles X
                self.xToggle = True
        if self.xToggle:#If X has been toggled, it will eject cubes
            self.leftManipulatorMotor.set(-1)
            self.rightManipulatorMotor.set(1)
