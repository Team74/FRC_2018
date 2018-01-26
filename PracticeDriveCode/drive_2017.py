


import wpilib
import robotpy_ext
from robotpy_ext.common_drivers.navx.ahrs import AHRS
from wpilib.drive import DifferentialDrive
import ctre
from drive import driveTrain
class driveTrain2017(driveTrain):

    def instantiateMotors(self):
        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(6)
        self.lbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(7)
        self.rfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)

    def setWheelCircumference(self):
        self.wheelCircumference = 12.5663706144

    def drive(self, leftY, rightY):
        leftY = leftY*-1
        self.lbMotor.set(leftY)
        self.lfMotor.set(leftY)
        self.rfMotor.set(rightY)
        self.rbMotor.set(rightY)
