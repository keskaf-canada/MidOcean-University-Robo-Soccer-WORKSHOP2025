# ========================================
# my_controller.py
# A simple controller to move the e-puck forward
# ========================================

# Step 1: Import the Robot class from the Webots API
from controller import Robot

# Step 2: Create an instance of the robot
robot = Robot()

# Step 3: Get the time step of the current world
# الوقت بين كل خطوة في المحاكاة (بالمللي ثانية)
timestep = int(robot.getBasicTimeStep())

# Step 4: Get the motors for the left and right wheels
# الحصول على المحركات اليمنى واليسرى لعجلات الروبوت
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Step 5: Set both motors to infinite rotation (velocity control)
# نحدد أن المحرك يعمل بسرعة (وليس تحديد موقع)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Step 6: Set the speed for both motors
# نحدد السرعة للمحركين - قيمة موجبة تعني للأمام
left_motor.setVelocity(3.0)
right_motor.setVelocity(3.0)

# Step 7: Main simulation loop
# حلقة تستمر أثناء تشغيل المحاكاة
while robot.step(timestep) != -1:
    pass  # لا نقوم بأي شيء آخر، فقط نستمر في الحركة للأمام
