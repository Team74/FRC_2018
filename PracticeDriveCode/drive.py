"""
File Author: Jacob Harrelson
File Name: drive.py
File Creation Date: 1/10/2018
File Purpose: To create and run our drive functions
"""

import wpilib
from wpilib.drive import DifferentialDrive
from wpilib import Encoder
import ctre

class driveTrain():

    def __init__(self, robot):
        self.gyro = AHRS.create_spi()
        #self.gyro = wpilib.interfaces.Gyro()
        """Sets drive motors to a cantalon"""
        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(7)
        self.lbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(6)
        self.rfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)

        self.left = wpilib.SpeedControllerGroup(self.lfMotor, self.lbMotor)
        self.right = wpilib.SpeedControllerGroup(self.rfMotor, self.rbMotor)

        self.robotDrive = DifferentialDrive(self.left, self.right)

        self.shifter = wpilib.Solenoid(0)#Initilizes the shifter's solenoid and sets it to read fron digital output 0
        self.shifterPosition = self.shifter.get()

        self.firstTime = True
        self.resetFinish = False
        self.counterTime = 0

        self.wheelCircumference = 12.5663706144

    def printEncoders(self):
        print(self.lfMotor.getSelectedSensorPosition(0))
        #print(self.lbMotor.getSelectedSensorPosition(0))
        #print(self.rfMotor.getSelectedSensorPosition(0))
        #print(self.rbMotor.getSelectedSensorPosition(0))

    def drivePass(self, leftY, rightY, leftX, leftBumper):
        self.drive(leftY, rightY)
        self.shift(leftBumper)

    def drive(self, leftY, rightY):
        leftY = leftY*-1
        self.left.set(leftY)
        self.right.set(rightY)
        self.printEncoders()

    def turnAngle(self, degrees, speed):
        if(self.gyro.getAngle() > degrees+0.25):
            self.autonTankDrive(-1*speed, speed)
            print(self.gyro.getAngle())
        elif(self.gyro.getAngle() < degrees-0.25):
            self.autonTankDrive(speed, -1*speed)
            print(self.gyro.getAngle())
        elif(self.gyro.getAngle() <= degrees-0.25):
            self.autonTankDrive(-1*speed, speed)
            print(self.gyro.getAngle())
        else:
            return True
        return False

    def autonDrawDrive(self, leftSpeed, rightSpeed, leftDistance, rightDistance):
        if ((self.lfmotor.getSelectedSensorPosition(0)+self.lbMotor.getSelectedSensorPosition(0))/2 != abs(leftDistance-1)):
            self.lfmotor.set(leftSpeed)
            self.lbmotor.set(leftSpeed)
        if((self.rfMotor.getSelectedSensorPosition(0)+self.rbMotor.getSelectedSensorPosition(0))/2 != abs(leftDistance-1)):
            self.rfmotor.set(rightSpeed)
            self.rbmotor.set(rightSpeed)

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
        ulfSpeed = speed
        ulbSpeed = speed
        urfSpeed = speed* -1
        urbSpeed = speed* -1
        encoderDistance = (distance / self.wheelCircumference) * 4096
        #print(encoderDistance)

        if self.firstTime:
                    print(self.lfMotor.setSelectedSensorPosition(1, 0, 10000))
                    print(self.lbMotor.setSelectedSensorPosition(1, 0, 10000))
                    print(self.rfMotor.setSelectedSensorPosition(1, 0, 10000))
                    print(self.rbMotor.setSelectedSensorPosition(1, 0, 10000))

                    self.lfEncoderPosition = self.lfMotor.getSelectedSensorPosition(0)

                    print('Encoder Reset')
                    print(self.lfEncoderPosition[1])
                    self.firstTime = False
        self.lfEncoderPosition = self.lfMotor.getSelectedSensorPosition(0)
        self.lbEncoderPosition = self.lbMotor.getSelectedSensorPosition(0)
        self.rfEncoderPosition = self.rfMotor.getSelectedSensorPosition(0)
        self.rbEncoderPosition = self.rbMotor.getSelectedSensorPosition(0)
        if self.lfEncoderPosition[1] > 100 and not self.resetFinish:
            return True
        else:
            self.resetFinish = True

        if self.lfEncoderPosition[1] < encoderDistance:
            if self.lbEncoderPosition[1] < self.rbEncoderPosition[1]:
                if ulbSpeed < 0:
                    ulbSpeed = ulbSpeed + .01
                elif ulbSpeed > 0:
                    ulbSpeed = ulbSpeed - .01
                else:
                    pass

            if self.rbEncoderPosition[1] < self.lbEncoderPosition[1]:
                if urbSpeed < 0:
                    urbSpeed = urbSpeed + .01
                elif urbSpeed > 0:
                    urbSpeed = urbSpeed - .01
                else:
                    pass

            if self.lfEncoderPosition[1] < self.rfEncoderPosition[1]:
                if ulfSpeed < 0:
                    ulfSpeed = ulfSpeed + .01
                elif ulfSpeed > 0:
                    ulfSpeed = ulfSpeed - .01
                else:
                    pass

            if self.rfEncoderPosition[1] < self.lfEncoderPosition[1]:
                if urfSpeed < 0:
                    urfSpeed = urfSpeed + .01
                elif urfSpeed > 0:
                    urfSpeed = urfSpeed - .01
                else:
                    pass

            self.lfMotor.set(ulfSpeed)
            self.lbMotor.set(ulbSpeed)
            self.rfMotor.set(urfSpeed)
            self.rbMotor.set(urbSpeed)
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

    def zeroGyro(self):
        self.gyro.reset()

    def autonPivot(self, turnAngle):
        turnSpeed = .3
        if turnAngle < 0:
            if self.getGyroAngle() > turnAngle:
                self.lfMotor.set(turnSpeed * -1)
                self.lbMotor.set(turnSpeed * -1)
                self.rfMotor.set(turnSpeed * -1)
                self.rfMotor.set(turnSpeed * -1)
                return True
            else:
                self.lfMotor.set(0)
                self.lbMotor.set(0)
                self.rfMotor.set(0)
                self.rbMotor.set(0)
                self.zeroGyro()
                return False
        elif turnAngle > 0:
            if self.getGyroAngle() < turnAngle:
                self.lfMotor.set(turnSpeed)
                self.lbMotor.set(turnSpeed)
                self.rfMotor.set(turnSpeed)
                self.rbMotor.set(turnSpeed)
                return True
            else:
                self.lfMotor.set(0)
                self.lbMotor.set(0)
                self.rfMotor.set(0)
                self.rbMotor.set(0)
                self.zeroGyro()
                return False

    def autonAngledTurn(self, turnAngle):#Angle is in degrees
        ROBOT_WIDTH = 24.3

    def getSpeeds(self, angle, radius, speed=1):
        return [speed, speed*(lambda x: x[1]/x[0])(getDistances(angle, radius))]

    def getDistances(self, angle, radius):
	    return [(radius + ROBOT_WIDTH/2)*math.radians(angle), (radius - ROBOT_WIDTH/2)*math.radians(angle) ]
