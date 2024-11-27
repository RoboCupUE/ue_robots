import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    ld = LaunchDescription()

    world = LaunchConfiguration('world')
    model = LaunchConfiguration('model')
    namespace = LaunchConfiguration('namespace')
    use_sim_time = LaunchConfiguration('use_sim_time')

    world_arg = DeclareLaunchArgument('world', default_value='warehouse',
                                    description='Ignition World')

    model_arg = DeclareLaunchArgument('model', default_value='standard',
                                    choices=['standard', 'lite'],
                                    description='Turtlebot4 Model')

    namespace_arg = DeclareLaunchArgument('namespace', default_value='',
                          description='Robot namespace')
    
    use_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='true',
                          choices=['true', 'false'],
                          description='use_sim_time')

    tb4_ign_pkg = get_package_share_directory('turtlebot4_ignition_bringup')
    pkg_dr = get_package_share_directory('tb4_bringup')

    ignition_launch_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(tb4_ign_pkg,
                                        'launch', 'ignition.launch.py')),
                                        launch_arguments={
                                            'world': world,
                                            'model': model
                                        }.items()
    )

    tb4_spawn_launch_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_dr,
                                        'launch', 'tb4_spawn-launch.py')),
                                        launch_arguments={
                                            'namespace': namespace,
                                            'model': model,
                                            'use_sim_time': use_sim_time
                                        }.items()
    )

    ld.add_action(world_arg)
    ld.add_action(model_arg)
    ld.add_action(namespace_arg)
    ld.add_action(use_sim_time_arg)

    ld.add_action(ignition_launch_cmd)
    ld.add_action(tb4_spawn_launch_cmd)

    return ld