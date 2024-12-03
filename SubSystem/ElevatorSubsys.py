from commands2 import Subsystem
import rev
import Constants
import math

#radius of spindel = 0.1(m)
class elevator(Subsystem):
    def __init__(self):
        #motor
        self.leftMotor = rev.CANSparkMax(Constants.Elevator.leftMotorID, rev.CANSparkMax.MotorType.kBrushless)
        self.rightMotor = rev.CANSparkMax(Constants.Elevator.rightMotorID, rev.CANSparkMax.MotorType.kBrushless)
        #encoder
        self.leftEncoder = self.leftMotor.getEncoder()
        self.rightEncoder = self.rightMotor.getEncoder()
        #controller
        self.leftController = self.leftMotor.getPIDController()
        self.rightController = self.rightMotor.getPIDController()

        self.configMotor(self.leftMotor,self.leftController)
        self.configMotor(self.rightMotor,self.rightController)
        super().__init__()

    def configMotor(self, motor:rev.CANSparkMax, controller: rev.SparkPIDController) -> None:
        motor.restoreFactoryDefaults()
        #empty on porpus(those are just values needed to be entered) search for PID values and feed forward for an explanation
        controller.setP()
        controller.setI()
        controller.setD()
        controller.setFF()
        controller.setSmartMotionMaxAccel()
        controller.setSmartMotionMaxVelocity()

    def getHeight(self) -> float:
        precentRotation = self.leftEncoder.getPosition()/360
        height = precentRotation*2*math.pi*0.1
        return height

    def heightToAngle(self, dHeight) -> float:
        pRotation = dHeight/(2*math.pi*0.1)
        angle = pRotation*360
        return angle

    def getToHeight(self, targetHeight:float):
        height = self.getHeight()
        dAngle = self.heightToAngle(targetHeight-height)
        angle = self.leftEncoder.getPosition()+dAngle
        self.leftController.setReference(rev.CANSparkMax.ControlType.kSmartMotion, angle)
        self.rightController.setReference(rev.CANSparkMax.ControlType.kSmartMotion, angle)

    def stop(self) -> None:
        self.leftMotor.set(0)
        self.rightMotor.set(0)
