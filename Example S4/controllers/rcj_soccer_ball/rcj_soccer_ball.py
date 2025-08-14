# Dr.Khaled Eskaf
# Professor of Intelligent Systems
# khaled.eskaf@mail.mcgill.ca

from controller import Robot

robot = Robot()
ball_emitter = robot.getDevice("ball emitter")

data = "x"  # Packet cannot be empty

while robot.step(32) != -1:
    ball_emitter.send(data)
