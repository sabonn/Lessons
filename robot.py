import commands2
import wpilib
from RobotContainer import RobotContainer
import Constants

class MyRobot(commands2.TimedCommandRobot):

    def robotInit(self) -> None:
        self.schedular = commands2.CommandScheduler.getInstance()
        self.container = RobotContainer()
        self.auto_command = self.container.get_autonomous_command()
        return super().robotInit()

    def robotPeriodic(self) -> None:
        commands2.CommandScheduler.getInstance().run()
        return super().robotPeriodic()

    def autonomousInit(self) -> None:
        if self.auto_command is not None:
            self.auto_command.schedule()
        return super().autonomousInit()

    def autonomousPeriodic(self) -> None:
        return super().autonomousPeriodic()

    def teleopInit(self) -> None:
        if self.auto_command is not None:
            self.auto_command.cancel()
        return super().teleopInit()

    def teleopPeriodic(self) -> None:
        return super().teleopPeriodic()

if __name__ == "__main__":
    wpilib.run(MyRobot)
