from commands2 import Command
from commands2 import button
import Constants
from SubSystem import ElevatorSubsys, IntakeSubsys, ShooterSubsys, ArmSubsys
from Commands import IntakeCommand, ElevatorCommand, ArmCommand

class RobotContainer:
    def __init__(self) -> None:
        self.xboxController = button.CommandXboxController(Constants.Controller.xboxControllerId)
        self.intakeSubsys = IntakeSubsys.intake()
        self.elevator = ElevatorSubsys.elevator()
        self.shooter = ShooterSubsys.shooter()
        self.arm = ArmSubsys.arm()

        self.ControllerBindings()

    def ControllerBindings(self) -> None:
        self.xboxController.a().onTrue(IntakeCommand.intakeCommand(self.intakeSubsys))
        self.xboxController.x().toggleOnTrue(ElevatorCommand.elevatorCommand(self.elevator,1.5))
        self.xboxController.y().toggleOnTrue(ArmCommand.ArmCommand(self.arm,30))

    def get_autonomous_command() -> Command:
        return None
