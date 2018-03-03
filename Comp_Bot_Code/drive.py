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
    MOTOR_SPEED_CONTROL = .82
    ENCODER_CODES_PER_REV = 5887

    def __init__(self, robot):
        self.operate = operatorFunctions(drive = self, robot = robot)
        self.gyro = AHRS.create_spi()
        #self.gyro = wpilib.interfaces.Gyro()
        """Sets drive motors to a cantalon or victor"""
        #self.instantiateMotors()
        #self.encoderReset()
        #self.driveBase = arcadeDrive()

        self.shifter = wpilib.DoubleSolenoid(20, 0, 1)#Initilizes the shifter's solenoid and sets it to read fron digital output 0
        #Motor Ids for comp. base lf = 4, lb = 2, rf = 5, rb = 2
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
        self.firstAngleTurn = True#Check for autonAngledTurn

        self.setWheelCircumference()

        self.oldGyro = 0

        self.moveNumber = 1
        self.shiftCounter = 0
        self.instantiateEncoders()

    def setWheelCircumference(self):
        #$ inch wheels circ = 12.5663706144, 6 inch wheels circ = 18.849
        self.wheelCircumference = 18.849

    def instantiateEncoders(self):
        self.lbMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.rbMotor.configSelectedFeedbackSensor(0, 0, 0)

        self.lbMotor.setSensorPhase(True)

    def drivePass(self, leftY, rightX, leftBumper, rightBumper, aButton):
        self.arcadeDrive(leftY, rightX)
        self.shift(leftBumper, rightBumper)
        self.manualEncoderReset(aButton)
        pass

    def scaleInputs(self, leftY, rightX):
        if abs(leftY) < .05:
            return .75 * rightX
        rightX = (-(math.log10((2*(abs(leftY)))+1)-1)*rightX)
        return rightX

    def printer(self):
        print('Why does Hescott look so much like shrek?')

    def arcadeDrive(self, leftY, rightX):
        #self.drive.arcadeDrive(leftY * -self.MOTOR_SPEED_CONTROL, self.scaleInputs(leftY, rightX) * self.MOTOR_SPEED_CONTROL)
        #print((-1 * self.scaleInputs(leftY, rightX)))
        #self.drive.arcadeDrive((-1 * self.scaleInputs(leftY, rightX)), (rightX/2))
        self.drive.arcadeDrive(leftY * -self.MOTOR_SPEED_CONTROL, rightX * self.MOTOR_SPEED_CONTROL)

    def shift(self, leftBumper, rightBumper):
        #print(self.shifter.get())
        if leftBumper:#When left bumper is pressed we shift gears
            if self.shifter.get() == 1:#Checks to see what gear we are in and shifts accordingly
                self.shifter.set(2)
                #print("shifting left")
        if rightBumper:
            if self.shifter.get() == 2 or self.shifter.get() == 0:
                self.shifter.set(1)
                #print("shifting right")

    def getGyroAngle(self):
    	return (self.gyro.getAngle()-self.oldGyro)

    def zeroGyro(self):
        self.gyro.reset()
        while(abs(self.getGyroAngle()) > 340):
            self.gyro.reset()

    def encoderReset(self):
        self.lbMotor.setQuadraturePosition(0, 0)
        self.rbMotor.setQuadraturePosition(0, 0)
        #print("Encoders Reset")

    def printEncoderPosition(self):
        lbEncoder = (self.lbMotor.getQuadraturePosition())
        rbEncoder = -(self.rbMotor.getQuadraturePosition())
        distanceDrivenInches = (lbEncoder / self.ENCODER_CODES_PER_REV) * self.wheelCircumference
        #averageEncoders = (lbEncoder + rbEncoder) / 2
        #print(averageEncoders)
        print('Right encoder   ' + str(rbEncoder))
        print('Left Encoder   ' + str(lbEncoder))
        #print(distanceDrivenInches)
        #print(self.getGyroAngle())

    def manualEncoderReset(self, aButton):
        if aButton:
            self.lbMotor.setQuadraturePosition(0, 0)
            self.rbMotor.setQuadraturePosition(0, 0)
        else:
            pass

    def autonShift(self, gear):
        if gear == 'high':
            if self.shifter.get() == 1 or self.shifter.get() == 0:
                self.shifter.set(2)
                #print('Shift to low')
                #return False
        elif gear == 'low':
            if self.shifter.get() == 2 or self.shifter.get() == 0:
                self.shifter.set(1)
                #print('Shift to high')
                #return False
        else:
            pass

    def autonPivot(self, turnAngle, turnSpeed):
        slowDownSpeed = .12
        correctionDeadzone = 1
        turnSpeed -= (2*turnSpeed/(1+math.exp(0.045*(-1 if turnAngle>0 else 1)*(-turnAngle + self.getGyroAngle()))))
        turnSpeed = max(turnSpeed, slowDownSpeed)
        if turnAngle < 0:
            if abs(turnAngle - self.getGyroAngle()) > correctionDeadzone:
                if self.getGyroAngle() >= turnAngle:
                    self.drive.tankDrive(-(turnSpeed) * self.MOTOR_SPEED_CONTROL, (turnSpeed) * self.MOTOR_SPEED_CONTROL, False)
                    #print('Turning Left')
                    return True
                elif self.getGyroAngle() <= turnAngle:
                    self.drive.tankDrive(.2, -.2)
                    return True
                else:
                    pass
            else:
                #print("Done Turning Left")
                print(self.getGyroAngle())
                self.drive.stopMotor()
                self.firstRun = True
                return False
        elif turnAngle > 0:
            if abs(turnAngle - self.getGyroAngle()) > correctionDeadzone:
                if self.getGyroAngle() <= turnAngle:
                    self.drive.tankDrive((turnSpeed) * self.MOTOR_SPEED_CONTROL, -(turnSpeed) * self.MOTOR_SPEED_CONTROL, False)
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
        #print('entered auton straight')
        lSpeed = speed
        rSpeed = speed
        encoderDistance = (distance / self.wheelCircumference) * self.ENCODER_CODES_PER_REV#Figueres out how far to spin the wheels in encoder codes, 265 is how many pins on current encoders
        #print('Encoder Distance' + str(encoderDistance))

        if self.firstTime:#Checks for first time through the function to only reset encoders on the first time
            #print('passed first check')#Debugging
            #self.encoderReset()#Resets encoders
            self.oldGyro = self.gyro.getAngle()
            self.oldPositionLeft =  (self.lbMotor.getQuadraturePosition())
            self.oldPositionRight =  -(self.rbMotor.getQuadraturePosition())
            self.autonCounter = 0
            self.firstTime = False

        self.lfEncoderPosition = (self.lbMotor.getQuadraturePosition()) - self.oldPositionLeft
        self.rbEncoderPosition = -(self.rbMotor.getQuadraturePosition()) - self.oldPositionRight
        if speed < 0:#If speed is negetive, this lets us drive backward
            self.lfEncoderPosition *= -1
            self.rbEncoderPosition *= -1
        #print(self.lfEncoderPosition)
        #print(self.rbEncoderPosition)
        averageEncoders = (self.lfEncoderPosition + self.rbEncoderPosition) / 2
        #print('Average Encodes' + str(averageEncoders))
        if averageEncoders < encoderDistance and self.autonCounter == 0:
            speedAdjustment = .1
            slowDownSpeed = .25
            gyroAngle = self.getGyroAngle()
            speedAdjustment /= 1+math.exp(-gyroAngle)
            speedAdjustment -= 0.05
            print(speedAdjustment)
            rSpeed += speedAdjustment
            lSpeed -= speedAdjustment
            if averageEncoders > encoderDistance - 500:
                lSpeed = slowDownSpeed
                rSpeed = slowDownSpeed
                #print('Slowing Down')
            self.drive.tankDrive(lSpeed * self.MOTOR_SPEED_CONTROL, rSpeed * self.MOTOR_SPEED_CONTROL,False)
            return True
        else:
            if self.autonCounter < 4:
                #print('Active Breaking')
                self.drive.tankDrive(-.15 * self.MOTOR_SPEED_CONTROL, -.15 * self.MOTOR_SPEED_CONTROL,False)
                self.autonCounter = self.autonCounter + 1
                return True
            else:
                #print('EndLoop')
                self.firstTime = True
                self.drive.stopMotor()
                #print(self.lfEncoderPosition)
                print(self.rbEncoderPosition)
                return False

    def autonAngledTurn(self, radius, turnangle, speed):
        if self.firstAngleTurn:#Checks for first time through the function to only reset encoders on the first time
            #print('passed first check')#Debugging
            #self.encoderReset()#Resets encoders
            self.oldGyro = self.gyro.getAngle()
            self.oldPositionLeft =  (self.lbMotor.getQuadraturePosition())
            self.oldPositionRight =  -(self.rbMotor.getQuadraturePosition())
            self.autonCounter = 0
            self.firstAngleTurn = False
        robotSpeed = 8
        robotSpeedInchesPerSecond = robotSpeed * 12
        wheelWidth = 24.3
        wheelDistanceFromCenter = wheelWidth / 2
        overallCircumference = 2 * (3.14159265 * radius)
        cirlcePercentage = 360 / turnAngle
        if turnAngle > 0:#IF we are turning right, the left wheels have to travel further
            leftTurnDistance = (overallCircumference + wheelDistanceFromCenter) / circlePercentage
            rightTurnDistance = (overallCircumference - wheelDistanceFromCenter) / circlePercentage
            leftSpeed = speed
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
            rightSpeed = speed
            turnTime = (rightTurnDistance / robotSpeedInchesPerSecond)
            leftSpeed = (leftTurnDistance / turnTime)
            leftSpeedPercentage = (leftSpeed / rightSpeed)
            rightTurnSpeed = rightSpeed
            leftTurnSpeed = leftSpeedPercentage
            if turnAngle < self.getGyroAngle():
                self.drive.tankDrive(leftTurnSpeed, rightTurnSpeed, False)
            else:
                return False

    def autonMove(self, moveNumberPass, commandNumber, speed, distance, turnAngle, turnSpeed, setLiftPosition, intakeMode):
        if moveNumberPass == self.moveNumber:
            print(self.moveNumber)
            if commandNumber == 0:
                if self.autonDriveStraight(speed, distance):
                    if self.operate.autonRaiseLowerLift(setLiftPosition):
                        pass
                    if self.operate.autonIntakeControl(intakeMode):
                        pass
                else:
                    print(self.getGyroAngle())
                    print('Move ' + str(moveNumberPass) + ' Complete')
                    self.moveNumber += 1
            elif commandNumber == 1:
                if self.autonPivot(turnAngle, turnSpeed):
                    if self.operate.autonRaiseLowerLift(setLiftPosition):
                        pass
                    if self.operate.autonIntakeControl(intakeMode):
                        pass
                else:
                    print(self.getGyroAngle())
                    print('Move ' + str(moveNumberPass) + ' Complete')
                    self.moveNumber += 1
            elif commandNumber == 2:
                if self.operate.standaloneAutonRaiseLowerLift(setLiftPosition):
                    pass
                else:
                    self.moveNumber += 1
            elif commandNumber == 3:
                if self.operate.standaloneAutonIntakeControl(intakeMode):
                    pass
                else:
                    self.moveNumber += 1
            else:
                pass
        else:
            pass

    def resetMoveNumber(self):
        self.moveNumber = 1
