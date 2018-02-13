"""
File Author: Jacob Harrelson
File Name: operator.py
File Creation Date: 1/11/2018
File Purpose: To create and run our operator functions
"""
import wpilib
from wpilib import Encoder, RobotDrive
import timeOut
import ctre

class operatorControl():
    MIN_LIFT_HEIGHT = 'Some Value'#Value in encoder codes
    MAX_LIFT_HEIGHT = 'Some value'#Value in encoder codes
    TIME_LEFT_UNTIL_ENDGAME = 105 * 50#105 is time in teleop before endgame, 50 is how many times our code's period

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

    def operate(self, leftY, leftX, rightY, rightX, aButton, bButton, xButton, yButton, rightTrigger,rightBumper, leftTrigger, leftBumper, startButton, backButton):
        #Passes inputs from operator controller to the appropriate operator functions
        self.raiseLowerLift(leftY)
        self.winchUpDown(rightY)
        self.manipulatorIntake(aButton)
        self.ejectCube(xButton)
        self.deployClimber(startButton, backButton)

    def raiseLowerLift(self, leftY):
        currentEncoderPosition = self.liftMotor.getSelectedSensorPosition(0)
        if (currentEncoderPosition >= self.MIN_LIFT_HEIGHT) and (currentEncoderPosition <= self.MAX_LIFT_HEIGHT):
            self.liftMotor.set(leftY)
        else:
            self.liftMotor.set(0)

    def autonRaiseLowerLift(self, setLiftPosition):#Note encoder values do not scale linearly with lift hieght
        currentEncoderPosition = self.liftMotor.getSelectedSensorPosition(0)
        #Defines three set lift positions
        liftPositionOne = 0#Lift position when lift is all the way down in encoder values
        liftPositionTwo = x#Lift position to place cubes on the switch in encoder values
        liftPositionThree = y#Lift position to place cubes on the scale in encoder values
        #Reads the desiried lift position and sets how high we need to lift the lift
        if setLiftPosition == 1:
            liftHeight = liftPositionOne
        elif setLiftPosition == 2:
            liftHeight = liftPositionTwo
        elif setLiftPosition == 3:
            liftHeight = liftPositionThree
        self.liftMotor.set(math.sqrt(1-(currentEncoderPosition/liftHeight)))
        return True
    def deployClimber(self, startButton, backButton):
            if (startButton or backButton) and (self.timeOut.time >= self.TIME_LEFT_UNTIL_ENDGAME):#If start button or back button is pressed and we are in endgame, the climber will deploy
                pass
            else:
                pass

    def winchUpDown(self, rightY):#Operator can use right stick to raise the winch for climbing
        if self.timeOut.time >= self.TIME_LEFT_UNTIL_ENDGAME:#Prevents climber from being deployed until the endgame starts
            self.winchMotorControlGroup.set(rightY)
        else:
            pass

    def manipulatorIntake(self, aButton):#operator can toggle the intake using A, the intake will run until it detects that it has a cube, or the operator can toggle if off using A
        self.cubeInManinpulator = self.doWeHaveACube.get()#Gets input from proximity sensor and setes it to self.cubeInManinpulator
        if aButton:#Runs when A is pressed
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

    def autonIntakeControl(self, intakeMode):
        if intakeMode == 0:#Neutral Mode
            self.leftManipulatorMotor.set(-0)
            self.rightManipulatorMotor.set(0)
            return True
        elif intakeMode == 1:#Intake mode
            self.manipulatorIntake(True)
            return True
        elif intakeMode == 2:#Eject Mode
            self.leftManipulatorMotor.set(-1)
            self.rightManipulatorMotor.set(1)
            return True
