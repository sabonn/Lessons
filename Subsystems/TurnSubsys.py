import Constants
import rev
from commands2 import Subsystem


class TurnSubsys(Subsystem):
    def __init__(self):
        self.motor = rev.CANSparkMax(
            Constants.Turn.id, rev.CANSparkMax.MotorType.kBrushless
        )
        super().__init__()

    def run(self):
        self.motor.set(Constants.Turn.power)

    def stop(self):
        self.motor.set(0)
