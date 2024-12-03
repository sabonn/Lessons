import Constants
from commands2 import Command
import wpilib


class manoacommand(Command):
    def __init__(self, Subsys):
        self.subsys = Subsys
        self.timer=wpilib.Timer()
    def initialize(self):
        self.timer.reset()
        self.timer.start()
        return super().initialize()
    def isFinished(self):
        return self.timer.get()>=Constants.Manoa.MaxTime
    def execute(self):
       self.subsys.Voltagerun()
       print(self.timer.get())
       return super().execute()
    def end(self, interrupted):
       self.subsys.STOP()
       return super().end(interrupted)