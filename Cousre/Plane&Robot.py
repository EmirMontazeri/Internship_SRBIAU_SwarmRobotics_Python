import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)  
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
boxId = p.loadURDF("r2d2.urdf", [2, -2, 2])

p.setGravity(0, 0, -9.81)

for _ in range(1000):
    p.stepSimulation()
    time.sleep(1./240.)
p.resetBaseVelocity(robot_id, linearVelocity=[2, 0, 0], angularVelocity=[0, 0, 1])

p.disconnect()