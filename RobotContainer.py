from Subsystems import SpinSubsys, TurnSubsys, manoa
from Commands import SpinCommand, TurnCommand, manoacommand
from commands2 import button

class RobotContainer:
    def __init__(self):
        self.spinSubsys = SpinSubsys.spinSubsys()
        self.spinCommand = SpinCommand.spinCommand(self.spinSubsys)
        self.TurnSubsys = TurnSubsys.TurnSubsys()
        self.TurnCommand = TurnCommand.TurnCommand(self.TurnSubsys)
        self.manoa=manoa.manoa()
        self.manoacommand= manoacommand.manoacommand(self.manoa)

    def getmanoacommand(self):
        return manoacommand.manoacommand(self.manoa)

    def getSpinCommand(self):
        return self.spinCommand

    def getTurnCommand(self):
        return self.TurnCommand
