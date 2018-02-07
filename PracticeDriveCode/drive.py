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
import ctre
import math

class driveTrain():

    def __init__(self, robot):
        self.gyro = AHRS.create_spi()
        #self.gyro = wpilib.interfaces.Gyro()
        """Sets drive motors to a cantalon or victor"""
        self.instantiateMotors()
        self.instantiateEncoders()
        #self.encoderReset()
        #self.driveBase = arcadeDrive()

        self.shifter = wpilib.DoubleSolenoid(51, 0, 1)#Initilizes the shifter's solenoid and sets it to read fron digital output 0

        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.lbMotor = ctre.wpi_victorspx.WPI_VictorSPX(11)
        self.rfMotor = ctre.wpi_victorspx.WPI_VictorSPX(9)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)
        '''
        self.left=wpilib.SpeedControllerGroup(self.lfMotor, self.lbMotor)
        self.right=wpilib.SpeedControllerGroup(self.rfMotor, self.rbMotor)
        self.drive = DifferentialDrive(self.left, self.right)
        '''
        self.drive = RobotDrive

        self.lfMotor.setNeutralMode(2)
        self.lbMotor.setNeutralMode(2)
        self.rfMotor.setNeutralMode(2)
        self.rbMotor.setNeutralMode(2)

        self.firstTime = True#Check for autonDriveStraight
        self.firstRun = True#Check for autonPivot
        self.resetFinish = False#Check for encoder reset

        self.setWheelCircumference()

        self.moveNumber = 1
        self.shiftCounter = 0

    def setWheelCircumference(self):
        self.wheelCircumference = 18.84954

    def instantiateEncoders(self):
        self.lfMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.rbMotor.configSelectedFeedbackSensor(0, 0, 0)

        self.lfMotor.setSensorPhase(True)

    def instantiateMotors(self):
        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.lbMotor = ctre.wpi_victorspx.WPI_VictorSPX(11)
        self.rfMotor = ctre.wpi_victorspx.WPI_VictorSPX(9)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)

        self.lfMotor.setNeutralMode(2)
        self.lbMotor.setNeutralMode(2)
        self.rfMotor.setNeutralMode(2)
        self.rbMotor.setNeutralMode(2)

    def drivePass(self, leftY, rightX, leftBumper, rightBumper, aButton):
        self.arcadeDrive(leftY, rightX)
        self.shift(leftBumper, rightBumper)
        self.manualEncoderReset(aButton)
        pass

    def scaleInputs(self, leftY, rightX):

        if leftY < .05:
            return .75 * rightX
        rightX = (-(math.log10((2*(abs(leftY)))+1)-1)*rightX)
        return rightX
        '''
        if abs(rightX) < .05:
            return leftY
        leftY = (-(math.log10((3*(abs(rightX)))+1.5))*leftY)
        return leftY
        '''
    def tankDrive(self, leftY, rightY):
        leftY = leftY*-1
        self.lbMotor.set(leftY * .82)
        self.lfMotor.set(leftY * .82)
        self.rfMotor.set(rightY * .82)
        self.rbMotor.set(rightY * .82)

    def arcadeDrive(self, leftY, rightX):
        self.drive.arcadeDrive(leftY * -.82, self.scaleInputs(leftY, rightX) * .82)
        #print((-1 * self.scaleInputs(leftY, rightX)))
        #self.drive.arcadeDrive((-1 * self.scaleInputs(leftY, rightX)), (rightX/2))
        #self.drive.arcadeDrive(leftY, rightX)

    def shift(self, leftBumper, rightBumper):
        if leftBumper:#When left bumper is pressed we shift gears
            if self.shifter.get() == 1:#Checks to see what gear we are in and shifts accordingly
                self.shifter.set(2)
        if rightBumper:
            if self.shifter.get() == 2 or self.shifter.get() == 0:
                self.shifter.set(1)

    def getGyroAngle(self):
    	return self.gyro.getAngle()

    def zeroGyro(self):
        self.gyro.reset()

    def encoderReset(self):
        self.lfMotor.setQuadraturePosition(0, 0)
        self.rbMotor.setQuadraturePosition(0, 0)
        print("Encoders Reset")

    def printEncoderPosition(self):
        lfEncoder = -(self.lfMotor.getQuadraturePosition())
        rbEncoder = self.rbMotor.getQuadraturePosition()
        averageEncoders = (lfEncoder + rbEncoder) / 2
        print(averageEncoders)
        #print(rbEncoder)

    def manualEncoderReset(self, aButton):
        if aButton:
            self.lfMotor.setQuadraturePosition(0, 0)
            self.rbMotor.setQuadraturePosition(0, 0)
        else:
            pass

    def autonShift(self, gear):
        if gear == 'low':
            if self.shifter.get() == 1 or self.shifter.get() == 0:
                self.shifter.set(2)
                print('Shift to low')
                #return False
        elif gear == 'high':
            if self.shifter.get() == 2 or self.shifter.get() == 0:
                self.shifter.set(1)
                print('Shift to high')
                #return False
        else:
            pass

    def autonPivot(self, turnAngle, turnSpeed):
        slowDownSpeed = .08
        if self.firstRun:
            self.zeroGyro()
            self.firstRun = False
        if abs(turnAngle - self.getGyroAngle()) < 20:
            turnSpeed = slowDownSpeed
        if turnAngle < 0:
            if self.getGyroAngle() > turnAngle:
                self.tankDrive((turnSpeed), -(turnSpeed))
                return True
            else:
                self.tankDrive(0,0)
                self.firstRun = True
                self.zeroGyro()
                return False
        elif turnAngle > 0:
            if self.getGyroAngle() < turnAngle:
                self.tankDrive(-(turnSpeed), (turnSpeed))
                return True
            else:
                self.tankDrive(0, 0)
                self.zeroGyro()
                self.firstRun = True
                return False

    def autonDriveStraight(self, speed, distance):
        #print('entered auton straight')
        lSpeed = speed
        rSpeed = speed
        encoderDistance = (distance / self.wheelCircumference) * 5887#Figueres out how far to spin the wheels in encoder codes, 265 is how many pins on current encoders
        print('Encoder Distance' + str(encoderDistance))

        if self.firstTime:#Checks for first time through the function to only reset encoders on the first time
            print('passed first check')#Debugging
            #self.encoderReset()#Resets encoders
            self.oldPositionLeft =  -(self.lfMotor.getQuadraturePosition())
            self.oldPositionRight =  self.rbMotor.getQuadraturePosition()
            self.autonCounter = 0
            self.firstTime = False

        self.lfEncoderPosition = -(self.lfMotor.getQuadraturePosition()) - self.oldPositionLeft
        self.rbEncoderPosition = self.rbMotor.getQuadraturePosition() - self.oldPositionRight
        #print(self.lfEncoderPosition)
        #print(self.rbEncoderPosition)
        averageEncoders = (self.lfEncoderPosition + self.rbEncoderPosition) / 2
        #print('Average Encodes' + str(averageEncoders))
        '''
        if averageEncoders > 250 and not self.resetFinish:
            #self.encoderReset()
            self.printEncoderPosition()
            return True
        else:
            if not self.resetFinish:
                print(self.lfEncoderPosition)
                print(self.rbEncoderPosition)
            #print('Encoder Reset Finished')
            self.resetFinish = True
        '''
        if averageEncoders < encoderDistance and self.autonCounter == 0:
            speedAdjustment = .05
            slowDownSpeed = .25
            if self.getGyroAngle() < -1:
                rSpeed = rSpeed - speedAdjustment
            elif self.getGyroAngle() > 1:
                lSpeed = lSpeed - speedAdjustment
            if averageEncoders > encoderDistance - 500:
                lSpeed = slowDownSpeed
                rSpeed = slowDownSpeed
                #print('Slowing Down')
            self.tankDrive(-(lSpeed), -(rSpeed))
            return True
        else:
            if self.autonCounter < 4:
                #print('Active Breaking')
                self.tankDrive(.15, .15)
                self.autonCounter = self.autonCounter + 1
                return True
            else:
                #print('EndLoop')
                self.zeroGyro()
                self.resetFinish = False
                self.firstTime = True
                self.tankDrive(0, 0)
                print(self.lfEncoderPosition)
                print(self.rbEncoderPosition)
                return False

    '''
    def autonAngledTurn(self, turnAngle):#Angle is in degrees
        ROBOT_WIDTH = 24.3

    def getSpeeds(self, angle, radius, speed=1):
        return [speed, speed*(lambda x: x[1]/x[0])(getDistances(angle, radius))]

    def getDistances(self, angle, radius):
           return [(radius + ROBOT_WIDTH/2)*math.radians(angle), (radius - ROBOT_WIDTH/2)*math.radians(angle) ]
    '''
    def autonMove(self, moveNumberPass, commandNumber, speed, distance, turnAngle, turnSpeed):
        if moveNumberPass == self.moveNumber:
            #print(self.moveNumber)
            if commandNumber == 0:
                if self.autonDriveStraight(speed, distance):
                    pass
                else:
                    #print(self.getGyroAngle())
                    print('Move ' + str(moveNumberPass) + ' Complete')
                    self.moveNumber = moveNumberPass + 1
            elif commandNumber == 1:
                if self.autonPivot(turnAngle, turnSpeed):
                    pass
                else:
                    #print(self.getGyroAngle())
                    print('Move ' + str(moveNumberPass) + ' Complete')
                    self.moveNumber = moveNumberPass + 1
            elif commandNumber == 2:
                pass
                """
                if self.encoderReset():
                    #print(' 1st pass')
                    pass
                else:
                    print('Move ' + str(moveNumberPass) + ' Complete')
                    self.moveNumber = moveNumberPass + 1
                """
            '''
            elif commandNumber == 3:
                if self.autonShifter():
                    pass
                else:
                    print('Move ' + str(moveNumberPass) + ' Complete')
                    self.moveNumber = moveNumberPass + 1            else:
                #print('2nd pass')
                pass
            '''
        else:
            #print('3rd pass')
            pass

    def resetMoveNumber(self):
        self.moveNumber = 1
