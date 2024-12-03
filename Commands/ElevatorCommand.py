import robot
from commands2 import Command
from SubSystem.ElevatorSubsys import elevator

class elevatorCommand(Command):
    def __init__(self, subsys:elevator ,targetHeight:float):
        self.targetHeight = targetHeight
        self.subsys = subsys
        super().__init__()

    def initialize(self):
        return super().initialize()

    def execute(self):
        #runs the main function
        self.subsys.getToHeight(self.targetHeight)
        return super().execute()

    def end(self, interrupted):
        self.subsys.stop()
        return super().end(interrupted)

    def isFinished(self):
        #this checks the difference in height
        if abs(self.targetHeight-self.subsys.getHeight()) < 0.05:
            return True
        return super().isFinished()
