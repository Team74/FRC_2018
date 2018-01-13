"""
File Author: Jacob Harrelson
File Name: drive.py
File Creation Date: 1/10/2018
File Purpose: To create and run our drive functions
"""

import wpilib
from wpilib.drive import DifferentialDrive
from wpilib import Encoder

class driveTrain():

    def __init__(self, robot):
        """Sets drive motors to a cantalon"""
        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)
        self.lbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.rfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(7)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(6)

        """Sets motors to an encoder"""
        self.lfMotor.setFeedbackDevice(ctre.wpi_talonsrx.WPI_TalonSRX.FeedbackDevice.CtreMagEncoder_Relative)
        self.lbMotor.setFeedbackDevice(ctre.wpi_talonsrx.WPI_TalonSRX.FeedbackDevice.CtreMagEncoder_Relative)
        self.rfMotor.setFeedbackDevice(ctre.wpi_talonsrx.WPI_TalonSRX.FeedbackDevice.CtreMagEncoder_Relative)
        self.rbMotor.setFeedbackDevice(ctre.wpi_talonsrx.WPI_TalonSRX.FeedbackDevice.CtreMagEncoder_Relative)
        """Configures encoders"""
        self.lfMotor.configEncoderCodesPerRev(4096)
        self.lbMotor.configEncoderCodesPerRev(4096)
        self.rfMotor.configEncoderCodesPerRev(4096)
        self.rbMotor.configEncoderCodesPerRev(4096)
        """Sets position of encoders"""
        self.lfMotor.setPosition(0)
        self.lbMotor.setPosition(0)
        self.rfMotor.setPosition(0)
        self.rbMotor.setPosition(0)
        """Sets motors on the same side to a control group for easier control"""
        self.left = wpilib.SpeedControllerGroup(self.lfMotor, self.lbMotor)
        self.right = wpilib.SpeedControllerGroup(self.rfMotor, self.rbMotor)

        self.robotDrive = DifferentialDrive(self.left, self.right)

        self.shifter = wpilib.Solenoid(0)#Initilizes the shifter's solenoid and sets it to read fron digital output 0
        self.shifterPosition = self.shifter.get()

    def drive(self, leftY, rightY):
        leftY = leftY*-1
        self.left.set(leftY)
        self.right.set(rightY)

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

    def autonTurn(self, turnAngle):#Angle is in degrees
        ROBOT_WIDTH = 24.3

        def getSpeeds(angle, radius, speed=1):
	        return [speed, speed*(lambda x: x[1]/x[0])(getDistances(angle, radius))

        def getDistances(angle, radius):
	        return [(radius + ROBOT_WIDTH/2)*math.radians(angle), (radius - ROBOT_WIDTH/2)*math.radians(angle) ]
