from commands2 import Command


class spinCommand(Command):
    def __init__(self, container):
        self.container = container
        super().__init__()

    def initialize(self):
        self.container.getSpinSubsys().execute()
        return super().initialize()

    def execute(self):
        return super().execute()

    def end(self, interrupted):
        self.container.getSpinSubsys().stop()
        return super().end(interrupted)

    def isFinished(self):
        return super().isFinished()
