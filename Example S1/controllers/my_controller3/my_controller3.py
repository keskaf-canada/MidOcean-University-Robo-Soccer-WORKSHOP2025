from controller import Robot

# Create robot instance
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Get and enable the ball receiver
receiver = robot.getDevice("ball receiver")
if receiver is None:
    print("❌ ERROR: Ball receiver not found.")
    exit()

receiver.enable(timestep)
print("🟢 Ball receiver enabled and controller started...")

while robot.step(timestep) != -1:
    if receiver.getQueueLength() > 0:
        direction = receiver.getDirection()
        x = direction[0]
        y = direction[1]

        if y > 0.7:
            print("⚽ Ball is in FRONT")
        elif x < -0.2:
            print("⚽ Ball is on the LEFT")
        elif x > 0.2:
            print("⚽ Ball is on the RIGHT")
        else:
            print("⚽ Ball location unclear")

        receiver.nextPacket()

