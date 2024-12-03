from commands2 import Subsystem
import phoenix6

class arm(Subsystem):
    def __init__(self):
        self.stopControl = phoenix6.controls.DutyCycleOut(0)
        self.motor = phoenix6.hardware.TalonFX(0)
        self.magicMotion = phoenix6.controls.MotionMagicVoltage(0)
        talonfx_configs = phoenix6.configs.TalonFXConfiguration()

        # set slot 0 gains
        slot0_configs = talonfx_configs.slot0
        slot0_configs.k_s = 0.25 # Add 0.25 V output to overcome static friction
        slot0_configs.k_v = 0.12 # A velocity target of 1 rps results in 0.12 V output
        slot0_configs.k_a = 0.01 # An acceleration of 1 rps/s requires 0.01 V output
        slot0_configs.k_p = 4.8 # A position error of 2.5 rotations results in 12 V output
        slot0_configs.k_i = 0 # no output for integrated error
        slot0_configs.k_d = 0.1 # A velocity error of 1 rps results in 0.1 V output

        # set Motion Magic settings
        motion_magic_configs = talonfx_configs.motion_magic
        motion_magic_configs.motion_magic_cruise_velocity = 80 # Target cruise velocity of 80 rps
        motion_magic_configs.motion_magic_acceleration = 160 # Target acceleration of 160 rps/s (0.5 seconds)
        motion_magic_configs.motion_magic_jerk = 1600 # Target jerk of 1600 rps/s/s (0.1 seconds)

        self.motor.configurator.apply(talonfx_configs)
        super().__init__()

    def stop(self) -> None:
        self.motor.set_control(self.stopControl)

    def getToPosition(self, pos:float) -> None:
        self.motor.set_control(self.magicMotion.with_position(0))

    #the position functions of the Talon work with DutyCycles(How much did the motor rotate 360 degrees = 1 DutyCycle)
    def getCurrentAngle(self) -> float:
        cycle = self.motor.get_position()
        cycle *= 360
        return cycle

    def angleToCycle(self, angle:float) -> float:
        return angle/360
