from ast import Pass
import os.path
import time
import serial
import logging

#Log Configuration
# file_path = os.path.join(os.path.split(os.path.dirname(__file__))[0]  + '/sealer_logs/sealer_logs.log')
# logging.basicConfig(filename = file_path, level=logging.DEBUG, format = '[%(levelname)s] [%(asctime)s] [%(name)s] %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')


class A4S_SEALER_CLIENT():
    """
    Description: 
                 - Python interface that allows remote commands to be executed using simple string messages over TCP/IP on PF400 cobot. 
    Serial Communication Messages from the Robot:
                 - Responses begin with a "0" if the command was successful, or a negative error code number
    """
    def __init__(self, host_path, baud_rate=19200):
        '''
        This function initializes the data to be called and modified in other locations in the client.
        '''

        self.host_path = host_path
        self.baud_rate = baud_rate
        ser = self.connect_sealer()

    def connect_sealer(self):
        '''
        Connect to serial port / If wrong port entered inform user 
        '''

        #Connect to serial port / If wrong port entered inform user 
        try:
            ser = serial.Serial(self.host_path, self.baud_rate)
        except:
            print("Wrong port entered")
            pass
        #ser = serial.Serial(self.host_path, self.baud_rate)
        return ser

    def send_command(self, command, success_msg ="", err_msg = ""):
        '''
        Sends the given command to the sealer.
        Resets sealer before sending given command. 
        '''

        ser = self.connect_peeler()
        ser.write(command.encode('*00SR=zz!'))
        ser.write(command.encode('utf-8')) 
     

    def get_error(self):
        pass

    def reset(self):
        '''
        Clears error status/resets shuttle.
        '''

        cmd_string = '*00SR=zz!'
        success_msg = "Conducting System Reset"
        err_msg = "Failed to Conduct System Reset"
        self.send_command(cmd_string, success_msg, err_msg)

    def open_gate(self):
        '''
        Opens shuttle
        '''

        cmd_string = '*00MO=zz!'
        success_msg = "Opening Gate"
        err_msg = "Failed to Open Gate"
        self.send_command(cmd_string, success_msg, err_msg)

    def close_gate(self):
        '''
        Closes shuttle
        '''
        
        cmd_string = '*00MC=zz!'
        success_msg = "Closing Gate"
        err_msg = "Failed to Close Gate"          
        self.send_command(cmd_string, success_msg, err_msg)

    def set_temp(self, temp=100):
        '''
        Adjusts seal to given temperature.
        '''

        cmd_string = '*00DH=0100zz!'
        success_msg = "Setting Temp. to %d°C"%(temp)
        err_msg = "Failed to Set Temp. to 100°C"          
        self.send_command(cmd_string, success_msg, err_msg)
       
    def set_time(self, time=0.5):
        '''
        Adjusts seal time to given time.
        '''

        cmd_string = '*00DT=005zz!'
        success_msg = "Setting Seal Time to %s S"%(time)
        err_msg = "Failed to Set Seal Time to %s S"%(time)
        self.send_command(cmd_string, success_msg, err_msg)

    def seal(self):
        '''
        Conducts seal action.
        '''

        cmd_string = '*00GS=zz!'
        success_msg = "Sealing"
        err_msg = "Failed to Seal"
        self.send_command(cmd_string, success_msg, err_msg)


    def config_robot(self, temp,time):
        '''
        Sets robot to given permission/time
        '''

        self.set_temp(temp)
        self.set_time()



if __name__ == "__main__":
    '''
    Runs given function.
    '''

    dummy_seal = A4S_SEALER_CLIENT("/dev/ttyUSB0")
    # dummy_seal.reset()
    dummy_seal.reset()
    