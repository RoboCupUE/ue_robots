import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    ld = LaunchDescription()

    tb3_gazebo_pkg = get_package_share_directory('turtlebot3_gazebo')

    os.environ['TURTLEBOT3_MODEL'] = 'burger'

    tb3_world_launch_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(tb3_gazebo_pkg,
                                        'launch', 'turtlebot3_world.launch.py'))
    )

    ld.add_action(tb3_world_launch_cmd)

    return ld