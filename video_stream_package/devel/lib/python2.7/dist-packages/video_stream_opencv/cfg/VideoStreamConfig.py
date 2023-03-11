## *********************************************************
##
## File autogenerated for the video_stream_opencv package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'Camera name', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'camera_name', 'edit_method': '', 'default': 'camera', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Image Publish Rate', 'max': 1000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'set_camera_fps', 'edit_method': '', 'default': 30.0, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Buffer size for capturing frames', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'buffer_queue_size', 'edit_method': '', 'default': 100, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Image Publish Rate', 'max': 1000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'fps', 'edit_method': '', 'default': 240.0, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Camera FrameID', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'frame_id', 'edit_method': '', 'default': 'camera', 'level': 1, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Camera info URL', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'camera_info_url', 'edit_method': '', 'default': '', 'level': 1, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Flip image horizontally', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flip_horizontal', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Flip image vertically', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flip_vertical', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Target width', 'max': 10000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'width', 'edit_method': '', 'default': 0, 'level': 1, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Target height', 'max': 10000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'height', 'edit_method': '', 'default': 0, 'level': 1, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Target brightness', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'brightness', 'edit_method': '', 'default': 0.5019607843137255, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Target contrast', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'contrast', 'edit_method': '', 'default': 0.12549019607843137, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Target hue', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'hue', 'edit_method': '', 'default': 0.5, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Target saturation', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'saturation', 'edit_method': '', 'default': 0.64, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Target auto exposure', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'auto_exposure', 'edit_method': '', 'default': True, 'level': 1, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Target exposure', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'exposure', 'edit_method': '', 'default': 0.5, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Loop videofile', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'loop_videofile', 'edit_method': '', 'default': False, 'level': 1, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Re-open camera device on read failure', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'reopen_on_read_failure', 'edit_method': '', 'default': False, 'level': 1, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Output encoding', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'output_encoding', 'edit_method': '', 'default': 'bgr8', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Start frame of the video ', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'start_frame', 'edit_method': '', 'default': 0, 'level': 1, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Stop frame of the video', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'stop_frame', 'edit_method': '', 'default': -1, 'level': 1, 'min': -1, 'type': 'int'}, {'srcline': 291, 'description': 'Removes suspicious calls from OpenCV VideoCapture object', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'remove_suspicious_calls', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

