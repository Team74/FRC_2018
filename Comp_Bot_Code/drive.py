"""
File Author: Jacob Harrelson
File Name: drive.py
File Creation Date: 1/10/2018
File Purpose: To create and run our drive functions
"""

import wpilib
import robotpy_ext
from robotpy_ext.common_drivers.navx.ahrs import AHRS
from wpilib.drive import DifferentialDrive
from wpilib import RobotDrive
from operatorFunctions import *
import ctre
import math

class driveTrain():
    #MOTOR_SPEED_CONTROL = .87#Practice base
    MOTOR_SPEED_CONTROL = 1#Comp Base
    ENCODER_CODES_PER_REV = 5000#Comp Base
    #ENCODER_CODES_PER_REV = 5887#Practice Base
    WHEEL_CIRCUMFERENCE = 12.5663706144#Comp Base
    #WHEEL_CIRCUMFERENCE = 18.849#Practice base
    RIGHT_MOTOR_BIAS = .9

    def __init__(self, robot):
        self.operate = operatorFunctions(drive = self, robot = robot)#Creates the operator functions
        self.gyro = AHRS.create_spi()

        self.shifter = wpilib.DoubleSolenoid(20, 0, 1)#Initilizes the shifter's solenoid and sets it to read fron digital output 0
        """Sets drive motors to a cantalon or victor"""
        self.lbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.lfMotor = ctre.wpi_victorspx.WPI_VictorSPX(4)
        self.rfMotor = ctre.wpi_victorspx.WPI_VictorSPX(5)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)

        self.lfMotor.setNeutralMode(2)
        self.lbMotor.setNeutralMode(2)
        self.rfMotor.setNeutralMode(2)
        self.rbMotor.setNeutralMode(2)

        self.left = wpilib.SpeedControllerGroup(self.lfMotor, self.lbMotor)
        self.right = wpilib.SpeedControllerGroup(self.rfMotor, self.rbMotor)
        self.drive = DifferentialDrive(self.left, self.right)

        self.firstTime = True#Check for autonDriveStraight
        self.firstRun = True#Check for autonPivot
        self.firstAngleTurn = True#Check for first angled turn

        self.oldGyro = 0

        self.moveNumber = 1
        self.shiftCounter = 0
        self.instantiateEncoders()

    def instantiateEncoders(self):
        self.lbMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.rbMotor.configSelectedFeedbackSensor(0, 0, 0)

        self.lbMotor.setSensorPhase(True)

    def drivePass(self, leftY, rightY, leftBumper, rightBumper, leftTrigger, rightTrigger, aButton, bButton, xButton, yButton, dpadAngle, startButton, backButton):
        self.shift(leftBumper, rightBumper)
        self.manualEncoderReset(aButton)
        self.scaleInputs(-leftY, -rightY, rightTrigger)
        #self.samsStupidExperimentalDrive(leftBumper, rightBumper, leftTrigger, rightTrigger, aButton, bButton, xButton, yButton, dpadAngle)
        #self.shift(startButton, backButton)
    def scaleInputs(self,leftY, rightY, rightTrigger):
        leftOutput = leftY
        rightOutput = rightY
        if rightTrigger:
            leftOutput = leftOutput / 1.8
            rightOutput = rightOutput / 1.8
        self.tankDrive(leftOutput, rightOutput)

    def tankDrive(self, leftY, rightY):
        self.drive.tankDrive(leftY * self.MOTOR_SPEED_CONTROL, rightY * self.MOTOR_SPEED_CONTROL, True)#True squares the inputs, further testing requiered on weather that is a good idea

    def shift(self, leftBumper, rightBumper):
        if leftBumper:#When left bumper is pressed we shift gears
            if self.shifter.get() == 1:#Checks to see what gear we are in and shifts accordingly
                self.shifter.set(2)
        if rightBumper:
            if self.shifter.get() == 2 or self.shifter.get() == 0:
                self.shifter.set(1)

    def getGyroAngle(self):
    	return (self.gyro.getAngle()-self.oldGyro)

    def zeroGyro(self):
        self.gyro.reset()
        while(abs(self.getGyroAngle()) > 340):
            self.gyro.reset()

    def encoderReset(self):
        self.lbMotor.setQuadraturePosition(0, 0)
        self.rbMotor.setQuadraturePosition(0, 0)

    def printEncoderPosition(self):
        lbEncoder = -(self.lbMotor.getQuadraturePosition())
        rbEncoder = self.rbMotor.getQuadraturePosition()
        distanceDrivenInches = (lbEncoder / self.ENCODER_CODES_PER_REV) * self.WHEEL_CIRCUMFERENCE
        averageEncoders = (lbEncoder + rbEncoder) / 2

    def manualEncoderReset(self, aButton):
        if aButton:
            self.lbMotor.setQuadraturePosition(0, 0)
            self.rbMotor.setQuadraturePosition(0, 0)
        else:
            pass

    def autonShift(self, gear):
        if gear == 'low':
            if self.shifter.get() == 1 or self.shifter.get() == 0:
                self.shifter.set(2)
                #return False
        elif gear == 'high':
            if self.shifter.get() == 2 or self.shifter.get() == 0:
                self.shifter.set(1)
                #return False
        else:
            pass

    def autonAngledTurn(self, radius, turnAngle, turnSpeed):
        if self.firstAngleTurn:#Checks for first time through the function to only reset encoders on the first time
            self.oldGyro = self.gyro.getAngle()
            self.oldPositionLeft =  (self.lbMotor.getQuadraturePosition())
            self.oldPositionRight =  -(self.rbMotor.getQuadraturePosition())
            self.autonCounter = 0
            self.firstAngleTurn = False
        robotSpeedFeetPerSecond = 8
        robotSpeedInchesPerSecond = robotSpeedFeetPerSecond * 12
        wheelWidth = 24.3
        wheelDistanceFromCenter = wheelWidth / 2
        overallCircumference = 2 * (3.14159265 * radius)
        circlePercentage = 360 / turnAngle
        if turnAngle > 0:#IF we are turning right, the left wheels have to travel further
            leftTurnDistance = (overallCircumference + (2 * 3.14159265 * wheelDistanceFromCenter)) / circlePercentage
            rightTurnDistance = (overallCircumference - (2 * 3.14159265 * wheelDistanceFromCenter)) / circlePercentage
            leftSpeed = turnSpeed
            turnTime = (leftTurnDistance / robotSpeedInchesPerSecond)
            rightSpeed = (rightTurnDistance / turnTime)
            rightSpeedPercentage = (rightSpeed / leftSpeed)
            leftTurnSpeed = leftSpeed
            rightTurnSpeed = rightSpeedPercentage
            if turnAngle > self.getGyroAngle():
                self.drive.tankDrive(leftTurnSpeed, rightTurnSpeed, False)
            else:
                return False
        elif turnAngle < 0:#If we are turning left, the right wheels have to travel further
            leftTurnDistance = (overallCircumference - wheelDistanceFromCenter) / circlePercentage
            rightTurnDistance = (overallCircumference + wheelDistanceFromCenter) / circlePercentage
            rightSpeed = turnSpeed
            turnTime = (rightTurnDistance / robotSpeedInchesPerSecond)
            leftSpeed = (leftTurnDistance / turnTime)
            leftSpeedPercentage = (leftSpeed / rightSpeed)
            rightTurnSpeed = rightSpeed
            leftTurnSpeed = leftSpeedPercentage
            if turnAngle < self.getGyroAngle():
                self.drive.tankDrive(leftTurnSpeed, rightTurnSpeed, False)
            else:
                return False


    def autonPivot(self, turnAngle, turnSpeed):
        slowDownSpeed = .14
        correctionDeadzone = 5
        if self.firstRun:
            self.oldGyro = self.gyro.getAngle()
            self.firstRun = False
        turnSpeed -= (2*turnSpeed/(1+math.exp(0.049*(-1 if turnAngle>0 else 1)*(-turnAngle + self.getGyroAngle()))))
        #turnSpeed -= (2*turnSpeed/(1+math.exp(0.045*(-1 if turnAngle>0 else 1)*(-turnAngle + self.getGyroAngle()))))#Old turning formula, states
        turnSpeed = max(turnSpeed, slowDownSpeed)
        if turnAngle < 0:
            if abs(turnAngle - self.getGyroAngle()) > correctionDeadzone:
                if self.getGyroAngle() >= turnAngle:
                    self.drive.tankDrive(-(turnSpeed) * self.MOTOR_SPEED_CONTROL, (turnSpeed) * self.MOTOR_SPEED_CONTROL,False)
                    return True
                elif self.getGyroAngle() <= turnAngle:
                    self.drive.tankDrive(.2, -.2)
                    return True
                else:
                    pass
            else:
                self.drive.stopMotor()
                self.firstRun = True
                return False
        elif turnAngle > 0:
            if abs(turnAngle - self.getGyroAngle()) > correctionDeadzone:
                if self.getGyroAngle() <= turnAngle:
                    self.drive.tankDrive((turnSpeed) * self.MOTOR_SPEED_CONTROL, -(turnSpeed) * self.MOTOR_SPEED_CONTROL,False)
                    return True
                elif self.getGyroAngle() >= turnAngle:
                    self.drive.tankDrive(-.2, .2)
                    return True
                else:
                    pass
            else:
                self.drive.stopMotor()
                self.firstRun = True
                return False

    def autonDriveStraight(self, speed, distance):
        lSpeed = speed
        rSpeed = speed * self.RIGHT_MOTOR_BIAS
        encoderDistance = (distance / self.WHEEL_CIRCUMFERENCE) * self.ENCODER_CODES_PER_REV#Figueres out how far to spin the wheels in encoder codes, 265 is how many pins on current encoders
        if speed < .97:
            speedAdjustmentMultiplier = 4
        else:
            speedAdjustmentMultiplier = 2.5
        if self.firstTime:#Checks for first time through the function to only reset encoders on the first time
            self.oldGyro = self.gyro.getAngle()
            self.oldPositionLeft =  -(self.lbMotor.getQuadraturePosition())
            self.oldPositionRight =  self.rbMotor.getQuadraturePosition()
            self.autonCounter = 0
            self.firstTime = False

        self.lfEncoderPosition = abs(-(self.lbMotor.getQuadraturePosition()) - self.oldPositionLeft)
        self.rbEncoderPosition = abs(self.rbMotor.getQuadraturePosition() - self.oldPositionRight)
        averageEncoders = (self.lfEncoderPosition + self.rbEncoderPosition) / 2
        if averageEncoders < encoderDistance and self.autonCounter == 0:
            speedAdjustment = (.1 * speedAdjustmentMultiplier)
            slowDownSpeed = .25
            gyroAngle = self.getGyroAngle()
            speedAdjustment /= 1+math.exp(-gyroAngle)
            speedAdjustment -= (0.05 * speedAdjustmentMultiplier)
            rSpeed += speedAdjustment#Comment Line 248 and 249 out to remove the speed adjustment functions
            lSpeed -= speedAdjustment
            if averageEncoders > (encoderDistance - 500):
                lSpeed = slowDownSpeed
                rSpeed = slowDownSpeed
            self.drive.tankDrive(lSpeed * self.MOTOR_SPEED_CONTROL, rSpeed * self.MOTOR_SPEED_CONTROL,False)
            return True
        else:
            if self.autonCounter < 4:
                self.drive.tankDrive(-.15 * self.MOTOR_SPEED_CONTROL, -.15 * self.MOTOR_SPEED_CONTROL,False)
                self.autonCounter += 1
                return True
            else:
                self.firstTime = True
                self.drive.stopMotor()
                return False

    def autonMove(self, moveNumberPass, commandNumber, speed = 0, distance = 0, turnAngle = 0, turnSpeed = 0, setLiftPosition = 0, intakeMode = 0, radius = 0):
        if moveNumberPass == self.moveNumber:
            if commandNumber == 0:
                if self.autonDriveStraight(speed, distance):
                    if self.operate.autonRaiseLowerLift(setLiftPosition):
                        pass
                    if self.operate.autonIntakeControl(intakeMode):
                        pass
                else:
                    self.moveNumber += 1
            elif commandNumber == 1:
                if self.autonPivot(turnAngle, turnSpeed):
                    if self.operate.autonRaiseLowerLift(setLiftPosition):
                        pass
                    if self.operate.autonIntakeControl(intakeMode):
                        pass
                else:
                    self.moveNumber += 1
            elif commandNumber == 2:
                if self.operate.standaloneAutonRaiseLowerLift(setLiftPosition):
                    if self.operate.autonIntakeControl(intakeMode):
                        pass
                else:
                    self.moveNumber += 1
            elif commandNumber == 3:
                if self.operate.standaloneAutonIntakeControl(intakeMode):
                    if self.operate.autonRaiseLowerLift(setLiftPosition):
                        pass
                else:
                    self.moveNumber += 1
            elif commandNumber == 4:
                self.operate.liftMotorControlGroup.set(0)
                self.operae.rightManipulatorMotor.set(1)
                self.operate.leftManipulatorMotor.set(1)
                self.drive.tankDrive.stop()
            elif commandNumber == 5:
                if self.autonAngledTurn(radius, turnAngle, turnSpeed):
                    if self.operate.autonRaiseLowerLift(setLiftPosition):
                        pass
                    if self.operate.autonIntakeControl(intakeMode):
                        pass
        else:
            pass

    def resetMoveNumber(self):
        self.moveNumber = 1

    def samsStupidExperimentalDrive(self, aButton, bButton, xButton, yButton, rBumper, rTrigger, lBumper, lTrigger, dpad):
        leftPower = 0
        leftBackwards = False
        rightPower = 0
        rightBackwards = False
        if lBumper:
            leftPower = 1
        if lTrigger:
            leftBackwards = True
        if dpad == 90:
            leftPower *= .9
        if dpad == 180:
            leftPower *= .75
        if dpad == 270:
            leftPower *= .6
        if dpad == 0:
            leftPower *= .5
        if leftBackwards:
            leftPower *= -1
        if rBumper:
            rightPower = 1
        if rTrigger:
            rightBackwards = True
        if xButton:
            rightPower *= .9
        if aButton:
            rightPower *= .75
        if bButton:
            rightPower *= .6
        if yButton:
            rightPower *= .5
        if rightBackwards:
            rightPower *= -1
        self.tankDrive(leftPower, rightPower * -1)
