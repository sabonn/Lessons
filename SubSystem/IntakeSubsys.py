from commands2 import Subsystem
import rev
import Constants

class intake(Subsystem):
    def __init__(self):
        self.motor = rev.CANSparkMax(Constants.Intake.motorID,rev.CANSparkMax.MotorType.kBrushless)
        super().__init__()

    def activate(self) -> None:
        self.motor.set(Constants.Intake.intakePower)

    def stop(self) -> None:
        self.motor.set(0)