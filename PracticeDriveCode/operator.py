"""
File Author: Jacob Harrelson
File Creation Date: 1/11/2018
File Purpose: To create and run our operator functions
"""
import wpilib
from wpilib import Encoder, RobotDrive

class operatorControl():

    def __init__(self, robot, drive):

        self.drive = drive

        self.liftMotorOne = ctre.cantalon.CANTalon(4)
        self.leftWinchMotorOne = ctre.cantalon.CANTalon(6)
        self.liftMotorTwo = ctre.cantalon.CANTalon(5)
        self.leftWinchMotorTwo = ctre.cantalon.CANTalon(7)
        self.rightWinchMotorOne = ctre.cantalon.CANTalon(8)
        self.rightWinchMotorTwo = ctre.cantalon.CANTalon(9)
        self.leftMinipulatorMotor = ctre.cantalon.CANTalon(10)
        self.rightMinipulatorMotor = ctre.cantalon.CANTalon(11)
        self.leftPlatformDeployMotor = ctre.cantalon.CANTalon(12)
        self.rightPlatformDeployMotor = ctre.cantalon.CANTalon(13)
        self.minipulatorFoldUpDownMotor = ctre.cantalon.CANTalon(14)
        self.minipulatorPowerCubeReleaseMotor = ctre.cantalon.CANTalon(15)

    def 
