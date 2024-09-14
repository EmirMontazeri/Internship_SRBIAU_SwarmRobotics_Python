import pybullet as p
import pybullet_data
import time

# Start the physics simulation
p.connect(p.GUI)

# Set up search path for URDF models
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load a plane
p.loadURDF("plane.urdf")

# Load a robot arm (KUKA model)
robot_id = p.loadURDF("kuka_iiwa/model.urdf", useFixedBase=True)

# Set gravity
p.setGravity(0, 0, -9.8)

# Get the number of joints in the robot
num_joints = p.getNumJoints(robot_id)

# Print joint info (optional, for exploration)
for i in range(num_joints):
    joint_info = p.getJointInfo(robot_id, i)
    print(joint_info)

# Control the robot by moving its joints
for t in range(1000):
    target_position = t * 0.05  # Small movement increment
    p.setJointMotorControl2(robot_id, 1, p.POSITION_CONTROL, target_position)
    p.stepSimulation()
    time.sleep(1./240.)

# Disconnect the simulation
p.disconnect()
