import wpilib

from autonBaseInit import *

from functools import partial


class AutonInterpreter(autonBaseInit):

    def __init__(self,side, switchPosition, scalePosition, driveTrain):#,   name):
        super().__init__(side, switchPosition, scalePosition, driveTrain)
        #self.drive = "AYYY"

        self.lift_pos = 0

        with open("/home/lvuser/prog_auton.txt") as f:	#"/home/svanderark/FRC_2018/GUI/test_prog_auton.txt"
            name = f.readline().strip()
        #print("sfhdjkfhwsdkjfhjskdhfjksdhfkjsd\t" + name)
        self.masterlist = []
        self.default_loc = "/home/lvuser/prog_auton_dir/" #"/home/svanderark/FRC_2018/GUI/convert/"
        with open(self.default_loc + name, "r") as f:
            data = f.readlines()
            i = 0
            del data[0] #first line is absolute position, for later re-import
            del data[0] #let's assume it starts facing the right way
            for line in data:
                i += 1
                temp = line[:-1].split(",")
                if temp[0] == "0":
                    self.masterlist.append(partial(self.bloob, self.drive, i, 0, float(temp[1]), float(temp[2]), 0, 0, self.lift_pos))
                elif temp[0] == "1":
                    turnSpeed = 0.5
                    self.masterlist.append(partial(self.bloob, self.drive, i, 1, 0, 0, float(temp[1]), float(turnSpeed), self.lift_pos))
                elif temp[0] == "2":
                    self.lift_pos = float(temp[1])
    def run(self):
        for i in self.masterlist:
            i()

    def bloob(self, a, b, c, d, e, f, g, _h=0, _i=0, _j=0):
        #print(str(a) + "\t" + str(b) + "\t" + str(c) + "\t" + str(d) + "\t" + str(e) + "\t" + str(f) + "\t" + str(g) + "\t" + str(_h) + "\t" + str(_i) + "\t" + str(_j))
        a.autonMove(b,c,d,e,f,g,_h,_i, _j)
