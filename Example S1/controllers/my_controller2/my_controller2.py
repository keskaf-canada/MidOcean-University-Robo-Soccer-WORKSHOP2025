# Detect ball direction and print: Left, Right, or Front

from controller import Robot

# Create Robot instance
robot = Robot()
timestep = int(robot.getBasicTimeStep())  # Get simulation step time (e.g., 32 ms)

# Initialize left and right wheel motors
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Set motors to velocity control mode
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Enable the ball receiver sensor
ball_receiver = robot.getDevice("ball receiver")
ball_receiver.enable(timestep)

# Main control loop
while robot.step(timestep) != -1:
    # Check if there is a new ball signal received
    if ball_receiver.getQueueLength() > 0:
        # Get the direction of the ball relative to the robot
        direction = ball_receiver.getDirection()  # [x, y, z] vector
        x = direction[0]  # Left/Right
        y = direction[1]  # Front/Back

        # Decision logic based on direction
        if y > 0.7:
            print("⚽ Ball is in FRONT")
        elif x < -0.2:
            print("⚽ Ball is on the LEFT")
        elif x > 0.2:
            print("⚽ Ball is on the RIGHT")
        else:
            print("⚽ Ball location unclear")

        # Move to the next packet (clear current)
        ball_receiver.nextPacket()
