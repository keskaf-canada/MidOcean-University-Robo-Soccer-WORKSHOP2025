# Dr.Khaled Eskaf
#Professor of Intelligent Systems
#khaled.eskaf@mail.mcgill.ca


# rcj_soccer_robot.py - for robot B1 only
# كود مبسط للتحكم بروبوت B1 فقط

import math  # For compass angle calculations / لحساب الاتجاهات باستخدام البوصلة

# Set the time step (frame update rate)
# تحديد الزمن بين كل تحديث للمحاكاة (كل 32 ميلي ثانية)
TIME_STEP = 32


class RCJSoccerRobot:
    def __init__(self, robot):
        # Save the Webots robot object
        # حفظ كائن الروبوت من Webots
        self.robot = robot

        # --- Ball Sensor (IR) - حساس الكرة ---
        self.ball_receiver = self.robot.getDevice("ball receiver")
        self.ball_receiver.enable(TIME_STEP)

        # --- Compass Sensor - حساس الاتجاه ---
        self.compass = self.robot.getDevice("compass")
        self.compass.enable(TIME_STEP)

        # --- GPS Sensor - حساس الموقع ---
        self.gps = self.robot.getDevice("gps")
        self.gps.enable(TIME_STEP)

        # --- Motors - المحركات ---
        self.left_motor = self.robot.getDevice("left wheel motor")
        self.right_motor = self.robot.getDevice("right wheel motor")

        # Set motors to velocity mode (not position mode)
        # تفعيل المحركات بوضع السرعة وليس الموضع
        self.left_motor.setPosition(float("inf"))
        self.right_motor.setPosition(float("inf"))

        # Start with both wheels stopped
        # البدء بتوقف العجلات
        self.left_motor.setVelocity(0.0)
        self.right_motor.setVelocity(0.0)

    # --- Ball Detection Function ---
    # دالة الحصول على بيانات الكرة
    def get_new_ball_data(self) -> dict:
        _ = self.ball_receiver.getString()  # We don't use the string
        ball_data = {
            "direction": self.ball_receiver.getEmitterDirection()[:3],  # اتجاه الكرة
            "strength": self.ball_receiver.getSignalStrength(),         # قوة الإشارة
        }
        self.ball_receiver.nextPacket()
        return ball_data

    # --- Ball Availability Check ---
    # التحقق إذا كانت هناك كرة جديدة مرصودة
    def is_new_ball_data(self) -> bool:
        return self.ball_receiver.getQueueLength() > 0

    # --- GPS Coordinates ---
    # الحصول على الموقع الحالي للروبوت (x, y)
    def get_gps_coordinates(self) -> list:
        gps_values = self.gps.getValues()
        return [gps_values[0], gps_values[1]]

    # --- Compass Heading ---
    # الحصول على اتجاه الروبوت بالراديان (0 تعني باتجاه الهدف)
    def get_compass_heading(self) -> float:
        compass_values = self.compass.getValues()
        heading = math.atan2(compass_values[0], compass_values[1]) + (math.pi / 2)
        if heading < -math.pi:
            heading += 2 * math.pi
        return heading
