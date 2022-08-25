# azenta_driver

## Authors and Maintainers
* Sanjiv Parthasarathy
* Rafael Vescovi
* Doga Ozgulbas
* Eric Codrea
<p>&nbsp;</p>

## Description
This repository is provides drivers and ROS2 clients that are able to send commands to the Brooks XPeel peeler and the A4S sealer. 

The package is composed of 3 folders:
* azenta_driver
  * Contains drivers for sending command to the sealer & peeler 
  * The peeler_driver.py file is responsible for sending commands for removing seals off of microplates
  * The sealer_driver.py file is responsible for sending commands for adding seals on to microplates
* sp_module_client
  * Contains ROS2 nodes that that interface with the drivers and receive service commands using the wei_service ROS service package
* docker
  * Contains Dockerfile that builds an image, runs a container, and executes a launchfile
<p>&nbsp;</p>

## User Setup Guide

1. ### Git Clone azenta_driver repository
	In terminal:
	
		git clone https://github.com/AD-SDL/azenta_driver.git

2. ### Launching azenta driver on personal device

   In terminal:

        cd <azenta_driver location>
        cd azenta_driver
        touch __init__.py
        cd ..
        python setup.py
	
## Azenta Driver Send Command Guide

### Sending commands to XPeel driver:
	* Connect XPeel Driver to device with a serial to usb cable
	* Find XPeel port ex: "/dev/ttyUSB0"

   	In Python:
    
		from azenta_driver.peeler_driver import BROOKS_PEELER_CLIENT
		peeler = BROOKS_PEELER_CLIENT(port)
		
	* Send commands (provided below)
	
### Sending commands to A4S driver:
	* Connect A4S Driver to device with a serial to usb cable
	* Find A4S port ex: "/dev/ttyUSB0"

   	In Python:
    
		from azenta_driver.sealer_driver import A4S_SEALER_CLIENT
		sealer = A4S_SEALER_CLIENT(port)
		
	* Send commands (provided below)
<p>&nbsp;</p>

## Azenta Driver Commands
### Commands for XPeel driver:

	   
1.     peeler.check_status()

Identifies up to 3 errors currently present.
<p>&nbsp;</p>

2.     peeler.check_version() 

Identifies the XPeel virmware version.
<p>&nbsp;</p>

3.     peeler.reset()

This command causes the spool to advance a few inches to fresh tape, and the elevator and conveyor axes to return to the home and ready for plate pick up position. A good use for the reset command is to ensure that fresh tape is presented after a long period of inactivity.
<p>&nbsp;</p>

4.     peeler.restart()

This command causes the XPeel to restart; the same as turning the power off and back on.
<p>&nbsp;</p>

5.     peeler.peel(Set Number, Time)

This command has a number of parameters that can be selected to achieve better performance on difficult or unusual seal types. For most seals the default and fastest settings will give good
performance. In an automated environment it may be advisable to be more conservative, or to provide
for a retry at slower settings when the XPeel detects that a seal is not removed.

Parameter sets 1-8 are fixed; parameter set 9 can be set and saved manually by the user.

| Set Number | Begin Peel Location | Speed  |
|------------|---------------------|--------|
| 1          | Default -2 mm       | fast   |
| 2          | Default -2 mm       | slow   |
| 3          | Default             | fast   |
| 4          | Default             | slow   |
| 5          | Default +2 mm       | fast   |
| 6          | Default +2 mm       | slow   |
| 7          | Default +4 mm       | fast   |
| 8          | Default +4 mm       | slow   |
| 9          | custom              | custom |


The second parameter, refers to adhere time in seconds.
<p>&nbsp;</p>

6.     peeler.seal_check()

The ‘sealcheck’ command causes the conveyor to place the plate under the reflective seal detection
sensor and the elevator to move down to the proper sensing elevation. The sensor status is then
recorded. The elevator and conveyor axes then return to the home and ready for plate pick up
position. Since this action only checks the plate at one location, a better indicator is the error code
that will be generated during a normal desealing operation where the plate is scanned over most of its
length. The ‘sealcheck’ command is useful, however, to verify that the sensor parameters are set
correctly to detect a particular seal type.
<p>&nbsp;</p>

7.     peeler.tape_remaining()

The XPeel calculates the amount of tape remaining on the supply spool by comparing the travel of the
conveyor to the rotation of both the supply and take-up spools. After a completed ‘XPeel’ operation, a
‘tapeleft’ command can be issued to verify the amount of tape left as well as the space remaining on
the take-up spool. These calculations are not perfectly accurate but they will provide sufficient
warning to avoid running out of tape unexpectedly.
<p>&nbsp;</p>

8.     peeler.plate_check(y or n?)

This command sets the plate check parameter to yes or no.
<p>&nbsp;</p>

9.     peeler.sensor_threshold()

This command reports the threshold value of the seal detected sensor.
<p>&nbsp;</p>

10.     peeler.sensor_threshold_higher(Threshold Value)

Setting the seal detected threshold value for the seal present if higher than threshold.

The Threshold Value refers to the 3 digit threshold value. This command sets the seal detected threshold so that during an XPeel, sensor readings higher than this value represents an un-removed seal and will
result in an error 04, “seal not removed”, message.
<p>&nbsp;</p>

11.     peeler.sensor_threshold_lower(Threshold Value)

Setting the seal detected threshold value for the seal present if lower than threshold.

Where Threshold Value refers to the 3 digit threshold value. This command sets the seal detected threshold so that during an XPeel, sensor readings lower than this value represents an un-removed seal and will
result in an error 04, “seal not removed”, message.
<p>&nbsp;</p>

12.     peeler.conveyor_out()

This command causes the conveyor to move out towards the user 7mm each time the command is called. When the conveyor reaches it’s fully extended home position no movement
occurs.
<p>&nbsp;</p>

13.     peeler.conveyor_in()

This command causes the conveyor to move in to the default ‘begin peel’ position.
<p>&nbsp;</p>

14.     peeler.elevator_down()

This command causes the elevator to move down until it is stopped by a plate or reaches its lower limit. The plate check option is disabled for this command.
<p>&nbsp;</p>

15.     peeler.elevator_up()

This command causes the elevator to move up approximately 1.5mm each time the
command is called until the elevator reaches it full up home position.
<p>&nbsp;</p>

16.     peeler.move_spool()

This command causes the spool to advance approximately 10mm of tape.

### Commands for A4S driver:

1.     sealer.reset()

This command makes the sealer device clear error status' and reset the gate.
<p>&nbsp;</p>

2.     sealer.open_gate()
This command makes the sealer device open the gate.
<p>&nbsp;</p>

3.     sealer.close_gate()
This command makes the sealer device close the gate.
<p>&nbsp;</p>

4.     sealer.set_temp(temp)
This command makes the sealer device set the temperature for the upcoming seal. If a value is not passed the sealing temperature defaults to 175 degrees Celsius.
<p>&nbsp;</p>

5.     sealer.set_time(time)
This command sets amount of time the sealer device will keep the seal under a specified temperature for the sealing process. If a value is not passed the sealing time defaults to 3 minutes.
<p>&nbsp;</p>

6.     sealer.seal()
This command makes the sealer device seal a microplate for the previously specified amount of time and the previously specified heat.
<p>&nbsp;</p>

7.     sealer.config_robot(temp,time)
This command sets the amount of time the sealing proccess will take and the temperature the plate shall be sealed at.
<p>&nbsp;</p>


## Python Dependencies
Code developed and tested with Python 3.9.12

Required packages:
* Serial Package Installation:

	    pip install pyserial
    
	    conda install pyserial

* Regex Package installation: 

        pip install regex



