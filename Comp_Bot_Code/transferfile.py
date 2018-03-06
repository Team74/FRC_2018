def manipulatorControl(self, aButton, xButton, yButton):
      if aButton:
          self.toggle = 1
      elif xButton:
          self.toggle = 2
      elif yButton:
          self.toggle = 0
      if self.toggle == 0:
          self.leftManipulatorMotor.set(0)
          self.rightManipulatorMotor.set(0)
      elif self.toggle == 1:
          self.leftManipulatorMotor.set(-1)
          self.rightManipulatorMotor.set(-1)
      elif self.toggle == 2:
          self.leftManipulatorMotor.set(1)
          self.rightManipulatorMotor.set(1)
