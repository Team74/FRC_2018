import wpilib

from autonBaseInit import *

from functools import partial


class AutonInterpreter(autonBaseInit):

    def __init__(self,side, switchPosition, scalePosition, driveTrain):#,   name):
        super().__init__(side, switchPosition, scalePosition, driveTrain)

        with open("/home/lvuser/prog_auton.txt") as f:
            name = f.readline().strip()
        print("sfhdjkfhwsdkjfhjskdhfjksdhfkjsd\t" + name)
        self.masterlist = []
        self.default_loc = "/home/lvuser/prog_auton_dir/" #"/home/svanderark/FRC_2018/GUI/convert/"
        with open(self.default_loc + name, "r") as f:
            lift_pos = 0
            intake_mode = 0

            data = f.readlines()
            i = 0
            del data[0] #first line is absolute position, for later re-import
            del data[0] #let's assume it starts facing the right way
            for line in data:
                i += 1
                temp = line[:-1].split(",")
                if temp[0] == "0":
                    self.masterlist.append(partial(self.bloob, self.drive, i, 0, float(temp[1]), float(temp[2]), 0, 0, lift_pos, intake_mode))
                elif temp[0] == "1":
                    turnSpeed = 0.5
                    self.masterlist.append(partial(self.bloob, self.drive, i, 1, 0, 0, float(temp[1]), float(turnSpeed), lift_pos, intake_mode))
                elif temp[0] == "2":
                    lift_pos = int(temp[1])
                elif temp[0] == "3":
                    intake_mode = int(temp[1])
                else:
                    self.masterlist.append(partial(self.bloob, self.drive, i, float(temp[0]), 0,0,0,0, lift_pos, intake_mode))
    def run(self):
        for i in self.masterlist:
            i()

    def bloob(self, a, b, c, d, e, f, g, h, i):
        a.autonMove(b,c,d,e,f,g,h,i,0)
