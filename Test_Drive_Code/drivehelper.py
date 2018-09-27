import Math
class Drivehelper():

    def __init__():
        self.kThrottleDeadband
        self.kWheelDeadband

        self.kHighWheelNonLinearity
        self.kLowWheelNonLinearity

        self.kHighNegInertiaScalar

        self.kLowNegInertiaThreshold
        self.kLowNegInertiaTurnScalar
        self.kLowNegInertiaCloseScalar
        self.kLowNegInertiaFarScalar

        self.kHighSensitivity
        self.kLowSensitivity

        self.kQuickStopDeadband
        self.kQuickStopWeight
        self.kQuickStopScalar

        self.mOldWheel = 0
        self.mQuickStopAccumlator = 0
        self.mNegInertiaAccumlator = 0

    def drive(self, wheel, throtle, isQuickTurn, isHighGear):
        wheel = self.handledeadband(wheel, kWheelDeadband)
        negInertia = wheel - mOldWheel
        self.mOldWheel = wheel

        wheelNonLinearity
        if isHighGear:
            wheelNonLinearity = kHighWheelNonLinearity

    def handledeadband(self, value, deadband):
        return value if abs(value) >= deadband else 0
