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


        self.lfMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.lbMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.rfMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.rbMotor.configSelectedFeedbackSensor(0, 0, 0)

        self.lfMotor.setSensorPhase(True)
        self.lbMotor.setSensorPhase(True)
        self.rfMotor.setSensorPhase(False)
        self.rbMotor.setSensorPhase(False)

        self.lfMotor.setSelectedSensorPosition(0, 0, 0)
        self.lbMotor.setSelectedSensorPosition(0, 0, 0)
        self.rfMotor.setSelectedSensorPosition(0, 0, 0)
        self.rbMotor.setSelectedSensorPosition(0, 0, 0)

    def printEncoders(self):
        print(self.lfMotor.getSelectedSensorPosition(0))
        print(self.lbMotor.getSelectedSensorPosition(0))
        print(self.rfMotor.getSelectedSensorPosition(0))
        print(self.rbMotor.getSelectedSensorPosition(0))

    def drivePass(self, leftY, rightY, leftX, leftBumper):
        self.drive(leftY, rightY)
        self.shift(leftBumper)

    def drive(self, leftY, rightY):
        leftY = leftY*-1
        self.left.set(leftY)
        self.right.set(rightY)
        self.printEncoders()

    def autonDrive(self, leftSpeed, rightSpeed, leftDistance, rightDistance):
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

    def autonDrive(self, leftSpeed, rightSpeed):
        self.left.set(leftSpeed)
        self.right.set(rightSpeed)
"""
    def autonTurn(self, turnAngle):#Angle is in degrees
        ROBOT_WIDTH = 24.3

        def getSpeeds(angle, radius, speed=1):
	        return [speed, speed*(lambda x: x[1]/x[0])(getDistances(angle, radius))

        def getDistances(angle, radius):
	        return [(radius + ROBOT_WIDTH/2)*math.radians(angle), (radius - ROBOT_WIDTH/2)*math.radians(angle) ]
"""
