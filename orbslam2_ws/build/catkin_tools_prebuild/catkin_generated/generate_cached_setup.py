# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/aiudabot/AIUDA_PACKAGES/opencv_ros_package/devel;/home/aiudabot/AIUDA_PACKAGES/ros_workspace/devel;/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/devel;/home/aiudabot/AIUDA_PACKAGES/AIUDA_STARTER/devel;/home/aiudabot/AIUDA_PACKAGES/husky_ros_package/devel;/home/aiudabot/AIUDA_PACKAGES/hector_slam_package/devel;/home/aiudabot/AIUDA_PACKAGES/video_stream_package/devel;/home/aiudabot/AIUDA_PACKAGES/pose_estimate_ws/devel;/home/aiudabot/AIUDA_PACKAGES/mpu_ws/devel;/home/aiudabot/AIUDA_PACKAGES/postal_goal_ws/devel;/home/aiudabot/AIUDA_PACKAGES/teleop_catkin_ws/devel;/home/aiudabot/tf_catkin_ws/devel;/home/aiudabot/turtlebot_ws/devel;/home/aiudabot/orb_catkin_ws/devel;/opt/ros/melodic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/aiudabot/AIUDA_PACKAGES/orbslam2_ws/devel/.private/catkin_tools_prebuild/env.sh')

output_filename = '/home/aiudabot/AIUDA_PACKAGES/orbslam2_ws/build/catkin_tools_prebuild/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
