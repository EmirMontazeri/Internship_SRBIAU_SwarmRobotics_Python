import pybullet as p
import pybullet_data
import time
import numpy as np

# Connect to the physics simulation
physicsClient = p.connect(p.GUI)

# Set up the search path for URDF models
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load the plane (the ground)
planeId = p.loadURDF("plane.urdf")

# Load R2D2 at a starting position
r2d2Id = p.loadURDF("r2d2.urdf", [2, -2, 0.5])

# Set gravity in the environment
p.setGravity(0, 0, -9.81)

# Load the cube with a scaling factor (15) and repositioned to (0, 0, 0.5)
cubeId = p.loadURDF("cube_small.urdf", [0, 0, 0.5], globalScaling=15)  # Cube scaled to 15x size

# Function to move R2D2 in its current heading
def move_robot(r2d2_id, key_dict):
    velocity = 0
    turn = 0

    # Adjust velocities based on key inputs
    if key_dict.get(p.B3G_UP_ARROW):
        velocity = 2  # Move forward
    elif key_dict.get(p.B3G_DOWN_ARROW):
        velocity = -2  # Move backward
    if key_dict.get(p.B3G_LEFT_ARROW):
        turn = 1  # Turn left
    elif key_dict.get(p.B3G_RIGHT_ARROW):
        turn = -1  # Turn right

    # Get the current orientation of the robot in quaternion form
    position, orientation = p.getBasePositionAndOrientation(r2d2_id)

    # Convert quaternion orientation to Euler angles (yaw, pitch, roll)
    euler_orientation = p.getEulerFromQuaternion(orientation)

    # Get the yaw (rotation around Z axis) and adjust it by 90 degrees (pi/2 radians)
    yaw = euler_orientation[2] + np.pi / 2  # Adjust for initial 90-degree offset

    # Compute the forward direction vector based on adjusted yaw
    forward_direction = [np.cos(yaw), np.sin(yaw), 0]

    # Multiply the forward direction by the velocity
    velocity_vector = [velocity * forward_direction[0], velocity * forward_direction[1], 0]

    # Set the linear and angular velocities for R2D2
    p.resetBaseVelocity(r2d2_id, linearVelocity=velocity_vector, angularVelocity=[0, 0, turn])

# Function to measure distance to the closest object in front of R2D2
def distance_sensor(r2d2_id):
    # Get the current position and orientation of the robot
    position, orientation = p.getBasePositionAndOrientation(r2d2_id)
    
    # Convert quaternion orientation to Euler angles (yaw, pitch, roll)
    euler_orientation = p.getEulerFromQuaternion(orientation)
    
    # Get the yaw (rotation around Z axis) and adjust it by 90 degrees (pi/2 radians)
    yaw = euler_orientation[2] + np.pi / 2  # Adjust for initial 90-degree offset
    
    # Define the depth (5 meters) in front of the robot
    depth = 5.0
    
    # Compute the front position of the sensor (5 blocks in front of the robot)
    sensor_front = [position[0] + depth * np.cos(yaw), position[1] + depth * np.sin(yaw), position[2]]
    
    # Initialize minimum distance to a large value
    min_distance = float('inf')
    
    # Check distance to the cube
    obj_position = p.getBasePositionAndOrientation(cubeId)[0]
    
    # Calculate distance to the object
    distance = np.linalg.norm(np.subtract(sensor_front, obj_position))
    min_distance = min(min_distance, distance)
    
    if min_distance == float('inf'):
        print("No object detected within the sensor range.")
    else:
        print(f"Distance to nearest object in front of the robot: {min_distance:.2f} meters")

# Main simulation loop
while True:
    # Get pressed keys
    keys = p.getKeyboardEvents()

    # Exit the loop if Escape (key code 27) is pressed
    if 27 in keys and keys[27] & p.KEY_WAS_TRIGGERED:
        print("Escape key pressed. Exiting...")
        break

    # Move R2D2 based on key input
    move_robot(r2d2Id, keys)

    # Measure distance to the closest object in front of R2D2
    distance_sensor(r2d2Id)

    # Check for collisions with the cube
    contact_points = p.getContactPoints(r2d2Id, cubeId)
    if contact_points:
        print("R2D2 collided with the cube!")

    # Step the simulation forward
    p.stepSimulation()
    
    # Sleep to maintain real-time simulation speed
    time.sleep(1./240.)

# Properly disconnect from the simulation
p.disconnect()
