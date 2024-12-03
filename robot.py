import commands2
import wpilib
from RobotContainer import RobotContainer


class MyRobot(commands2.TimedCommandRobot):
    # robot mode
    def robotInit(self):
        self.container = RobotContainer()
        self.schedular = commands2.CommandScheduler.getInstance()
        return super().robotInit()

    def robotPeriodic(self):
        self.schedular.getInstance().run()
        return super().robotPeriodic()

    # autonomus
    def autonomousInit(self):
        return super().autonomousInit()

    def autonomousPeriodic(self):

        self.container.getTurnCommand().schedule()
        return super().autonomousPeriodic()

    # teleoperated mod
    def teleopInit(self):
        self.container.getmanoacommand().schedule()
        return super().teleopInit()

    def teleopPeriodic(self):
        self.container.getSpinCommand().schedule()
        return super().teleopPeriodic()


if __name__ == "__main__":
    wpilib.run(MyRobot)
