# Dr.Khaled Eskaf
#Professor of Intelligent Systems
#khaled.eskaf@mail.mcgill.ca

from controller import Robot
from robot1 import MyRobot1

robot = Robot()
robot_controller = MyRobot1(robot)
robot_controller.run()
