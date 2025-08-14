# Dr.Khaled Eskaf
# Professor of Intelligent Systems
# khaled.eskaf@mail.mcgill.ca
############### IMPORTANT NOTE, Please dont modify in this code of Robot 3####


# ----------------------------
# ✅ Import necessary modules
# استيراد المكتبات الضرورية
import math                          # مكتبة الرياضيات (قد نحتاجها لاحقاً)
import utils                        # ملف يحتوي على دوال مساعدة
from controller import Robot       # استيراد واجهة Webots
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP  # استيراد كلاس الروبوت الذكي و الزمن بين كل خطوة

# ----------------------------
# ✅ إنشاء الكائنات الأساسية
# Create main robot object
robot_api = Robot()

# تحويل الروبوت العادي إلى روبوت ذكي لسهولة التعامل مع الحساسات والمحركات
robot = RCJSoccerRobot(robot_api)

# ----------------------------
# ✅ بداية الحلقة الرئيسية
# Start the main control loop
while robot_api.step(TIME_STEP) != -1:

    # التحقق إذا وصلت رسالة جديدة من المشرف (الحكم)
    if robot.is_new_data():
        data = robot.get_new_data()  # استلام الرسالة الجديدة

        # التحقق من وجود رسالة من زميل في الفريق
        while robot.is_new_team_data():
            team_data = robot.get_new_team_data()
            # يمكن لاحقاً استخدام بيانات الفريق

        # التحقق من رؤية الكرة باستخدام الحساس تحت الحمراء
        if robot.is_new_ball_data():
            ball_data = robot.get_new_ball_data()
        else:
            # إذا لم يتم رؤية الكرة، يتم إيقاف الروبوت
            robot.left_motor.setVelocity(0)
            robot.right_motor.setVelocity(0)
            continue  # العودة لبداية الحلقة

        # الحصول على الاتجاه الذي يواجهه الروبوت باستخدام البوصلة
        heading = robot.get_compass_heading()

        # الحصول على موقع الروبوت على الملعب باستخدام GPS
        robot_pos = robot.get_gps_coordinates()

        # الحصول على بيانات الحساسات الأمامية والخلفية (اختياري)
        sonar_values = robot.get_sonar_values()

        # استخدام الدالة المساعدة لتحديد اتجاه الكرة: أمام / يسار / يمين
        direction = utils.get_direction(ball_data["direction"])

        # ✅ اتخاذ القرار: إذا كانت الكرة أمام الروبوت → تقدم
        # إذا كانت على اليسار أو اليمين → لف باتجاهها
        if direction == 0:
            left_speed = 7     # العجلة اليسرى
            right_speed = 7    # العجلة اليمنى
        else:
            left_speed = direction * 4
            right_speed = direction * -4

        # إرسال السرعات للمحركات
        robot.left_motor.setVelocity(left_speed)
        robot.right_motor.setVelocity(right_speed)

        # إرسال رسالة لزملاء الفريق تحتوي على رقم هذا الروبوت
        robot.send_data_to_team(robot.player_id)