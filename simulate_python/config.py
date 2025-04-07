ROBOT = "g1" # Robot name, "go2", "b2", "b2w", "h1", "go2w", "g1"
DOF = "_29dof_with_hand" # "" for other than g1, "_23dof", "_29dof"
ROBOT_SCENE = "../unitree_robots/" + ROBOT + "/scene" + DOF+ ".xml" # Robot scene
# DDS domain id, it is recommended to distinguish from the real robot (default is 0 on the real robot)
DOMAIN_ID = 1 # Domain id
# Network interface name, for simulation, it is recommended to use the local loopback "lo"
INTERFACE = "lo" # Interface 

USE_JOYSTICK = 1 # Simulate Unitree WirelessController using a gamepad
JOYSTICK_TYPE = "xbox" #"ros2_hands"# ,"xbox" support and "switch" gamepad layout
JOYSTICK_DEVICE = 0 # Joystick number

PRINT_SCENE_INFORMATION = True # Print link, joint and sensors information of robot
ENABLE_ELASTIC_BAND = True # False # Virtual spring band, used for lifting h1

SIMULATE_DT = 0.005  # Need to be larger than the runtime of viewer.sync()
VIEWER_DT = 0.02  # 50 fps for viewer

HEADLESS = False # True
