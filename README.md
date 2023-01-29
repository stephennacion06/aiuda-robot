# aiuda-robot
Official repository for Aiuda Robot Project

## Installation
1. Install ROS2 - melodic from http://wiki.ros.org/melodic/Installation/Ubuntu
2. Install packages in ROS
<details>
<summary>Ros Package List Breakdown</summary>
<br>ORB_SLAM2 /opt/ros/melodic/share/ORB_SLAM2
<br>actionlib /opt/ros/melodic/share/actionlib
<br>actionlib_msgs /opt/ros/melodic/share/actionlib_msgs
<br>actionlib_tutorials /opt/ros/melodic/share/actionlib_tutorials
<br>aiuda_body_serial /home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial
<br>aiuda_throttle_package /home/aiudabot/AIUDA_PACKAGES/opencv_ros_package/src/aiuda_throttle_package
<br>aiudastarter /home/aiudabot/AIUDA_PACKAGES/AIUDA_STARTER/src/aiudastarter
<br>amcl /opt/ros/melodic/share/amcl
<br>angles /opt/ros/melodic/share/angles
<br>async_web_server_cpp /opt/ros/melodic/share/async_web_server_cpp
<br>base_local_planner /opt/ros/melodic/share/base_local_planner
<br>bond /opt/ros/melodic/share/bond
<br>bondcpp /opt/ros/melodic/share/bondcpp
<br>bondpy /opt/ros/melodic/share/bondpy
<br>camera_calibration /opt/ros/melodic/share/camera_calibration
<br>camera_calibration_parsers /opt/ros/melodic/share/camera_calibration_parsers
<br>camera_info_manager /opt/ros/melodic/share/camera_info_manager
<br>carrot_planner /opt/ros/melodic/share/carrot_planner
<br>catkin /opt/ros/melodic/share/catkin
<br>class_loader /opt/ros/melodic/share/class_loader
<br>clear_costmap_recovery /opt/ros/melodic/share/clear_costmap_recovery
<br>clock_relay /opt/ros/melodic/share/clock_relay
<br>cmake_modules /opt/ros/melodic/share/cmake_modules
<br>compressed_depth_image_transport /opt/ros/melodic/share/compressed_depth_image_transport
<br>compressed_image_transport /opt/ros/melodic/share/compressed_image_transport
<br>control_msgs /opt/ros/melodic/share/control_msgs
<br>control_toolbox /opt/ros/melodic/share/control_toolbox
<br>controller_interface /opt/ros/melodic/share/controller_interface
<br>controller_manager /opt/ros/melodic/share/controller_manager
<br>controller_manager_msgs /opt/ros/melodic/share/controller_manager_msgs
<br>costmap_2d /opt/ros/melodic/share/costmap_2d
<br>cpp_common /opt/ros/melodic/share/cpp_common
<br>cv_bridge /opt/ros/melodic/share/cv_bridge
<br>depth_image_proc /opt/ros/melodic/share/depth_image_proc
<br>diagnostic_aggregator /opt/ros/melodic/share/diagnostic_aggregator
<br>diagnostic_analysis /opt/ros/melodic/share/diagnostic_analysis
<br>diagnostic_common_diagnostics /opt/ros/melodic/share/diagnostic_common_diagnostics
<br>diagnostic_msgs /opt/ros/melodic/share/diagnostic_msgs
<br>diagnostic_updater /opt/ros/melodic/share/diagnostic_updater
<br>diff_drive_controller /opt/ros/melodic/share/diff_drive_controller
<br>dwa_local_planner /opt/ros/melodic/share/dwa_local_planner
<br>dynamic_reconfigure /opt/ros/melodic/share/dynamic_reconfigure
<br>eigen_conversions /opt/ros/melodic/share/eigen_conversions
<br>fake_localization /opt/ros/melodic/share/fake_localization
<br>filters /opt/ros/melodic/share/filters
<br>forward_command_controller /opt/ros/melodic/share/forward_command_controller
<br>gazebo_dev /opt/ros/melodic/share/gazebo_dev
<br>gazebo_msgs /opt/ros/melodic/share/gazebo_msgs
<br>gazebo_plugins /opt/ros/melodic/share/gazebo_plugins
<br>gazebo_ros /opt/ros/melodic/share/gazebo_ros
<br>gazebo_ros_control /opt/ros/melodic/share/gazebo_ros_control
<br>gencpp /opt/ros/melodic/share/gencpp
<br>geneus /opt/ros/melodic/share/geneus
<br>genlisp /opt/ros/melodic/share/genlisp
<br>genmsg /opt/ros/melodic/share/genmsg
<br>gennodejs /opt/ros/melodic/share/gennodejs
<br>genpy /opt/ros/melodic/share/genpy
<br>geographic_msgs /opt/ros/melodic/share/geographic_msgs
<br>geometry_msgs /opt/ros/melodic/share/geometry_msgs
<br>gl_dependency /opt/ros/melodic/share/gl_dependency
<br>global_planner /opt/ros/melodic/share/global_planner
<br>gmapping /opt/ros/melodic/share/gmapping
<br>hardware_interface /opt/ros/melodic/share/hardware_interface
<br>hector_compressed_map_transport /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_compressed_map_transport
<br>hector_geotiff /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_geotiff
<br>hector_geotiff_launch /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_geotiff_launch
<br>hector_geotiff_plugins /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_geotiff_plugins
<br>hector_imu_attitude_to_tf /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_imu_attitude_to_tf
<br>hector_imu_tools /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_imu_tools
<br>hector_map_server /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_map_server
<br>hector_map_tools /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_map_tools
<br>hector_mapping /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_mapping
<br>hector_marker_drawing /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_marker_drawing
<br>hector_nav_msgs /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_nav_msgs
<br>hector_slam_launch /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_slam_launch
<br>hector_trajectory_server /home/aiudabot/AIUDA_PACKAGES/hector_slam_package/src/hector_slam/hector_trajectory_server
<br>husky_base /home/aiudabot/AIUDA_PACKAGES/husky_ros_package/src/husky/husky_base
<br>husky_bringup /home/aiudabot/AIUDA_PACKAGES/husky_ros_package/src/husky/husky_bringup
<br>husky_control /home/aiudabot/AIUDA_PACKAGES/husky_ros_package/src/husky/husky_control
<br>husky_description /home/aiudabot/AIUDA_PACKAGES/husky_ros_package/src/husky/husky_description
<br>husky_gazebo /home/aiudabot/AIUDA_PACKAGES/husky_ros_package/src/husky/husky_gazebo
<br>husky_msgs /home/aiudabot/AIUDA_PACKAGES/husky_ros_package/src/husky/husky_msgs
<br>husky_navigation /home/aiudabot/AIUDA_PACKAGES/husky_ros_package/src/husky/husky_navigation
<br>husky_viz /home/aiudabot/AIUDA_PACKAGES/husky_ros_package/src/husky/husky_viz
<br>image_geometry /opt/ros/melodic/share/image_geometry
<br>image_proc /opt/ros/melodic/share/image_proc
<br>image_publisher /opt/ros/melodic/share/image_publisher
<br>image_rotate /opt/ros/melodic/share/image_rotate
<br>image_transport /opt/ros/melodic/share/image_transport
<br>image_view /opt/ros/melodic/share/image_view
<br>imu_complementary_filter /opt/ros/melodic/share/imu_complementary_filter
<br>interactive_marker_tutorials /opt/ros/melodic/share/interactive_marker_tutorials
<br>interactive_marker_twist_server /opt/ros/melodic/share/interactive_marker_twist_server
<br>interactive_markers /opt/ros/melodic/share/interactive_markers
<br>joint_limits_interface /opt/ros/melodic/share/joint_limits_interface
<br>joint_state_controller /opt/ros/melodic/share/joint_state_controller
<br>joint_state_publisher /opt/ros/melodic/share/joint_state_publisher
<br>joint_state_publisher_gui /opt/ros/melodic/share/joint_state_publisher_gui
<br>joint_trajectory_controller /opt/ros/melodic/share/joint_trajectory_controller
<br>joy /opt/ros/melodic/share/joy
<br>kdl_conversions /opt/ros/melodic/share/kdl_conversions
<br>kdl_parser /opt/ros/melodic/share/kdl_parser
<br>kdl_parser_py /opt/ros/melodic/share/kdl_parser_py
<br>laser_assembler /opt/ros/melodic/share/laser_assembler
<br>laser_filters /opt/ros/melodic/share/laser_filters
<br>laser_geometry /opt/ros/melodic/share/laser_geometry
<br>librviz_tutorial /opt/ros/melodic/share/librviz_tutorial
<br>lms1xx /opt/ros/melodic/share/lms1xx
<br>map_msgs /opt/ros/melodic/share/map_msgs
<br>map_server /opt/ros/melodic/share/map_server
<br>master_discovery_fkie /opt/ros/melodic/share/master_discovery_fkie
<br>master_sync_fkie /opt/ros/melodic/share/master_sync_fkie
<br>media_export /opt/ros/melodic/share/media_export
<br>message_filters /opt/ros/melodic/share/message_filters
<br>message_generation /opt/ros/melodic/share/message_generation
<br>message_relay /opt/ros/melodic/share/message_relay
<br>message_runtime /opt/ros/melodic/share/message_runtime
<br>mk /opt/ros/melodic/share/mk
<br>move_base /opt/ros/melodic/share/move_base
<br>move_base_msgs /opt/ros/melodic/share/move_base_msgs
<br>move_slow_and_clear /opt/ros/melodic/share/move_slow_and_clear
<br>mpu_6050_driver /home/aiudabot/AIUDA_PACKAGES/mpu_ws/src/mpu_6050_driver
<br>multimaster_launch /opt/ros/melodic/share/multimaster_launch
<br>multimaster_msgs /opt/ros/melodic/share/multimaster_msgs
<br>multimaster_msgs_fkie /opt/ros/melodic/share/multimaster_msgs_fkie
<br>nav_core /opt/ros/melodic/share/nav_core
<br>nav_msgs /opt/ros/melodic/share/nav_msgs
<br>navfn /opt/ros/melodic/share/navfn
<br>nodelet /opt/ros/melodic/share/nodelet
<br>nodelet_topic_tools /opt/ros/melodic/share/nodelet_topic_tools
<br>nodelet_tutorial_math /opt/ros/melodic/share/nodelet_tutorial_math
<br>openslam_gmapping /opt/ros/melodic/share/openslam_gmapping
<br>orb_slam2_ros /home/aiudabot/orb_catkin_ws/src/orb_slam_2_ros
<br>orocos_kdl /opt/ros/melodic/share/orocos_kdl
<br>pcl_conversions /opt/ros/melodic/share/pcl_conversions
<br>pcl_msgs /opt/ros/melodic/share/pcl_msgs
<br>pcl_ros /opt/ros/melodic/share/pcl_ros
<br>pluginlib /opt/ros/melodic/share/pluginlib
<br>pluginlib_tutorials /opt/ros/melodic/share/pluginlib_tutorials
<br>pointcloud_to_laserscan /opt/ros/melodic/share/pointcloud_to_laserscan
<br>polled_camera /opt/ros/melodic/share/polled_camera
<br>position_controllers /opt/ros/melodic/share/position_controllers
<br>postal_goal_ros /home/aiudabot/AIUDA_PACKAGES/postal_goal_ws/src/postal_goal_ros
<br>python_orocos_kdl /opt/ros/melodic/share/python_orocos_kdl
<br>python_qt_binding /opt/ros/melodic/share/python_qt_binding
<br>qt_dotgraph /opt/ros/melodic/share/qt_dotgraph
<br>qt_gui /opt/ros/melodic/share/qt_gui
<br>qt_gui_cpp /opt/ros/melodic/share/qt_gui_cpp
<br>qt_gui_py_common /opt/ros/melodic/share/qt_gui_py_common
<br>qwt_dependency /opt/ros/melodic/share/qwt_dependency
<br>realsense2_description /opt/ros/melodic/share/realsense2_description
<br>realtime_tools /opt/ros/melodic/share/realtime_tools
<br>resource_retriever /opt/ros/melodic/share/resource_retriever
<br>robot_localization /opt/ros/melodic/share/robot_localization
<br>robot_setup_tf /home/aiudabot/tf_catkin_ws/src/robot_setup_tf
<br>robot_state_publisher /opt/ros/melodic/share/robot_state_publisher
<br>ros_deep_learning /home/aiudabot/AIUDA_PACKAGES/ros_workspace/src/ros_deep_learning
<br>ros_environment /opt/ros/melodic/share/ros_environment
<br>rosbag /opt/ros/melodic/share/rosbag
<br>rosbag_migration_rule /opt/ros/melodic/share/rosbag_migration_rule
<br>rosbag_storage /opt/ros/melodic/share/rosbag_storage
<br>rosbash /opt/ros/melodic/share/rosbash
<br>rosboost_cfg /opt/ros/melodic/share/rosboost_cfg
<br>rosbuild /opt/ros/melodic/share/rosbuild
<br>rosclean /opt/ros/melodic/share/rosclean
<br>rosconsole /opt/ros/melodic/share/rosconsole
<br>rosconsole_bridge /opt/ros/melodic/share/rosconsole_bridge
<br>roscpp /opt/ros/melodic/share/roscpp
<br>roscpp_serialization /opt/ros/melodic/share/roscpp_serialization
<br>roscpp_traits /opt/ros/melodic/share/roscpp_traits
<br>roscpp_tutorials /opt/ros/melodic/share/roscpp_tutorials
<br>roscreate /opt/ros/melodic/share/roscreate
<br>rosgraph /opt/ros/melodic/share/rosgraph
<br>rosgraph_msgs /opt/ros/melodic/share/rosgraph_msgs
<br>roslang /opt/ros/melodic/share/roslang
<br>roslaunch /opt/ros/melodic/share/roslaunch
<br>roslib /opt/ros/melodic/share/roslib
<br>roslint /opt/ros/melodic/share/roslint
<br>roslisp /opt/ros/melodic/share/roslisp
<br>roslz4 /opt/ros/melodic/share/roslz4
<br>rosmake /opt/ros/melodic/share/rosmake
<br>rosmaster /opt/ros/melodic/share/rosmaster
<br>rosmsg /opt/ros/melodic/share/rosmsg
<br>rosnode /opt/ros/melodic/share/rosnode
<br>rosout /opt/ros/melodic/share/rosout
<br>rospack /opt/ros/melodic/share/rospack
<br>rosparam /opt/ros/melodic/share/rosparam
<br>rospy /opt/ros/melodic/share/rospy
<br>rospy_tutorials /opt/ros/melodic/share/rospy_tutorials
<br>rosservice /opt/ros/melodic/share/rosservice
<br>rostest /opt/ros/melodic/share/rostest
<br>rostime /opt/ros/melodic/share/rostime
<br>rostopic /opt/ros/melodic/share/rostopic
<br>rosunit /opt/ros/melodic/share/rosunit
<br>roswtf /opt/ros/melodic/share/roswtf
<br>rotate_recovery /opt/ros/melodic/share/rotate_recovery
<br>rqt_action /opt/ros/melodic/share/rqt_action
<br>rqt_bag /opt/ros/melodic/share/rqt_bag
<br>rqt_bag_plugins /opt/ros/melodic/share/rqt_bag_plugins
<br>rqt_console /opt/ros/melodic/share/rqt_console
<br>rqt_dep /opt/ros/melodic/share/rqt_dep
<br>rqt_graph /opt/ros/melodic/share/rqt_graph
<br>rqt_gui /opt/ros/melodic/share/rqt_gui
<br>rqt_gui_cpp /opt/ros/melodic/share/rqt_gui_cpp
<br>rqt_gui_py /opt/ros/melodic/share/rqt_gui_py
<br>rqt_image_view /opt/ros/melodic/share/rqt_image_view
<br>rqt_launch /opt/ros/melodic/share/rqt_launch
<br>rqt_logger_level /opt/ros/melodic/share/rqt_logger_level
<br>rqt_moveit /opt/ros/melodic/share/rqt_moveit
<br>rqt_msg /opt/ros/melodic/share/rqt_msg
<br>rqt_nav_view /opt/ros/melodic/share/rqt_nav_view
<br>rqt_plot /opt/ros/melodic/share/rqt_plot
<br>rqt_pose_view /opt/ros/melodic/share/rqt_pose_view
<br>rqt_publisher /opt/ros/melodic/share/rqt_publisher
<br>rqt_py_common /opt/ros/melodic/share/rqt_py_common
<br>rqt_py_console /opt/ros/melodic/share/rqt_py_console
<br>rqt_reconfigure /opt/ros/melodic/share/rqt_reconfigure
<br>rqt_robot_dashboard /opt/ros/melodic/share/rqt_robot_dashboard
<br>rqt_robot_monitor /opt/ros/melodic/share/rqt_robot_monitor
<br>rqt_robot_steering /opt/ros/melodic/share/rqt_robot_steering
<br>rqt_runtime_monitor /opt/ros/melodic/share/rqt_runtime_monitor
<br>rqt_rviz /opt/ros/melodic/share/rqt_rviz
<br>rqt_service_caller /opt/ros/melodic/share/rqt_service_caller
<br>rqt_shell /opt/ros/melodic/share/rqt_shell
<br>rqt_srv /opt/ros/melodic/share/rqt_srv
<br>rqt_tf_tree /opt/ros/melodic/share/rqt_tf_tree
<br>rqt_top /opt/ros/melodic/share/rqt_top
<br>rqt_topic /opt/ros/melodic/share/rqt_topic
<br>rqt_web /opt/ros/melodic/share/rqt_web
<br>rviz /opt/ros/melodic/share/rviz
<br>rviz_imu_plugin /opt/ros/melodic/share/rviz_imu_plugin
<br>rviz_plugin_tutorials /opt/ros/melodic/share/rviz_plugin_tutorials
<br>rviz_python_tutorial /opt/ros/melodic/share/rviz_python_tutorial
<br>self_test /opt/ros/melodic/share/self_test
<br>sensor_msgs /opt/ros/melodic/share/sensor_msgs
<br>set_point /home/aiudabot/AIUDA_PACKAGES/pose_estimate_ws/src/set_point
<br>shape_msgs /opt/ros/melodic/share/shape_msgs
<br>smach /opt/ros/melodic/share/smach
<br>smach_msgs /opt/ros/melodic/share/smach_msgs
<br>smach_ros /opt/ros/melodic/share/smach_ros
<br>smclib /opt/ros/melodic/share/smclib
<br>stage /opt/ros/melodic/share/stage
<br>stage_ros /opt/ros/melodic/share/stage_ros
<br>std_msgs /opt/ros/melodic/share/std_msgs
<br>std_srvs /opt/ros/melodic/share/std_srvs
<br>stereo_image_proc /opt/ros/melodic/share/stereo_image_proc
<br>stereo_msgs /opt/ros/melodic/share/stereo_msgs
<br>teleop_twist_joy /opt/ros/melodic/share/teleop_twist_joy
<br>teleop_twist_keyboard /home/aiudabot/AIUDA_PACKAGES/teleop_catkin_ws/src/teleop_twist_keyboard
<br>tf /opt/ros/melodic/share/tf
<br>tf2 /opt/ros/melodic/share/tf2
<br>tf2_eigen /opt/ros/melodic/share/tf2_eigen
<br>tf2_geometry_msgs /opt/ros/melodic/share/tf2_geometry_msgs
<br>tf2_kdl /opt/ros/melodic/share/tf2_kdl
<br>tf2_msgs /opt/ros/melodic/share/tf2_msgs
<br>tf2_py /opt/ros/melodic/share/tf2_py
<br>tf2_relay /opt/ros/melodic/share/tf2_relay
<br>tf2_ros /opt/ros/melodic/share/tf2_ros
<br>tf2_sensor_msgs /opt/ros/melodic/share/tf2_sensor_msgs
<br>tf_conversions /opt/ros/melodic/share/tf_conversions
<br>theora_image_transport /opt/ros/melodic/share/theora_image_transport
<br>topic_tools /opt/ros/melodic/share/topic_tools
<br>trajectory_msgs /opt/ros/melodic/share/trajectory_msgs
<br>transmission_interface /opt/ros/melodic/share/transmission_interface
<br>turtle_actionlib /opt/ros/melodic/share/turtle_actionlib
<br>turtle_tf /opt/ros/melodic/share/turtle_tf
<br>turtle_tf2 /opt/ros/melodic/share/turtle_tf2
<br>turtlebot3_bringup /home/aiudabot/turtlebot_ws/src/turtlebot3/turtlebot3_bringup
<br>turtlebot3_description /home/aiudabot/turtlebot_ws/src/turtlebot3/turtlebot3_description
<br>turtlebot3_example /home/aiudabot/turtlebot_ws/src/turtlebot3/turtlebot3_example
<br>turtlebot3_fake /home/aiudabot/turtlebot_ws/src/turtlebot3_simulations/turtlebot3_fake
<br>turtlebot3_gazebo /home/aiudabot/turtlebot_ws/src/turtlebot3_simulations/turtlebot3_gazebo
<br>turtlebot3_msgs /home/aiudabot/turtlebot_ws/src/turtlebot3_msgs
<br>turtlebot3_navigation /home/aiudabot/turtlebot_ws/src/turtlebot3/turtlebot3_navigation
<br>turtlebot3_slam /home/aiudabot/turtlebot_ws/src/turtlebot3/turtlebot3_slam
<br>turtlebot3_teleop /home/aiudabot/turtlebot_ws/src/turtlebot3/turtlebot3_teleop
<br>turtlesim /opt/ros/melodic/share/turtlesim
<br>twist_mux /opt/ros/melodic/share/twist_mux
<br>twist_mux_msgs /opt/ros/melodic/share/twist_mux_msgs
<br>urdf /opt/ros/melodic/share/urdf
<br>urdf_parser_plugin /opt/ros/melodic/share/urdf_parser_plugin
<br>urdf_sim_tutorial /opt/ros/melodic/share/urdf_sim_tutorial
<br>urdf_tutorial /opt/ros/melodic/share/urdf_tutorial
<br>urdfdom_py /opt/ros/melodic/share/urdfdom_py
<br>uuid_msgs /opt/ros/melodic/share/uuid_msgs
<br>velodyne_description /opt/ros/melodic/share/velodyne_description
<br>video_stream_opencv /home/aiudabot/AIUDA_PACKAGES/video_stream_package/src/video_stream_opencv
<br>vision_msgs /opt/ros/melodic/share/vision_msgs
<br>visualization_marker_tutorials /opt/ros/melodic/share/visualization_marker_tutorials
<br>visualization_msgs /opt/ros/melodic/share/visualization_msgs
<br>voxel_grid /opt/ros/melodic/share/voxel_grid
<br>web_video_server /opt/ros/melodic/share/web_video_server
<br>webkit_dependency /opt/ros/melodic/share/webkit_dependency
<br>xacro /opt/ros/melodic/share/xacro
<br>xmlrpcpp /opt/ros/melodic/share/xmlrpcpp
</details>
<br> 3. Install ORBSLAM2 from  https://github.com/raulmur/ORB_SLAM2
<br> 4. Install jetson-inference from https://github.com/dusty-nv/jetson-inference and guide from https://github.com/dusty-nv/jetson-inference/blob/master/docs/segnet-console-2.md
<br> 5. Install AIUDA python packages "pip3 install -r requirements_aiuda.txt"
<br> 6. Update deeploarning model to fcn-resnet18-cityscapes-1024x512 in AIUDA_PACKAGES/ros_workspace/src/ros_deep_learning/launch/segnet.ros1.launch
<br> 7. For AIUDA body copy all libraries found in Arduino_Library into  /home/aiudabot/Arduino/libraries and use PID_AIUDA_BODY.ino 


## Remote Access
Follow this tutorial https://medium.com/@bharathsudharsan023/jetson-nano-remote-vnc-access-d1e71c82492b.

Note: This uses Remmina so this is only applicable from linux to linux remote access

## Running AIUDA Software
### Running AIUDA-SOFTWARE App Server
```
roslaunch deployment_video.launch
```

### Video Input
```
roslaunch deployment_video.launch
```
Note: 
For debugging change `<arg name="input" default="csi://0"/> into <arg name="input" default="file:///home/aiudabot/AIUDA_PACKAGES/barangay_video.mp4"/>` then run rviz and add display image then change topic to video/source/raw

### Mapping Process - New Created File - Generation of .bin, .pgm and .yaml
Start Video launch - either camera or recorded video
```
roslaunch deployment_video.launch
```
Start Orb-Slam, Image Segmentation, Throttle Control, Video Web Server
```
roslaunch aiuda_mapping_orbslam_new_map.launch
```
<br>Note: Start Scanning the environment 3-5 laps and check in mobile phone if the environment is being scanned 
<br> If the result of ORB-SLAM has accurate localization, save generated binary file by running the command
```
rosservice list (to check if /orb_slam2_mono/save_map is available)
rosservice call /orb_slam2_mono/save_map -f /home/aiudabot/AIUDA_PACKAGES/smith_map.bin
```
<br> After orb-slam scanning, run Hector SLAM. Repeat scanning upto 3-5 laps.
```
roslaunch aiuda_mapping_orbslam_new_map.launch
```
Save the generated map 
```
rosrun map_server map_saver -f mymap
```
<br> The all generates file must be transfer to this location
```
/home/aiudabot/AIUDA_PACKAGES/smith_map.bin - for binary file
/home/aiudabot/orb_catkin_ws/mymap.yaml - for yaml file
/home/aiudabot/orb_catkin_ws/mymap.pgm - for generated map image
NOTE: AIUDA_PACKAGES folder is just a backup folder for all packages used in AIUDA project
```

### Mapping Process -  Improving saved ORB-SLAM Map
Start Video launch - either camera or recorded video
```
roslaunch deployment_video.launch
```
Start Orb-Slam, Image Segmentation, Throttle Control, Video Web Server
```
roslaunch aiuda_mapping_orbslam_load_map.launch
```
<br>Note: Start Scanning the environment 3-5 laps and check in mobile phone if the environment is being scanned 
<br> If the result of ORB-SLAM has accurate localization, save generated binary file by running the command
```
rosservice list (to check if /orb_slam2_mono/save_map is available)
rosservice call /orb_slam2_mono/save_map -f /home/aiudabot/AIUDA_PACKAGES/smith_map.bin
NOTE: change file name of smith_map.bin to iterate or not overwrite saved map
```
