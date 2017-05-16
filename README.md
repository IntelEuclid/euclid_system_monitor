# Intel&reg; Euclid&trade; System monitor node.

This system monitor node is reponsible for providing Intel&reg; Euclid&trade; system utilization and information such as CPU, WiFi, Thermal, and memory consumption.

[Intel® Euclid™ Community Site](http://www.euclidcommunity.intel.com).

[Intel® Euclid™ Support Forum](http://www.intel.com/content/www/us/en/support/emerging-technologies/intel-euclid-development-kit.html).

## Subscribed Topics
	None

## Published Topics

    wifi_status 
        publishes a ROS topic with wifi details for IP, Mac address, and connected ssid.
    
    hardware_status
        publishes a ROS topic with details for machine name, battery charging percentage, battery charging state.

    usb_status
        publishes a ROS topic with details for connected 'ttyUSB' devices.
        
    cpu_info
        publishes a ROS topic with details for sampled utilizations such as:
		CPU model name, Utilization per core, Frequency per core, Temperature, Memory usage percentage.

## Services
   None
    
## Contributing to the Project

The Intel&reg; Euclid&trade; System monitor node is developed and distributed under
a BSD-3 license as noted in [License.txt](licenses/License.txt).

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
have the right to submit it under the open source license
indicated in the file; or

(b) The contribution is based upon previous work that, to the best
of my knowledge, is covered under an appropriate open source
license and I have the right under that license to submit that
work with modifications, whether created in whole or in part
by me, under the same open source license (unless I am
permitted to submit under a different license), as indicated
in the file; or

(c) The contribution was provided directly to me by some other
person who certified (a), (b) or (c) and I have not modified
it.

(d) I understand and agree that this project and the contribution
are public and that a record of the contribution (including all
personal information I submit with it, including my sign-off) is
maintained indefinitely and may be redistributed consistent with
this project or the open source license(s) involved.

## Configuration:

| Version        | Best Known           |
|:-------------- |:---------------------|
| OS             | Ubuntu 16.04 LTS     |
| ROS            | Kinetic              |
