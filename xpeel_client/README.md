## Peeler Driver

A repository for Brooks XPeel, including user manuals and remote control interfaces.

###  Peeler Remote Client 
* Peeler is the main object responsible for removing seals off of microplates

### Current Features
* Peeler initialization
* Peeler information (version number, current status, tape remaining, etc.)
* Basic movements (move conveyor, spool, reset microplate, etc.)
* Execute peeling 
* Change sensor threshold value
* Displays up to 3 error messages

### Installation Requirements
* Python Version: X or higher
* Serial Package Installation:
	* python -m pip install pyserial
	* conda install pyserial
* Regex Package installation: 	
	* pip install regex

