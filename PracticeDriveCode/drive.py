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
import ctre

class driveTrain():

    def __init__(self, robot):
        self.gyro = AHRS.create_spi()
        #self.gyro = wpilib.interfaces.Gyro()
        """Sets drive motors to a cantalon or victor"""
        self.instantiateMotors()


        self.lfMotor.setSelectedSensorPosition(1, 0, 10000)
        self.rbMotor.setSelectedSensorPosition(1, 0, 10000)


        self.lfMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.rbMotor.configSelectedFeedbackSensor(0, 0, 0)

        self.lfMotor.setSensorPhase(True)
        self.rbMotor.setSensorPhase(False)

        #self.left = wpilib.SpeedControllerGroup(self.lfMotor, self.lbMotor)
        #self.right = wpilib.SpeedControllerGroup(self.rfMotor, self.rbMotor)

        #self.robotDrive = DifferentialDrive(self.left, self.right)

        #self.shifter = wpilib.Solenoid(0)#Initilizes the shifter's solenoid and sets it to read fron digital output 0
        #self.shifterPosition = self.shifter.get()

        self.firstTime = True#Check for autonDriveStraight
        self.firstRun = True#Check for autonPivot
        self.resetFinish = False#Check for encoder reset

        #Circumference of our wheels in inches

        self.moveNumber = 1

    def instantiateMotors(self):
        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.lbMotor = ctre.victorspx.VictorSPX(11)
        self.rfMotor = ctre.victorspx.VictorSPX(9)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)

    def setWheelCircumference(self):
        self.wheelCircumference = 18.84954

    def drivePass(self, leftY, rightY, leftX, leftBumper):
        self.drive(leftY, rightY)
        #self.shift(leftBumper)

    def drive(self, leftY, rightY):
        leftY = leftY*-1
        self.lbMotor.set(0, leftY)
        self.lfMotor.set(leftY)
        self.rfMotor.set(0, rightY)
        self.rbMotor.set(rightY)
    '''

    def shift(self, leftBumper):
        self.shifterPosition = self.shifter.get()
        if leftBumper:#When left bumper is pressed we shift gears
            if self.shifter.get():#Checks to see what gear we are in and shifts accordingly
                self.shifter.set(False)
            elif self.shifter.get() == False:
                self.shifter.set(True)
            else:
                pass
    '''
    def autonDriveStraight(self, speed, distance):
        ulfSpeed = speed
        ulbSpeed = speed
        urfSpeed = speed* -1
        urbSpeed = speed* -1
        encoderDistance = (distance / self.wheelCircumference) * 4096
        #print(encoderDistance)

        if self.firstTime:
            '''
                    self.lfMotor.setSelectedSensorPosition(1, 0, 10000)
                    self.rbMotor.setSelectedSensorPosition(1, 0, 10000)

                    self.lfEncoderPosition = self.lfMotor.getSelectedSensorPosition(0)

                    print('Encoder Reset')
                    #print(self.lfEncoderPosition)
                    self.firstTime = False
        self.lfEncoderPosition = self.lfMotor.getSelectedSensorPosition(0)
        self.rbEncoderPosition = self.rbMotor.getSelectedSensorPosition(0)
        if self.lfEncoderPosition > 250 and not self.resetFinish:
            #print(self.lfEncoderPosition)
            return True
        else:
            #print('Encoder Reset Finished')
            self.resetFinish = True

        if self.lfEncoderPosition < encoderDistance:
            if self.lbEncoderPosition < self.rbEncoderPosition:
                if ulbSpeed < 0:
                    ulbSpeed = ulbSpeed + .01
                elif ulbSpeed > 0:
                    ulbSpeed = ulbSpeed - .01
                else:
                    pass

            if self.rbEncoderPosition < self.lbEncoderPosition:
                if urbSpeed < 0:
                    urbSpeed = urbSpeed + .01
                elif urbSpeed > 0:
                    urbSpeed = urbSpeed - .01
                else:
                    pass

            if self.lfEncoderPosition < self.rfEncoderPosition:
                if ulfSpeed < 0:
                    ulfSpeed = ulfSpeed + .01
                elif ulfSpeed > 0:
                    ulfSpeed = ulfSpeed - .01
                else:
                    pass

            if self.rfEncoderPosition < self.lfEncoderPosition:
                if urfSpeed < 0:
                    urfSpeed = urfSpeed + .01
                elif urfSpeed > 0:
                    urfSpeed = urfSpeed - .01
                else:
                    pass

            self.lfMotor.set(ulfSpeed)
            self.rbMotor.set(urbSpeed)
            return True
        else:
            print('EndLoop')
            self.zeroGyro()
            self.counterTime = 0
            self.resetFinish = False
            self.firstTime = True
            return False
    '''
    def getGyroAngle(self):
    	return self.gyro.getAngle()
    '''
    def zeroGyro(self):
        self.gyro.reset()

    def encoderReset(self):
        self.lfMotor.setSelectedSensorPosition(1, 0, 10000)
        self.rbMotor.setSelectedSensorPosition(1, 0, 10000)
        return False

    def autonPivot(self, turnAngle, turnSpeed):
        if self.firstRun:
            self.zeroGyro()
            self.firstRun = False
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
                self.firstRun = True
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
                self.firstRun = True
                return False

    def autonAngledTurn(self, turnAngle):#Angle is in degrees
        ROBOT_WIDTH = 24.3

        def getSpeeds(self, angle, radius, speed=1):
            return [speed, speed*(lambda x: x[1]/x[0])(getDistances(angle, radius))]

        def getDistances(self, angle, radius):
	           return [(radius + ROBOT_WIDTH/2)*math.radians(angle), (radius - ROBOT_WIDTH/2)*math.radians(angle) ]

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
                    print('In turn')
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

        '''
