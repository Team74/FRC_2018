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

class driveTrain():

    def __init__(self, robot):
        self.gyro = AHRS.create_spi()
        #self.gyro = wpilib.interfaces.Gyro()
        """Sets drive motors to a cantalon or victor"""
        self.instantiateMotors()
        self.instantiateEncoders()
        self.driveBase = arcadeDrive()

        self.shifter = wpilib.Solenoid(0)#Initilizes the shifter's solenoid and sets it to read fron digital output 0
        self.shifterPosition = self.shifter.get()

        self.firstTime = True#Check for autonDriveStraight
        self.firstRun = True#Check for autonPivot
        self.resetFinish = False#Check for encoder reset

        self.setWheelCircumference()

        self.moveNumber = 1

    def setWheelCircumference(self):
        self.wheelCircumference = 18.84954

    def instantiateEncoders(self):
        self.lfMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.rbMotor.configSelectedFeedbackSensor(0, 0, 0)

    def instantiateMotors(self):
        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.lbMotor = ctre.wpi_victorspx.WPI_VictorSPX(11)
        self.rfMotor = ctre.wpi_victorspx.WPI_VictorSPX(9)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)

        self.lfMotor.setNeutralMode(2)
        self.lbMotor.setNeutralMode(2)
        self.rfMotor.setNeutralMode(2)
        self.rbMotor.setNeutralMode(2)

    def drivePass(self, leftY, rightY, leftX, leftBumper, rightX, rightTrigger, leftTrigger):
        #self.drive(leftY, rightY, rightTrigger, leftTrigger)
        self.arcadeDrive(leftY, rightX)
        #self.shift(leftBumper)

    def drive(self, leftY, rightY, rightTrigger, leftTrigger):
        leftY = leftY*-1
        if rightTrigger:#straight
            self.lbMotor.set(leftY)
            self.lfMotor.set(leftY)
            self.rfMotor.set(leftY)
            self.rbMotor.set(leftY)
        elif leftTrigger:
            self.lbMotor.set(leftY/2)
            self.lfMotor.set(leftY/2)
            self.rfMotor.set(rightY/2)
            self.rbMotor.set(rightY/2)
        else:
            self.lbMotor.set(leftY)
            self.lfMotor.set(leftY)
            self.rfMotor.set(rightY)
            self.rbMotor.set(rightY)

    def arcadeDrive(self, leftY, rightX):
        self.driveBase.arcadeDrive(leftY, rightX)
        self.driveBase.drive(leftY, rightY)

    def arcadeDrive2(self):
        leftY=leftY*-1

    def shift(self, leftBumper):
        self.shifterPosition = self.shifter.get()
        if leftBumper:#When left bumper is pressed we shift gears
            if self.shifter.get():#Checks to see what gear we are in and shifts accordingly
                self.shifter.set(False)
            elif self.shifter.get() == False:
                self.shifter.set(True)
            else:
                pass

    def autonDriveStraight(self, speed, distance):
        #print('entered auton straight')
        lfSpeed = speed
        rbSpeed = speed
        encoderDistance = (distance / self.wheelCircumference * 4096)
        #print(encoderDistance)

        if self.firstTime:
            print('passed first check')
            self.encoderReset()

            self.lfEncoderPosition = self.lfMotor.getSelectedSensorPosition(0)

            print('Encoder Reset')
            self.firstTime = False

        self.lfEncoderPosition = self.lfMotor.getSelectedSensorPosition(0)
        self.rbEncoderPosition = self.rbMotor.getSelectedSensorPosition(0)
        print(self.lfEncoderPosition)
        if self.lfEncoderPosition > 250 and not self.resetFinish:
            print(self.lfEncoderPosition)
            return True
        else:
            #print('Encoder Reset Finished')
            self.resetFinish = True

        if self.lfEncoderPosition < encoderDistance:
            self.drive(-lfSpeed, -rbSpeed)
            return True
        else:
            print('EndLoop')
            self.zeroGyro()
            self.counterTime = 0
            self.resetFinish = False
            self.firstTime = True
            return False

    def getGyroAngle(self):
    	return self.gyro.getAngle()

    def setDistancePerPulse(self):
        #self.lfMotor.setDistancePerPulse(256)
        #self.rbMotor.setDistancePerPulse(256)
        pass
    def zeroGyro(self):
        self.gyro.reset()

    def encoderReset(self):
        self.lfMotor.reset()
        self.rbMotor.reset()

    def printEncoderPositition(self):
        lfEncoder = self.lfMotor.getQuadraturePosition()
        rbEncoder = self.rbMotor.getQuadraturePosition()
        print(lfEncoder)
        print(rbEncoder)

    def autonPivot(self, turnAngle, turnSpeed):
        if self.firstRun:
            self.zeroGyro()
            self.firstRun = False
        if turnAngle < 0:
            if self.getGyroAngle() > turnAngle:
                self.drive((turnSpeed), -(turnSpeed))
                return True
            else:
                self.drive(0,0)
                self.firstRun = True
                self.zeroGyro()
                return False
        elif turnAngle > 0:
            if self.getGyroAngle() < turnAngle:
                self.drive(-(turnSpeed), (turnSpeed))
                return True
            else:
                self.drive(0, 0)
                self.zeroGyro()
                self.firstRun = True
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
            if commandNumber == 0:
                if self.autonDriveStraight(speed, distance):
                    pass
                else:
                    print(self.getGyroAngle())
                    print('Move ' + str(moveNumberPass) + ' Complete')
                    self.moveNumber = moveNumberPass + 1
            elif commandNumber == 1:
                if self.autonPivot(turnAngle, turnSpeed):
                    pass
                else:
                    print(self.getGyroAngle())
                    print('Move ' + str(moveNumberPass) + ' Complete')
                    self.moveNumber = moveNumberPass + 1
            elif commandNumber == 2:
                if self.encoderReset():
                    pass
            else:
                pass
        else:
            pass
