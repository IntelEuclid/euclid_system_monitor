cmake_minimum_required(VERSION 2.8.3)
project(system_monitor)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   WifiStatus.msg
   HardwareStatus.msg
   USBStatus.msg
   CpuStatus.msg
 )


# Install python scripts using distutils
catkin_python_setup()

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )


catkin_package(
 CATKIN_DEPENDS message_runtime
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

# Load catkin and all dependencies required for this package
set(CATKIN_DEPS std_msgs rospy)

# Install launch files
install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

catkin_package(
    DEPENDS ${SYS_DEPS}
    CATKIN_DEPENDS ${CATKIN_DEPS}
)

catkin_install_python(PROGRAMS scripts/CpuDeviceInfo.py scripts/device_monitor.py scripts/nodes_monitor.py
                      DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
                      


