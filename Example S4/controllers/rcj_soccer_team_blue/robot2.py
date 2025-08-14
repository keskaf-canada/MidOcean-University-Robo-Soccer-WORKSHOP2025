# Dr.Khaled Eskaf
# Professor of Intelligent Systems
# khaled.eskaf@mail.mcgill.ca
############### IMPORTANT NOTE, Please dont modify in this code of Robot 2####



import math                      # مكتبة الرياضيات لحساب الزوايا
import utils                    # ملف يحتوي على دالة تحديد اتجاه الكرة
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP

# ⚙️ إنشاء الروبوت وتفعيله
robot_api = RCJSoccerRobot(RCJSoccerRobot)

# 🌀 حلقة تستمر طالما أن المحاكاة تعمل
while robot_api.robot.step(TIME_STEP) != -1:

    # ✅ التحقق من وصول بيانات من المشرف
    if robot_api.is_new_data():
        data = robot_api.get_new_data()

        # ✅ قراءة بيانات من زملاء الفريق (اختياري)
        while robot_api.is_new_team_data():
            team_data = robot_api.get_new_team_data()
            # لا نفعل شيء بهذه البيانات الآن

        # ⚽ محاولة قراءة بيانات الكرة
        if robot_api.is_new_ball_data():
            ball_data = robot_api.get_new_ball_data()
        else:
            # ❌ إذا لم تظهر الكرة، توقف عن الحركة
            robot_api.left_motor.setVelocity(0)
            robot_api.right_motor.setVelocity(0)
            continue

        # 🧭 قراءة اتجاه البوصلة
        heading = robot_api.get_compass_heading()

        # 📍 قراءة الموقع باستخدام GPS
        position = robot_api.get_gps_coordinates()

        # 🧠 حساب اتجاه الكرة: أمام / يمين / يسار
        direction = utils.get_direction(ball_data["direction"])

        # 🛞 تحديد سرعة العجلات
        if direction == 0:
            left_speed = 7
            right_speed = 7
        else:
            left_speed = direction * 4
            right_speed = direction * -4

        # ▶️ تشغيل العجلات
        robot_api.left_motor.setVelocity(left_speed)
        robot_api.right_motor.setVelocity(right_speed)

        # 📡 إرسال رسالة للفريق
        robot_api.send_data_to_team(robot_api.player_id)
