from ast import Pass
import os.path
import time
import serial
import logging

#Log Configuration
# file_path = os.path.join(os.path.split(os.path.dirname(__file__))[0]  + '/sealer_logs/sealer_logs.log')
# logging.basicConfig(filename = file_path, level=logging.DEBUG, format = '[%(levelname)s] [%(asctime)s] [%(name)s] %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')


class BROOKS_PEELER_CLIENT():
    """
    Description: 
                 - Python interface that allows remote commands to be executed using simple string messages over TCP/IP on PF400 cobot. 
    Serial Communication Messages from the Robot:
                 - Responses begin with a "0" if the command was successful, or a negative error code number
    """
    def __init__(self, host_path, baud_rate=9600):

        self.host_path = host_path
        self.baud_rate = baud_rate
        ser = self.connect_peeler()

    def connect_peeler(self):
        #Connect to serial port / If wrong port entered inform user 
        try:
            ser = serial.Serial(self.host_path, self.baud_rate)
        except:
            print("Wrong port entered")
            pass
        #ser = serial.Serial(self.host_path, self.baud_rate)
        return ser




    def send_command(self, command, success_msg = "", err_msg = "", firmware_ver = "Not Found"):

        #check if connected / if not (error? / reconnect?)
        ser = self.connect_sealer()

        #reset buffer (must do before sending commands)
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        time.sleep(1)
        ser.write(command.encode('utf-8'))        
        
        #Declares success/error messsage if none are given

        if success_msg == "":
            success_msg = 'Sent Command'
        if err_msg == "":
            err_msg = "Failed to Send Command:"

        response = ser.read_until(expected=b'\r')
        response_string = response.decode('utf-8')
        #Prints specific errors
        while "ready" not in response_string:
            if response_string[0] == "*" and response_string[1].isdigit() and response_string[2] == "." and response_string[3].is_digit():
                firmware_ver = response_string[1:4]
                if firmware_ver == "Not Found":
                    print(err_msg)
                else:
                    print(success_msg)
        self.error()


    def error(self):        
        error_dict = {
            "00" : "",
            "01" : "Conveyor motor stalled",
            "02" : "Elevator motor stalled",
            "03" : "Take up spool stalled",
            "04" : "Seal not removed",
            "05" : "Illegal Command",
            "06" : "No Plate found (Error only given if plate check option set to Yes)",
            "07" : "Out of tape, or tape broke",
            "08" : "Parameters not saved",
            "09" : "Stop button pressed while running",
            "10" : "Seal Sensor unplugged or broke",
            "20" : "Less than 30 seals left on the supply roll",
            "21" : "Room for less than 30 seals on take up spool",
            "51" : "Emergency Stop: Power relay is not settable- i.e. cover open, or hardware problem",
            "52" : "Circuitry Fault Detected: Remove Power"
            }

        ser = self.connect_sealer()
        response = ser.read_until(expected=b'\r')
        response_string = response.decode('utf-8')
        
        if "ready" in response_string:
            error_code = response_string[7:]
            first_error = error_code[0:2]
            second_error = error_code[3:5]
            third_error = error_code [6:8]
            if first_error and second_error and third_error == "00":
                print("No Errors")
            else:
                print(error_dict[first_error])
                print(error_dict[second_error])
                print(error_dict[third_error])




    def status(self):
        cmd_string = '*stat\r\n'
        success_msg = "Displaying status"
        err_msg = "Failed to display status"
        self.send_command(cmd_string, success_msg, err_msg)
    
    def version(self, firmware_ver = "Not Found"):
        cmd_string = '*version\r\n'
        success_msg = "XPeel Firmware Version: %d"(firmware_ver)
        err_msg = "Failed to display XPeel firmware version"
        self.send_command(cmd_string, success_msg, err_msg)

    def reset(self):
        cmd_string = '*reset\r\n'
        success_msg = "Displaying XPeel Firmware Version"
        err_msg = "Failed to Display XPeel Firmware Version"
        self.send_command(cmd_string, success_msg, err_msg)
    
    def restart(self):
        cmd_string = '*restart\r\n'
        success_msg = "Restarting XPeel"
        err_msg = "Failed to restart XPeel"
        self.send_command(cmd_string, success_msg, err_msg)        
    
    def location_and_speed(self):
        cmd_string = '*xpeel:AB\r\n'
        success_msg = "Adjusting Peel Location to ___ and Speed to ___"
        err_msg = "Failed to Adjust Peel Location to ___ and Speed to ___"
        self.send_command(cmd_string, success_msg, err_msg)      

    def seal_check(self):
        cmd_string = '*sealcheck\r\n'
        success_msg = "Seal Check Conducted"
        err_msg = "Failed to Conduct Seal Check"
        self.send_command(cmd_string, success_msg, err_msg)        
    
    def tape_remaining(self):
        cmd_string = '*tapeleft\r\n'
        success_msg = "__ Tape Remaining"
        err_msg = "Failed to find amount of tape remaining"
        self.send_command(cmd_string, success_msg, err_msg)   

    def plate_check(self):
        cmd_string = '*platecheck\r\n'
        success_msg = "Platecheck set to "
        err_msg = "Failed to set Plate Check"
        self.send_command(cmd_string, success_msg, err_msg)   

    def sensor_threshold(self):
        cmd_string = '*sealstat\r\n'
        success_msg = "Threshold value of __ for the seal detected sensor"
        err_msg = "Failed to get threshold value"
        self.send_command(cmd_string, success_msg, err_msg)   

    def sensor_higher_threshold(self):
        cmd_string = '*sealhigher:XXX\r\n'
        success_msg = "Threshold value of __ for the seal detected sensor"
        err_msg = "Failed to get threshold value"
        self.send_command(cmd_string, success_msg, err_msg)  

    def sensor_lower_threshold(self):
        cmd_string = '*seallower:XXX\r\n'
        success_msg = "Threshold value of __ for the seal detected sensor"
        err_msg = "Failed to get threshold value"
        self.send_command(cmd_string, success_msg, err_msg)    

    def conveyor_out(self):
        cmd_string = '*moveout\r\n'
        success_msg = "Conveyor moved out"
        err_msg = "Failed to move conveyor out"
        self.send_command(cmd_string, success_msg, err_msg) 

    def conveyor_in(self):
        cmd_string = '*movein\r\n'
        success_msg = "Conveyor moved in"
        err_msg = "Failed to move conveyor in"
        self.send_command(cmd_string, success_msg, err_msg) 

    def elevator_down(self):
        cmd_string = '*movedown\r\n'
        success_msg = "Elevator moved down"
        err_msg = "Failed to move elevator down"
        self.send_command(cmd_string, success_msg, err_msg) 

    def elevator_up(self):
        cmd_string = '*moveup\r\n'
        success_msg = "Elevator moved up"
        err_msg = "Failed to move elevator up"
        self.send_command(cmd_string, success_msg, err_msg) 

    def move_spool(self):
        cmd_string = '*movespool\r\n'
        success_msg = "Spool advanced approximately 10 mm"
        err_msg = "Failed to advance spool"
        self.send_command(cmd_string, success_msg, err_msg) 

if __name__ == "__main__":

    dummy_seal = BROOKS_PEELER_CLIENT("/dev/ttyUSB0")
    # dummy_seal.reset()
    dummy_seal.reset()
    