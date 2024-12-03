from Constants import Turn
from commands2 import Command
from Subsystems import TurnSubsys
import wpilib


class TurnCommand(Command):
    def __init__(self, Subsystem: TurnSubsys.TurnSubsys):
        self.Subsystem = Subsystem
        super().__init__()

    def initialize(self):
        self.timer = wpilib.Timer.get()
        return super().initialize()

    def execute(self):
        self.Subsystem.run()
        return super().execute()

    def end(self, interrupted):
        self.Subsystem.stop()
        return super().end(interrupted)

    def isFinished(self):
        if abs(self.timer - wpilib.Timer.get()) > Turn.maxTime:
            return True
        return super().isFinished()
