from Constants import Spin
from commands2 import Command
from Subsystems import SpinSubsys
import wpilib


class spinCommand(Command):
    def __init__(self, subsystem: SpinSubsys.spinSubsys):
        self.subsystem = subsystem
        super().__init__()

    def initialize(self):

        self.subsystem.execute()
        return super().initialize()

    def execute(self):
        return super().execute()

    def end(self, interrupted):
        self.subsystem.stop()
        return super().end(interrupted)

    def isFinished(self):

        return super().isFinished()
