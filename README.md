# aiuda-robot
Official repository for Aiuda Robot Project

## Remote Access
Follow this tutorial https://medium.com/@bharathsudharsan023/jetson-nano-remote-vnc-access-d1e71c82492b.
Note: This uses Remmina so this is only applicable from linux to linux remote access

## Running AIUDA Software
### Video Process
roslaunch deployment_video.launch
Note: For debugging change <arg name="input" default="csi://0"/> into <arg name="input" default="file:///home/aiudabot/AIUDA_PACKAGES/barangay_video.mp4"/>
Note: run rviz and add display image then change topic to video/source/raw
