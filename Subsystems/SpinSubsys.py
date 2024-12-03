from commands2 import Subsystem
import rev
import Constants


class spinSubsys(Subsystem):
    def __init__(self):
        self.motor = rev.CANSparkMax(
            Constants.Spin.id, rev.CANSparkMax.MotorType.kBrushless
        )
        super().__init__()

    def execute(self):
        self.motor.set(Constants.Spin.power)

    def stop(self):
        self.motor.set(0)
