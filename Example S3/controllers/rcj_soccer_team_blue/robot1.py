# Dr.Khaled Eskaf
# Professor of Intelligent Systems
# khaled.eskaf@mail.mcgill.ca

# rcj_soccer_player controller - ROBOT B1
# وحدة التحكم بالروبوت B1

# ----------------------------
# Import the Webots Robot API
# استيراد مكتبة Webots للتحكم في الروبوت
from controller import Robot

# ----------------------------
# Import helper function to decide direction
# استيراد دالة تساعد في تحديد اتجاه الكرة
import utils

# ----------------------------
# Import robot base and time step
# استيراد كلاس الروبوت الذي يربط الحساسات والمحركات
# واستيراد الثابت TIME_STEP لتحديد مدة كل خطوة في الحلقة
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP

# ----------------------------
# Create Webots robot object
# إنشاء كائن الروبوت من مكتبة Webots
robot_api = Robot()

# ----------------------------
# Create our soccer robot using RCJSoccerRobot class
# تحويل الروبوت إلى روبوت كرة قدم ذكي
robot = RCJSoccerRobot(robot_api)

# ----------------------------
# Target heading to face the yellow goal
# الزاوية المطلوبة لمواجهة مرمى الفريق الأصفر (اليسار)
TARGET_HEADING = 0.0  # radians

# ----------------------------
# Main loop runs until simulation stops
# حلقة التحكم الأساسية للروبوت
while robot_api.step(TIME_STEP) != -1:

    # ✅ Step 1: Read compass heading
    # 🧭 الخطوة الأولى: قراءة اتجاه الروبوت الحالي باستخدام البوصلة
    current_heading = robot.get_compass_heading()

    # ✅ Step 2: Calculate angular error
    # حساب الفرق بين الاتجاه الحالي والهدف (المرمى الأصفر)
    angle_diff = TARGET_HEADING - current_heading

    # 🔁 Normalize angle to range [-π, π]
    # جعل الفرق بين الزوايا ضمن المجال [-π, π]
    if angle_diff > 3.14:
        angle_diff -= 2 * 3.14
    elif angle_diff < -3.14:
        angle_diff += 2 * 3.14

    # ✅ Step 3: Movement decision
    # 🧠 منطق تحديد حركة الروبوت بناءً على اتجاهه الحالي

    if abs(angle_diff) < 0.1:
        print("✅ Facing yellow goal, moving forward...")
        left_speed = 6
        right_speed = 6
    elif angle_diff > 0.1:
        print(f"🔄 Turning left ({round(angle_diff, 2)} rad) toward yellow goal...")
        left_speed = -2
        right_speed = 2
    else:
        print(f"🔁 Turning right ({round(angle_diff, 2)} rad) toward yellow goal...")
        left_speed = 2
        right_speed = -2

    # ✅ Step 4: Apply speed to motors
    # تعيين السرعات للمحركات لتحريك الروبوت
    robot.left_motor.setVelocity(left_speed)
    robot.right_motor.setVelocity(right_speed)
