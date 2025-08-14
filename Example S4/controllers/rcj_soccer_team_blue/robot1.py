# Dr.Khaled Eskaf
# Professor of Intelligent Systems
# khaled.eskaf@mail.mcgill.ca


# ----------------------------------------
# Step 1: Import necessary libraries
# استيراد المكتبات اللازمة
import math                          # مكتبة الرياضيات لحساب الزاوية
import utils                         # ملف utils يحتوي على دالة get_direction لتحديد اتجاه الكرة
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP  # استيراد كلاس الروبوت والزمن

# ----------------------------------------
# Step 2: Create the robot object
# إنشاء كائن الروبوت باستخدام الكلاس RCJSoccerRobot
from controller import Robot
robot_api = Robot()                 # هذا هو الروبوت في المحاكاة
robot = RCJSoccerRobot(robot_api)  # تحويله إلى روبوت ذكي باستخدام RCJSoccerRobot

# ----------------------------------------
# Step 3: Start the main control loop
# بدء الحلقة الرئيسية للتحكم في الروبوت
while robot_api.step(TIME_STEP) != -1:

    # ----------------------------------------
    # Step 4: Check for new ball data
    # التحقق من وجود بيانات جديدة من حساس الكرة
    if robot.is_new_ball_data():
        ball_data = robot.get_new_ball_data()  # الحصول على بيانات الكرة
    else:
        # إذا لم تُكتشف الكرة، أوقف الروبوت
        # If ball is not detected, stop the robot
        robot.left_motor.setVelocity(0)
        robot.right_motor.setVelocity(0)
        print("⛔ Ball not detected - stopping.")
        continue  # العودة لبداية الحلقة

    # ----------------------------------------
    # Step 5: Get compass angle (heading)
    # قراءة زاوية الاتجاه من البوصلة (الرأسية)
    heading = robot.get_compass_heading()
    print("🧭 Compass heading (زاوية الاتجاه):", heading)

    # ----------------------------------------
    # Step 6: Get GPS position of the robot
    # الحصول على موقع الروبوت باستخدام GPS
    robot_pos = robot.get_gps_coordinates()
    print("📍 Robot Position (الموقع):", robot_pos)

    # ----------------------------------------
    # Step 7: Get sonar sensor values
    # قراءة قيم حساسات الموجات فوق الصوتية
    sonar = robot.get_sonar_values()
    print("🔊 Sonar values (الحساسات):", sonar)

    # ----------------------------------------
    # Step 8: Compute direction of the ball
    # تحديد اتجاه الكرة باستخدام الدالة get_direction
    direction = utils.get_direction(ball_data["direction"])
    print("⚽ Ball Direction (اتجاه الكرة):", direction)

    # ----------------------------------------
    # Step 9: Decide movement
    # تحديد حركة الروبوت بناءً على اتجاه الكرة
    if direction == 0:
        # الكرة أمام الروبوت → تحرك للأمام
        # Ball in front → Go straight
        left_speed = 7
        right_speed = 7
        print("🚀 Moving Forward toward ball (الكرة أمام الروبوت)")
    elif direction == 1:
        # الكرة على اليسار → لف لليسار
        # Ball on the left → Turn left
        left_speed = 4
        right_speed = -4
        print("↩️ Turning LEFT toward ball (الكرة على اليسار)")
    elif direction == -1:
        # الكرة على اليمين → لف لليمين
        # Ball on the right → Turn right
        left_speed = -4
        right_speed = 4
        print("↪️ Turning RIGHT toward ball (الكرة على اليمين)")

    # ----------------------------------------
    # Step 10: Set motor speeds
    # إرسال السرعات إلى المحركات
    robot.left_motor.setVelocity(left_speed)
    robot.right_motor.setVelocity(right_speed)

    # ----------------------------------------
    # Step 11: Send message to teammates (optional)
    # إرسال رسالة للفريق (اختياري)
    robot.send_data_to_team(robot.player_id)
    print("📡 Sending data to team (تم إرسال البيانات إلى الفريق)")
