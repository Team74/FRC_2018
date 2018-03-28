"""
File Author: Jacob Harrelson
File Name: operator.py
File Creation Date: 1/11/2018
File Purpose: To create and run our operator functions
"""
import wpilib
from wpilib import Encoder, RobotDrive
from timeOut import *
import ctre
import math

class operatorFunctions():
    TIME_LEFT_UNTIL_ENDGAME = 105 * 50#105 is time in teleop before endgame, 50 is how many times our code loops per second
    TIME_TO_EJECT = 10#Value is in number of loops through the function and represents how long it takes to fully eject a cube with some to spare
    TIME_TO_SPIN = 6#Value is in number of loops to spin the cube when realigning during intake

    def __init__(self, robot, drive):
        self.time = timeOut()
        self.drive = drive
        self.firstUse = True
        #Set each motor to a talon, and or victor
        self.liftMotor = ctre.wpi_talonsrx.WPI_TalonSRX(3)
        self.liftMotor.configSelectedFeedbackSensor(0, 0, 0)
        self.liftMotor.setSelectedSensorPosition(0, 0, 0)
        self.liftMotor.setSensorPhase(True)
        self.liftMotorTwo = ctre.wpi_victorspx.WPI_VictorSPX(7)
        self.liftMotorTwo.set(5, 3)

        self.winchMotorOne = ctre.wpi_victorspx.WPI_VictorSPX(6)
        self.winchMotorTwo = ctre.wpi_victorspx.WPI_VictorSPX(10)

        self.leftManipulatorMotor = ctre.wpi_victorspx.WPI_VictorSPX(8)
        self.rightManipulatorMotor = ctre.wpi_victorspx.WPI_VictorSPX(9)

        self.leftManipulatorMotor.setNeutralMode(2)
        self.rightManipulatorMotor.setNeutralMode(2)

        self.tilter = wpilib.DoubleSolenoid(20, 2, 3)

        self.proximitySensor = wpilib.DigitalInput(0)#Initilizes a proximity sensor used to see if we have a cube secured in the manipulator, sets it to read from DIO 0
        self.isLiftDown = wpilib.DigitalInput(1)#Initilizes a limit switch to see if the lift is at it's minnimum height, sets it to read from DIO 1
        self.isLiftUp = wpilib.DigitalInput(2)#Initilizes a limit switch to see if the lift is at it's maximum height, sets it to read from DIO 2

        self.toggle = 0

        self.compressor = wpilib.Compressor()
        self.compressor.setClosedLoopControl(True)

        self.winchMotorControlGroup = wpilib.SpeedControllerGroup(self.winchMotorOne, self.winchMotorTwo, self.winchMotorThree)
        self.firstEject = True#Says if it is our first time through the ejecting a cube in auton
        self.firstUse = True
        self.liftAccel = 0
        self.firstSpin = True
    def operate(self, leftY, leftX, rightY, rightX, aButton, bButton, xButton, yButton, rightTrigger,rightBumper, leftTrigger, leftBumper, startButton, backButton):
        #Passes inputs from operator controller to the appropriate operator functions
        self.liftTilt(rightBumper, leftBumper)
        self.raiseLowerLift(leftY)
        #self.winchUpDown(rightY)
        self.manipulatorControl(aButton, bButton, xButton, yButton)
        self.manipulatorControlTwo(rightY)
        self.zeroLiftEncoder(startButton)

    def liftTest(self):
        print(self.liftMotor.getSelectedSensorPosition(0))

    def liftTilt(self, rightBumper, leftBumper):#Controls the tilt of the lift
        if leftBumper:
            print('Tipping Foward')
            #if self.tilter.get() == 1:#Checks to see what position the lift is in and tilts accordingly
            self.tilter.set(2)
        if rightBumper:
            print('Tiping Back')
            #if self.tilter.get() == 2 or self.tilter.get() == 0:
            self.tilter.set(1)

    def raiseLowerLift(self, leftY):
        accelerationDeadzone = .1
        output = leftY
        if abs(leftY) >= accelerationDeadzone:
            self.liftAccel += 1
        else:
            self.liftAccel = 0
        maxSpeedLimit = .045 * self.liftAccel + .04
        if self.liftAccel < 15:
            if leftY < 0:
                output = max(output, (-1 * maxSpeedLimit))
            else:
                output = min(output, maxSpeedLimit)
        if self.isLiftDown.get():
            self.liftMotor.setSelectedSensorPosition(0, 0, 0)
            output = min(0, output)
        if self.isLiftUp.get():
            self.liftMotor.setSelectedSensorPosition(35600, 0, 0)
            output = max(0, output)
        self.liftMotor.set(output)
    def printLiftEncoder(self):
        print(self.liftMotor.getSelectedSensorPosition(0))

    def zeroLiftEncoder(self, startButton):
        if startButton:
            self.liftMotor.setSelectedSensorPosition(0, 0, 0)

    def printLiftOutputCurrent(self):
        print(self.liftMotor.getOutputCurrent())
    '''
    def pidLift(self, setLiftPosition):
        liftPositionOne = 0#Lift position when lift is all the way down in encoder values
        liftPositionTwo = 500#Lift position for
        liftPositionThree = 12000#Lift position to place cubes on the switch in encoder values
        liftPositionFour = 1#Lift position to place cubes on the scale in encoder values
        #Reads the desiried lift position and sets how high we need to lift the lift
        if setLiftPosition == 0:
            liftHeight = liftPositionOne
        elif setLiftPosition == 1:
            liftHeight = liftPositionTwo
        elif setLiftPosition == 2:
            liftHeight = liftPositionThree
        elif setLiftPosition == 3:
            liftHeight = liftPositionFour
        if self.firstUse:
            self.firstUse = False
            self.liftLoopSource = wpilib.interfaces.PIDSource()
            self.liftLoopSource.setContinuous(True)
            def getFunction():
                return self.liftMotor.getSelectedSensorPosition(0, 0, 0)
            def sourceTypFunction():
                return 0
            self.liftLoopSource.pidGet = getFunction
            self.liftLoopSource.getPIDSourceType = sourceTypFunction
            self.liftLoopOut = wpilib.interfaces.PIDOutput()
            def setFunction(output):
                self.liftmotor.set(-output)#LiftMotor outputs reversed, positive is down, negetive is up, correcting for that here
            self.liftLoopOut = setFunction
            self.liftPID = wpilib.PIDController(p, i, d, f, source=self.liftLoopSource, output=self.liftLoopOut, period=0.02)#p =, i =, d =, f =
        else:
            self.liftLoopSource.setSetpoint(liftHeight)
    '''

    def autonRaiseLowerLift(self, setLiftPosition):#Note encoder values do not scale linearly with lift hieght
        speed = 0
        currentEncoderPosition = self.liftMotor.getSelectedSensorPosition(0)
        #Defines three set lift positions
        liftPositionOne = 0#Lift position when lift is all the way down in encoder values
        liftPositionTwo = 500#Lift position for
        liftPositionThree = 10000#Lift position to place cubes on the switch in encoder values
        liftPositionFour = 35000#Lift position to place cubes on the scale in encoder values
        #Reads the desiried lift position and sets how high we need to lift the lift
        if setLiftPosition == 0:
            liftHeight = liftPositionOne
        elif setLiftPosition == 1:
            liftHeight = liftPositionTwo
        elif setLiftPosition == 2:
            liftHeight = liftPositionThree
        elif setLiftPosition == 3:
            liftHeight = liftPositionFour
        print(currentEncoderPosition)
        if currentEncoderPosition <= (liftHeight + 250):
            speed = 1
            #print('Going up')
        elif currentEncoderPosition >= (liftHeight - 250):
            #speed = -.75
            #print('going down')
            speed = 0
        else:
            speed = 0
            #print('Holding')
        '''
        if self.isliftDown.get():
            speed = max(0, speed)
        '''
        if self.isLiftUp.get():
            speed = min(0, speed)

        self.liftMotor.set(-speed)
        return True

    def standaloneAutonRaiseLowerLift(self, setLiftPosition):
        speed = 0
        currentEncoderPosition = self.liftMotor.getSelectedSensorPosition(0)
        #Defines four set lift positions
        liftPositionOne = 0#Lift position when lift is all the way down in encoder values
        liftPositionTwo = 500#Lift position for
        liftPositionThree = 10000#Lift position to place cubes on the switch in encoder values
        liftPositionFour = 35000#Lift position to place cubes on the scale in encoder values
        #Reads the desiried lift position and sets how high we need to lift the lift
        if setLiftPosition == 0:
            liftHeight = liftPositionOne
        elif setLiftPosition == 1:
            liftHeight = liftPositionTwo
        elif setLiftPosition == 2:
            liftHeight = liftPositionThree
        elif setLiftPosition == 3:
            liftHeight = liftPositionFour
        if (currentEncoderPosition > (liftHeight - 125) and currentEncoderPosition <  (liftHeight + 125)) or (self.isLiftUp.get()):
            self.liftMotor.set(0)
            return False
        if currentEncoderPosition <= (liftHeight + 500):
            speed = 1
            '''
            if self.isLiftDown.get():
                self.liftMotor.setSelectedSensorPosition(0, 0, 0)
                speed = min(0, speed)
            elif self.isLiftUp.get():
                self.liftMotor.setSelectedSensorPosition(36000, 0, 0)
                speed = max(0, speed)
            '''
            self.liftMotor.set(-speed)
            return True
        elif currentEncoderPosition >= (liftHeight - 500):
            speed = -1
            '''
            if self.isLiftDown.get():
                self.liftMotor.setSelectedSensorPosition(0, 0, 0)
                speed = min(0, speed)
            elif self.isLiftUp.get():
                self.liftMotor.setSelectedSensorPosition(35600, 0, 0)
                speed = max(0, speed)
            '''
            self.liftMotor.set(-speed)
            return True
        else:
            self.liftMotor.set(0)
            return False
    def deployClimber(self, startButton, backButton):
            if (startButton or backButton) and (self.time.time >= self.TIME_LEFT_UNTIL_ENDGAME):#If start button or back button is pressed and we are in endgame, the climber will deploy
                pass
            else:
                pass

    def winchUpDown(self, rightY):#Operator can use right stick to raise the winch for climbing

        if self.time.time >= self.TIME_LEFT_UNTIL_ENDGAME:#Prevents climber from being deployed until the endgame starts
            #self.winchMotorControlGroup.set(rightY)
            pass
        else:
            self.winchMotorControlGroup.set((rightY * 1) * .5)#Testing only, remove when done

    def doWeHaveACube(self):
        cubeInManipulator = self.proximitySensor.get()#Gets input from proximity sensor and setes it to cubeInManinpulator
        return cubeInManipulator

    def manipulatorControl(self, aButton, bButton, xButton, yButton):
        if aButton:#Intake
            self.leftManipulatorMotor.set(-.75)
            self.rightManipulatorMotor.set(-.75)
        elif bButton:#Automated function to spin cubes in the gripper to proper alignment
            if self.firstSpin:
                spinCounter = 0
                self.firstSpin = False
            if spinCounter =< self.TIME_TO_SPIN:
                self.leftManipulatorMotor.set(-1)
                self.rightManipulatorMotor.set(1)
            else:
                self.leftManipulatorMotor.set(-.75)
                self.rightManipulatorMotor.set(-.75)
        elif not bButton:
            self.firstSpin = True
        elif xButton:#Eject 1/2
            self.leftManipulatorMotor.set(.5)
            self.rightManipulatorMotor.set(.5)
        elif yButton:#Eject Full
            self.leftManipulatorMotor.set(1)
            self.rightManipulatorMotor.set(1)

    def manipulatorControlTwo(self, rightY):
        if rightY >= .075:
            speed = -(rightY)
            self.leftManipulatorMotor.set(speed)
            self.rightManipulatorMotor.set(speed)
        else:
            pass


    def startRunTimeClock(self):
        self.runTime = 0

    def autonIntakeControl(self, intakeMode):
        if intakeMode == 1:#Intake mode
            if self.doWeHaveACube():
                intakeMode = 0
            if intakeMode == 1:
                print('Intaking')
                self.leftManipulatorMotor.set(-1)
                self.rightManipulatorMotor.set(-1)
                return True
            else:
                pass
        elif intakeMode == 2:#Eject Mode
            print('Ejecting Half Power')
            self.leftManipulatorMotor.set(.5)
            self.rightManipulatorMotor.set(.5)
            return True
        elif intakeMode == 3:#Full Power eject
            print('Ejecting Full Power')
            self.leftManipulatorMotor.set(1)
            self.rightManipulatorMotor.set(1)
            return True
        elif intakeMode == 0:#Neutral Mode
            self.leftManipulatorMotor.set(0)
            self.rightManipulatorMotor.set(0)
            return True

    def standaloneAutonIntakeControl(self, intakeMode):
        if intakeMode == 1:#Intake mode
            if self.doWeHaveACube():
                return False
            elif intakeMode == 1:
                self.leftManipulatorMotor.set(-1)
                self.rightManipulatorMotor.set(-1)
                return True
            else:
                pass
        elif intakeMode == 2:#Half eject
            if self.firstEject:
                self.ejectClock = 0
                self.firstEject = False
            if self.ejectClock <= self.TIME_TO_EJECT:
                self.leftManipulatorMotor.set(.5)
                self.rightManipulatorMotor.set(.5)
                self.ejectClock += 1
                return True
            else:
                self.firstEject = True
                return False
        elif intakeMode == 3:#Full eject
            if self.firstEject:
                self.ejectClock = 0
                self.firstEject = False
            if self.ejectClock <= self.TIME_TO_EJECT:
                self.leftManipulatorMotor.set(1)
                self.rightManipulatorMotor.set(1)
                self.ejectClock += 1
                return True
            else:
                self.firstEject = True
                return False
        return False#Must be mode 0
