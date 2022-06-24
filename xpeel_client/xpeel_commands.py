import serial
import time

from peeler_client import BROOKS_PEELER_CLIENT


ser = serial.Serial("/dev/ttyUSB0", 9600)

# ser.reset_input_buffer()
# ser.reset_output_buffer()

# time.sleep(1)

ser.write("*reset\r\n".encode('utf-8'))        

































# ser_cmd = '*version\r\n'
# ser.reset_input_buffer()
# ser.reset_output_buffer()
# time.sleep(1)
# ser.write(ser_cmd.encode('utf-8'))
# time.sleep(1)
# # print(ser.read)
# print(ser.inWaiting())

# print(ser.out_waiting)

# for res_line in range(10):
#     response = ser.read_until(expected=b'\r')
#     print(response)





    # def error(self):        
    #     error_dict = {
    #         "00" : "",
    #         "01" : "Conveyor motor stalled",
    #         "02" : "Elevator motor stalled",
    #         "03" : "Take up spool stalled",
    #         "04" : "Seal not removed",
    #         "05" : "Illegal Command",
    #         "06" : "No Plate found (Error only given if plate check option set to Yes)",
    #         "07" : "Out of tape, or tape broke",
    #         "08" : "Parameters not saved",
    #         "09" : "Stop button pressed while running",
    #         "10" : "Seal Sensor unplugged or broke",
    #         "20" : "Less than 30 seals left on the supply roll",
    #         "21" : "Room for less than 30 seals on take up spool",
    #         "51" : "Emergency Stop: Power relay is not settable- i.e. cover open, or hardware problem",
    #         "52" : "Circuitry Fault Detected: Remove Power"
    #         }

    #     ser = self.connect_sealer()

    #     while True:
    #         response = ser.read_until(expected=b'\r')
    #         response_string = response.decode('utf-8')
    #         if "ready" in response_string:
    #             error_code = response_string[7:]
    #             first_error = error_code[0:2]
    #             second_error = error_code[3:5]
    #             third_error = error_code [6:8]
    #             if first_error and second_error and third_error == "00":
    #                 print("No Errors")
    #             else:
    #                 print(error_dict[first_error])
    #                 print(error_dict[second_error])
    #                 print(error_dict[third_error])
    #             break
    #         print(response_string)

            # #Confirm Restart
            # if restart == True:
            #     if "*ack" in response_string:
            #         success_cmd_correct = True
            #         break
            #     else:
            #         success_cmd_correct = False

            # #Confirm Request
            # if request == True:
            #     if "*ack" in response_string:
            #         success_cmd_correct = True
            #         break
            #     else:
            #         success_cmd_correct = False
            # #Confirm Seal Check
            # if seal_check == True:
            #     if "*setup" in response_string:
            #         success_cmd_correct = True
            #         break
            #     else:
            #         success_cmd_correct = False

        # reset buffer (must do before sending commands)
        # ser.reset_input_buffer()
        # ser.reset_output_buffer()
# 