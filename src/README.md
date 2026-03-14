# Source Code — 12-DOF Quadruped Robot

ROS2 packages and Arduino libraries for robot control, kinematics, 
gait generation, and camera streaming.

---

## Structure

src/
├── spider_control/       # ROS2 locomotion control package
├── spider_cam/           # ROS2 camera streaming package
└── arduino_libraries/    # Custom Arduino libraries
    ├── SpiderKinematics/
    ├── GaitGenerator/
    └── ServoController/

---

## ROS2 Packages

### spider_control

| Node | Subscribes | Publishes |
|------|-----------|-----------|
| servo_bridge | /spider/joint_commands | /spider/joint_states |
| gait_controller | /spider/cmd_vel, /spider/gait_select | /spider/foot_targets |
| kinematics_node | /spider/foot_targets | /spider/joint_commands |

Key parameters:
- servo_bridge: serial_port, baud_rate, control_frequency (50Hz)
- gait_controller: gait_type, step_height (30mm), stride_length (50mm)
- kinematics_node: coxa_length (30), femur_length (60), tibia_length (80)

### spider_cam

| Node | Publishes |
|------|-----------|
| cam_relay | /spider/camera, /spider/camera_info |

Parameters: camera_url (http://192.168.4.1:81/stream), frame_rate (10fps)

---

## Building ROS2 Packages
```bash
# Install ROS2 Humble
sudo apt install ros-humble-desktop

# Build workspace
cd ~/spider_ws
colcon build

# Source workspace
source install/setup.bash

# Run individual nodes
ros2 run spider_control servo_bridge
ros2 run spider_control gait_controller
ros2 run spider_control kinematics_node
ros2 run spider_cam cam_relay
```

---

## Arduino Libraries

### SpiderKinematics
```cpp
#include <SpiderKinematics.h>
SpiderKinematics ik(30, 60, 80);  // coxa, femur, tibia lengths

Vector3 target = {100, 0, -80};
LegAngles angles;
if (ik.solve(target, angles)) {
    // use angles.hip, angles.thigh, angles.knee
}
```

### GaitGenerator
```cpp
#include <GaitGenerator.h>
GaitGenerator gait;
gait.setGait(GAIT_WALK);
gait.setSpeed(1.0);
gait.update();
Vector3 footPos = gait.getFootPosition(legIndex);
```

### ServoController
```cpp
#include <ServoController.h>
ServoController servos;
servos.begin();
servos.setFrequency(50);
servos.setAngle(0, 90);
servos.update();
```

### Installing Libraries
```bash
cp -r src/arduino_libraries/SpiderKinematics ~/Arduino/libraries/
cp -r src/arduino_libraries/GaitGenerator ~/Arduino/libraries/
cp -r src/arduino_libraries/ServoController ~/Arduino/libraries/
```

---

## Testing
```bash
# Run unit tests
colcon test --packages-select spider_control
colcon test-result --all

# Check topics
ros2 topic list
ros2 topic echo /spider/joint_states
```

---

## Troubleshooting

Build errors:
```bash
rm -rf build install log
colcon build --symlink-install
rosdep install --from-paths src --ignore-src -r -y
```

Import errors:
```bash
source install/setup.bash
ros2 pkg list | grep spider
```

Serial permission:
```bash
sudo usermod -aG dialout $USER
```

---

## Notes

- Source workspace before running any ROS2 commands
- Arduino libraries must be in ~/Arduino/libraries/
- Test individual nodes before full system launch
- Always test with robot suspended before floor operation
