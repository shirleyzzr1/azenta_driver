from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
        
        Node(
            package='sp_module_client',
            namespace='sp_module',
            executable='peelerNode',
            name='peelerNode'

        ),

        Node(
            package='sp_module_client',
            namespace='sp_module',
            executable='sealerNode',
            name='sealerNode'
        ),

#        Node(
#            package='sp_module_client',
#            namespace='sp_module',
#            executable='cameraNode',
#            name='cameraNode'
#        ),

    ])
