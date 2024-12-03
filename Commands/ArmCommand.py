import robot
from commands2 import Command
from SubSystem import ArmSubsys

class ArmCommand(Command):
    def __init__(self, subsys:ArmSubsys.arm,angle:float):
        self.angle = angle
        self.subsys = subsys
        super().__init__()

    def initialize(self):
        return super().initialize()
    
    def execute(self):
        pos = self.subsys.angleToCycle(self.angle)
        self.subsys.arm.getToPosition(pos)
        return super().execute()
    
    def end(self, interrupted):
        self.subsys.stop()
        return super().end(interrupted)
    
    def isFinished(self):
        if abs(self.subsys.getCurrentAngle() - self.angle) <= 0.5:#minimum angle for correction
            return True
        return super().isFinished()
