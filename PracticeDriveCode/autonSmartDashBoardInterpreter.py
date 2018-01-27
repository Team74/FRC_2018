from autonNearSwitch import *
from autonCenterEitherSwitch import *
from autonTwoCubeScale import *
from autonNearScale import *
from autonDrive import *
from autonFarSwitch import *

class interprater():
    def interprate(self):
        self.side = blank #Either 'l' 'c' 'r'
        self.field = blank #Either 'll' 'lr' 'rl' 'rr'
        self.objective = blank #Either 'switch' 'scale' 'drive' 'drawn'
