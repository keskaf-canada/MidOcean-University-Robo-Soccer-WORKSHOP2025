# Dr.Khaled Eskaf
#Professor of Intelligent Systems
#khaled.eskaf@mail.mcgill.ca



# rcj_soccer_player controller - ROBOT B1
# وحدة التحكم بالروبوت B1

# ----------------------------
# Import the Webots Robot API
# استيراد واجهة برمجة التطبيقات الخاصة بـ Webots للتحكم بالروبوت
from controller import Robot

# ----------------------------
# Import helper function to decide direction
# استيراد ملف utils الذي يحتوي على دالة تساعد الروبوت في تحديد اتجاه الكرة
import utils

# ----------------------------
# Import base robot configuration (sensors, motors, etc.)
# استيراد الكلاس RCJSoccerRobot الذي يربط بين الحساسات والمحركات
# واستيراد TIME_STEP لتحديد الزمن بين كل خطوة في الحلقة
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP

# ----------------------------
# Create an instance of the Robot class from Webots
# إنشاء كائن من كلاس Robot لتوصيل الكود مع الروبوت الموجود في المحاكاة
robot_api = Robot()

# ----------------------------
# Create our custom soccer robot object using the Webots robot
# تحويل الروبوت العادي إلى روبوت ذكي باستخدام كلاس RCJSoccerRobot
# الكلاس هذا يُفعّل الحساسات والمحركات ويجعل استخدامها أسهل
robot = RCJSoccerRobot(robot_api)

# ----------------------------
# This loop keeps running as long as the simulation is active
# هذه الحلقة تستمر في العمل كل TIME_STEP وتسمح للروبوت بأن يتصرف بشكل مستمر
while robot_api.step(TIME_STEP) != -1:

    # -----------------------------------
    # Check if there is new ball data (from the IR ball sensor)
    # التحقق مما إذا كانت هناك بيانات جديدة من حساس الكرة (الأشعة تحت الحمراء)
    if robot.is_new_ball_data():

        # -----------------------------------
        # Get the direction and strength of the ball's signal
        # الحصول على اتجاه الكرة بناءً على البيانات القادمة من الحساس
        ball_data = robot.get_new_ball_data()

        # -----------------------------------
        # Use a helper function to decide how to move based on the ball direction
        # استخدام الدالة get_direction لتحديد كيف يجب أن يتحرك الروبوت
        # 0 = الكرة أمام الروبوت → يتحرك للأمام
        # 1 = الكرة على اليسار → يلف لليسار
        # -1 = الكرة على اليمين → يلف لليمين
        direction = utils.get_direction(ball_data["direction"])

        # -----------------------------------
        # Decide how fast each wheel should spin based on ball direction
        # تحديد سرعة كل عجلة بناءً على اتجاه الكرة
        if direction == 0:
            # إذا كانت الكرة أمام الروبوت، يتحرك للأمام بسرعة متساوية
            left_speed = 7
            right_speed = 7
        else:
            # إذا كانت الكرة على اليسار أو اليمين، يقوم بالدوران تجاهها
            # direction = 1 → يدور لليسار
            # direction = -1 → يدور لليمين
            left_speed = direction * 4
            right_speed = direction * -4

        # -----------------------------------
        # Set the wheel speeds to move the robot
        # تطبيق السرعات المحسوبة على المحركات لتحريك الروبوت
        robot.left_motor.setVelocity(left_speed)
        robot.right_motor.setVelocity(right_speed)

    else:
        # -----------------------------------
        # If the ball is not detected, stop the robot
        # إذا لم يرَ الروبوت الكرة، يتم إيقاف المحركات ليبقى في مكانه
        robot.left_motor.setVelocity(0)
        robot.right_motor.setVelocity(0)


