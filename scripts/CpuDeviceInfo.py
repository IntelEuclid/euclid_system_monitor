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

import subprocess
import psutil

def GetCpuModelName():
    cpu_model = subprocess.Popen(['cat /proc/cpuinfo | grep "model name" | uniq | cut -d: -f2'],
                             stdout=subprocess.PIPE, shell=True)
    (CPU_MODEL, errors) = cpu_model.communicate()
    cpu_model.stdout.close()
    return CPU_MODEL

def GetCPU_UtilizationPerCore():
    '''
    Get CPU utilization per core.
    :return: Collection of CPU utilization per core.
    '''
    coresUtilization = []
    cpu_perc = psutil.cpu_percent(interval=0.5, percpu=True)
    for i in range(len(cpu_perc)):
        coresUtilization.append(float(cpu_perc[i]))
    return coresUtilization

def GetCPUFrequencyPerCore():
    cpuFreq = subprocess.Popen(["cat /proc/cpuinfo | grep MHz | awk '{print $4}' | head -n4"],stdout=subprocess.PIPE,shell=True)
    (cpu,errors) = cpuFreq.communicate()
    return filter(None, cpu.split("\n"))

def GetMemoryUsagePercentage():
    '''
    Get Memory usage percentage
    :return: memory usage percentage e.g 20.2
    '''
    memoryusagePercent = psutil.virtual_memory().percent
    return memoryusagePercent

def GetCPUTemperature():
    '''
    Read CPU Temperature in C' from '/sys/class/thermal/thermal_zone6/temp'
    :return: CPU Temperature read. '-1' on read error.
    '''
    try:
        #temperature = open("/sys/class/thermal/thermal_zone6/temp").read().strip().lstrip('temperature :').rstrip(' C')
        #temperature = float(temperature) / 1000
        temp = subprocess.Popen(["cat /sys/devices/platform/coretemp.0/hwmon/hwmon3/temp*_input | awk '{ sum +=$1 } END { print sum/4 }'"], stdout=subprocess.PIPE,shell=True)
        (temperature,errors) = temp.communicate()
        return int(temperature.split("\n")[0])/1000;
    except:
        return -1 #TODO Print and handle error

if __name__ == '__main__':
    print (GetMemoryUsagePercentage())
    print (GetCpuModelName())
    print (GetCPU_UtilizationPerCore())
    print (GetCPUFrequencyPerCore())
    print (GetCPUTemperature())
