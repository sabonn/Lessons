from commands2 import Command
import robot
from SubSystem.IntakeSubsys import intake

class intakeCommand(Command):
    def __init__(self, subsys: intake):
        self.subsys = subsys
        super().__init__()

    def initialize(self):
        return super().initialize()
    
    def execute(self):
        self.subsys.activate()
        return super().execute()
    
    def end(self, interrupted):
        self.subsys.stop()
        return super().end(interrupted)
    
    def isFinished(self):
        return super().isFinished()
