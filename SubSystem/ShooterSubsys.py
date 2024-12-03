from commands2 import Subsystem
import phoenix6
import Constants

#NOT DOING A COMMAND FOR THIS, THE COMMAND WOULD BE JUST LIKE FOR THE INTAKE

class shooter(Subsystem):
    def __init__(self):
        self.leftMotor = phoenix6.hardware.TalonFX(Constants.Shooter.leftMotorID)
        self.rightMotor = phoenix6.hardware.TalonFX(Constants.Shooter.rightMotorID)#creating the motors

        self.letfControl = phoenix6.controls.Follower(Constants.Shooter.rightMotorID, Constants.Shooter.leftMotorReversed)#A follower 'follows' the actions of the motor its assigned to
        self.rightControl = phoenix6.controls.DutyCycleOut(0)#the starting output is zero, it would be updated later

        # With the controls we control how the motor will act, we decided to use DutyCycleOut(Precent Power)
        # We control the power by changing the output of the control variable
        self.leftMotor.set_control(self.letfControl)
        self.rightMotor.set_control(self.rightControl)
        super().__init__()

    def activate(self) -> None:
        self.rightControl.output = Constants.Shooter.shootPower

    def stop(self) -> None:
        self.rightControl.output = 0