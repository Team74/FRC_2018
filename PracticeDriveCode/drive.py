"""
File Author: Jacob Harrelson
File Creation Date: 1/10/2018
File Purpose: To create and run our drive functions
"""

import wpilib
from wpilib.drive import DifferentialDrive
from wpilib import Encoder

class driveTrain():

    def __init__(self, robot):
        self.lfMotor = wpilib.ctre.cantalon.CANTalon(0)
        self.lbMotor = wpilib.ctre.cantalon.CANTalon(1)
        self.rfMotor = wpilib.ctre.cantalon.CANTalon(2)
        self.rbMotor = wpilib.ctre.cantalon.CANTalon(3)


        self.lfMotor.setFeedbackDevice(ctre.cantalon.CANTalon.FeedbackDevice.CtreMagEncoder_Relative)
        self.lbMotor.setFeedbackDevice(ctre.cantalon.CANTalon.FeedbackDevice.CtreMagEncoder_Relative)
        self.rfMotor.setFeedbackDevice(ctre.cantalon.CANTalon.FeedbackDevice.CtreMagEncoder_Relative)
        self.rbMotor.setFeedbackDevice(ctre.cantalon.CANTalon.FeedbackDevice.CtreMagEncoder_Relative)

        self.lfMotor.configEncoderCodesPerRev(4096)
        self.lbMotor.configEncoderCodesPerRev(4096)
        self.rfMotor.configEncoderCodesPerRev(4096)
        self.rbMotor.configEncoderCodesPerRev(4096)

        self.lfMotor.setPosition(0)
        self.lbMotor.setPosition(0)
        self.rfMotor.setPosition(0)
        self.rbMotor.setPosition(0)

        self.left = wpilib.SpeedControllerGroup(self.lfMotor, self.lbMotor)
        self.right = wpilib.SpeedControllerGroup(self.rfMotor, self.rbMotor)

        self.robotDrive = DifferentialDrive(self.left, self.right)

    def autoDrive(self, leftSpeed, rightSpeed):
        self.lfmotor.set(leftSpeed)
        self.lbmotor.set(leftSpeed)
        self.rfmotor.set(rightSpeed)
        self.rbmotor.set(rightSpeed)

    def drive(self, leftY, rightY):
        self.robotDrive.tankDrive(leftY, rightY)
