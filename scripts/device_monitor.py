#!/usr/bin/env python

##################################################################################
#Copyright (c) 2016, Intel Corporation
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice,
#this list of conditions and the following disclaimer in the documentation
#and/or other materials provided with the distribution.
#
#3. Neither the name of the copyright holder nor the names of its contributors
#may be used to endorse or promote products derived from this software without
#specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
##################################################################################

import rospy
from system_monitor.msg import *
import CpuDeviceInfo
import platform
import glob
from EuclidNetworkHAL import EuclidNetworkHAL

searchPattern = "ttyUSB*"
    
def getBatteryLevel():
    try:
      battery_status_file = "/sys/class/power_supply/max170xx_battery/capacity"
      with open(battery_status_file) as state:
        state.seek(0)
        for line in state:
		    return int(line)
    except:
        return -1  # TODO Print and handle error

def getBatteryStatus():
  try:
    battery_status_file = "/sys/class/power_supply/max170xx_battery/status"
    with open(battery_status_file) as state:
      state.seek(0)
      for line in state:
        return line
  except:
    return -1  # TODO Print and handle error

def publishStatus():   
    rate = rospy.Rate(0.5)
    wifipub = rospy.Publisher('wifi_status',WifiStatus,queue_size=1)
    hardwarepub = rospy.Publisher('hardware_status',HardwareStatus,queue_size=1)
    usbpub = rospy.Publisher('usb_status',USBStatus,queue_size=1)
    cpuInfoPub = rospy.Publisher('cpu_info',CpuStatus,queue_size=1)

 
  #######################################
  # initializing static variables       #
  #######################################
  # WIFI:
    networkHAL = EuclidNetworkHAL()
    mac_address = networkHAL.GetMacAddress()
    ip_address = networkHAL.GetCurrentIP()
    ssid = networkHAL.GetCurrentConnectionName() 

    # HARDWARE:
    cs_name = platform.node()
   
    while not rospy.is_shutdown():

      # Network publisher
      if (wifipub.get_num_connections() > 0 ):
            wifipub.publish(WifiStatus(ssid,ip_address,mac_address))

      # Hardware publisher
      if (hardwarepub.get_num_connections() > 0):
            battery = getBatteryLevel()
            batteryStatus = getBatteryStatus()

            if battery <0 or battery > 100:
                  battery = 0
                  batteryStatus = 'unknown'           

            hardwarepub.publish(HardwareStatus(cs_name, battery, batteryStatus))
      
      # Usb publisher
      if (usbpub.get_num_connections() > 0):
            usb_list = glob.glob('/dev/' + searchPattern)
            usbpub.publish(USBStatus(usb_list))

      #Cpu Info
      if(cpuInfoPub.get_num_connections() > 0):
          cpuModelName = CpuDeviceInfo.GetCpuModelName()
          cpuUtilizations = CpuDeviceInfo.GetCPU_UtilizationPerCore()
          cpuFreqs = CpuDeviceInfo.GetCPUFrequencyPerCore()
          cpuTemperature = CpuDeviceInfo.GetCPUTemperature()
          memoryPercent = CpuDeviceInfo.GetMemoryUsagePercentage()
          cpuInfoPub.publish(CpuStatus(cpuModelName,cpuUtilizations,cpuFreqs,cpuTemperature,memoryPercent))

      rate.sleep() 
        
if __name__ == '__main__':
  try:
    rospy.init_node('CsDeviceMonitor')
    publishStatus()

  except rospy.ROSInterruptException:
    pass
  
