python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Camera relay (replace with your package/executable)
        Node(
            package="spider_cam",
            executable="cam_relay",
            name="cam_relay",
            output="screen",
            parameters=[{"camera_topic": "/spider/camera"}],
        ),
        # Teleop bridge to Arduino/PCA9685 (replace with your pkg)
        Node(
            package="spider_control",
            executable="servo_bridge",
            name="servo_bridge",
            output="screen",
            parameters=[{"i2c_addr": "0x40"}],
        ),
    ])
