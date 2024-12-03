import Constants
import phoenix6
from commands2 import Subsystem

class manoa(Subsystem):
    def __init__(self):
      self.motor = phoenix6.hardware.talon_fx.TalonFX(Constants.Manoa.id)
      self.control = phoenix6.controls.VoltageOut(0.0)

    def Voltagerun(self):
     self.motor.set_control(self.control.with_output(Constants.Manoa.Voltage)) 
    
    def STOP(self):
      self.motor.set_control(self.control.with_output(0))
