# Azenta Module

## Install Notes

	sudo mkdir /opt/spm_module
	sudo chmod 777 /opt/spm_module
	cd /opt/spm_module
	mkdir src
	cd src
	git clone https://github.com/AD-SDL/azents_driver
	cd ..
	rosdep install
	colcon build

move the 'SPM.service' into 
