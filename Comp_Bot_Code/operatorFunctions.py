"""
File Author: Jacob Harrelson
File Name: operator.py
File Creation Date: 1/11/2018
File Purpose: To create and run our operator functions
"""
import wpilib
from wpilib import Encoder, RobotDrive
from timeOut import *
import ctre
import math

class operatorFunctions():
    MIN_LIFT_HEIGHT = -100000000000000000000000000000000000000#Value in encoder codes
    MAX_LIFT_HEIGHT = 10000000000000000000000000000000000000#Value in encoder codes
    TIME_LEFT_UNTIL_ENDGAME = 105 * 50#105 is time in teleop before endgame, 50 is how many times our code's period
    TIME_TO_EJECT = 1#Value is in number of loops through the function and represents how long it takes to fully eject a cube with some to spare

    def __init__(self, robot, drive):
        self.time = timeOut()
        self.drive = drive
        #Set each motor to a talon
        #Note that these are theoretical and subject to change as of 1-13-2018
        self.liftMotor = ctre.wpi_talonsrx.WPI_TalonSRX(3)
        self.liftMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.liftMotor.setSelectedSensorPosition(0, 0, 0)

        self.winchMotorOne = ctre.wpi_victorspx.WPI_VictorSPX(6)
        self.winchMotorTwo = ctre.wpi_victorspx.WPI_VictorSPX(8)
        self.winchMotorThree = ctre.wpi_victorspx.WPI_VictorSPX(10)

        self.leftManipulatorMotor = ctre.wpi_victorspx.WPI_VictorSPX(7)
        self.rightManipulatorMotor = ctre.wpi_victorspx.WPI_VictorSPX(9)

        self.tilter = wpilib.DoubleSolenoid(20, 2, 3)

        self.doWeHaveACube = wpilib.DigitalInput(0)#Initilizes a proximity sensor used to see if we have a cube secured in the manipulator, sets it to read from digital input 0

        self.currentInput = None
        self.newInput = None

        self.compressor = wpilib.Compressor()
        self.compressor.setClosedLoopControl(True)

        self.winchMotorControlGroup = wpilib.SpeedControllerGroup(self.winchMotorOne, self.winchMotorTwo, self.winchMotorThree)
        self.firstEject = True#Says if it is our first time through the ejecting a cube in auton
    def operate(self, leftY, leftX, rightY, rightX, aButton, bButton, xButton, yButton, rightTrigger,rightBumper, leftTrigger, leftBumper, startButton, backButton):
        #Passes inputs from operator controller to the appropriate operator functions
        self.liftTilt(rightBumper, leftBumper)
        self.raiseLowerLift(leftY)
        self.winchUpDown(rightY)
        self.manipulatorIntake(aButton)
        self.ejectCube(xButton)
        self.deployClimber(startButton, backButton)

    def liftTest(self):
        print(self.liftMotor.getSelectedSensorPosition(0))

    def liftTilt(self, rightBumper, leftBumper):#Controls the tilt of the lift
        if leftBumper:
            if self.tilter.get() == 1:#Checks to see what position the lift is in and tilts accordingly
                self.tilter.set(2)
        if rightBumper:
            if self.tilter.get() == 2 or self.tilter.get() == 0:
                self.tilter.set(1)

    def raiseLowerLift(self, leftY):
        currentEncoderPosition = 50
        #currentEncoderPosition = self.liftMotor.getSelectedSensorPosition(0)
        if (currentEncoderPosition >= self.MIN_LIFT_HEIGHT) and (currentEncoderPosition <= (self.MAX_LIFT_HEIGHT - 250)):
            self.liftMotor.set(leftY)
        else:
            self.liftMotor.set(0)

    def printLiftEncoder(self):
        print(self.liftMotor.getSelectedSensorPosition(0))

    def autonRaiseLowerLift(self, setLiftPosition):#Note encoder values do not scale linearly with lift hieght
        currentEncoderPosition = 1
        #currentEncoderPosition = self.liftMotor.getSelectedSensorPosition(0)
        #Defines three set lift positions
        liftPositionOne = 1#Lift position when lift is all the way down in encoder values
        liftPositionTwo = 1#Lift position to place cubes on the switch in encoder values
        liftPositionThree = 1#Lift position to place cubes on the scale in encoder values
        #Reads the desiried lift position and sets how high we need to lift the lift
        if setLiftPosition == 0:
            liftHeight = liftPositionOne
        elif setLiftPosition == 1:
            liftHeight = liftPositionTwo
        elif setLiftPosition == 2:
            liftHeight = liftPositionThree
        if currentEncoderPosition <= (liftHeight + 250):
            self.liftMotor.set(math.sqrt(abs(1-(currentEncoderPosition/liftHeight))))
            return True
        elif currentEncoderPosition >= (liftHeight + 250):
            self.liftMotor.set((math.sqrt(abs(1-(currentEncoderPosition/liftHeight)))) * -1)
        else:
            self.liftMotor.set(0)
            return True

    def standaloneAutonRaiseLowerLift(self, setLiftPosition):
        currentEncoderPosition = 1
        #currentEncoderPosition = self.liftMotor.getSelectedSensorPosition(0)
        #Defines three set lift positions
        liftPositionOne = 1#Lift position when lift is all the way down in encoder values
        liftPositionTwo = 1#Lift position to place cubes on the switch in encoder values
        liftPositionThree = 1#Lift position to place cubes on the scale in encoder values
        #Reads the desiried lift position and sets how high we need to lift the lift
        if setLiftPosition == 0:
            liftHeight = liftPositionOne
        elif setLiftPosition == 1:
            liftHeight = liftPositionTwo
        elif setLiftPosition == 2:
            liftHeight = liftPositionThree
        if currentEncoderPosition <= (liftHeight + 250):
            self.liftMotor.set(math.sqrt(abs(1-(currentEncoderPosition/liftHeight))))
            return True
        else:
            self.liftMotor.set(0)
            return False
        return True
    def deployClimber(self, startButton, backButton):
            if (startButton or backButton) and (self.time.time >= self.TIME_LEFT_UNTIL_ENDGAME):#If start button or back button is pressed and we are in endgame, the climber will deploy
                pass
            else:
                pass

    def winchUpDown(self, rightY):#Operator can use right stick to raise the winch for climbing

        if self.time.time >= self.TIME_LEFT_UNTIL_ENDGAME:#Prevents climber from being deployed until the endgame starts
            #self.winchMotorControlGroup.set(rightY)
            pass
        else:
            self.winchMotorControlGroup.set((rightY * 1) * .5)#Testing only, remove when done

    def doWeHaveACube(self):
        self.cubeInManinpulator = self.doWeHaveACube.get()#Gets input from proximity sensor and setes it to self.cubeInManinpulator
        return self.cubeInManipulator

    def deBounceIntake(self, anyInput):
        waitTime = 4#Number in miiseconds, can only accept even numbers
        cycleTime = waitTime / 2
        stopTimer = 1
        if self.newInput != anyInput:
            self.newInput = anyInput
            stopTimer = 0
        else:
            stopTimer += 1
        if stopTimer > cycleTime:
            self.currentInput = self.newInput
        return self.currentInput
    def manipulatorIntake(self, aButton):#operator can toggle the intake using A, the intake will run until it detects that it has a cube, or the operator can toggle if off using A
        if aButton:#If a has been pressed, it will intake cubes
            self.leftManipulatorMotor.set(1)
            self.rightManipulatorMotor.set(-1)
        else:
            self.leftManipulatorMotor.set(0)
            self.rightManipulatorMotor.set(0)

    def ejectCube(self, xButton):#Ejects cube from the manipulator
        if self.xButton:#If X has been pressed, it will eject cubes
            self.leftManipulatorMotor.set(-1)
            self.rightManipulatorMotor.set(1)
        else:
            self.leftManipulatorMotor.set(0)
            self.rightManipulatorMotor.set(0)

    def startRunTimeClock(self):
        self.runTime = 0

    def autonIntakeControl(self, intakeMode):
        if intakeMode == 1:#Intake mode
            if self.doWeHaveACube():
                intakeMode = 0
            elif intakeMode == 1:
                self.leftManipulatorMotor.set(1)
                self.rightManipulatorMotor.set(-1)
                return True
            else:
                pass
        elif intakeMode == 2:#Eject Mode
            if self.firstEject:
                self.startRunTimeClock()
                self.firstEject = False
            if self.runTime <= self.TIME_TO_EJECT:
                self.leftManipulatorMotor.set(-1)
                self.rightManipulatorMotor.set(1)
                self.runTime += 1
                return True
            else:
                intakeMode = 0
            if intakeMode == 2:
                self.firstEject = True
        elif intakeMode == 0:#Neutral Mode
            self.leftManipulatorMotor.set(0)
            self.rightManipulatorMotor.set(0)
            return True

    def standaloneAutonIntakeControl(self, intakeMode):
        if intakeMode == 1:
            if intakeMode == 1:#Intake mode
                if self.doWeHaveACube():
                    return False
                elif intakeMode == 1:
                    self.leftManipulatorMotor.set(1)
                    self.rightManipulatorMotor.set(-1)
                    return True
                else:
                    pass
        if intakeMode == 2:
            if self.firstEject:
                self.startRunTimeClock()
                self.firstEject = False
            if self.runTime <= self.TIME_TO_EJECT:
                self.leftManipulatorMotor.set(-1)
                self.rightManipulatorMotor.set(1)
                self.runTime += 1
                return True
            else:
                self.firstEject = True
                return False
