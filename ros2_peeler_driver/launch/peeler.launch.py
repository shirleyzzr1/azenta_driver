from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='ros2_peeler_driver',
            namespace='peeler',
            executable='peelerNode',
            name='peelerNode'
        ),

        Node(
            package='ros2_peeler_driver',
            namespace='master',
            executable='masterNode',
            name='masterNode'
        ),

        Node(
            package='ros2_peeler_driver',
            namespace='camera',
            executable='cameraNode',
            name='cameraNode'
        ),

    ])