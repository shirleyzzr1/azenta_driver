#! /usr/bin/env python3

import rclpy                 # import Rospy
from rclpy.node import Node  # import Rospy Node
from std_msgs.msg import String

from services.srv import PeelerDescription
from services.srv import PeelerActions


class masterNode(Node):

    '''
    The peelerNode inputs data from the 'action' topic, providing a set of commands for the driver to execute. It then receives feedback, 
    based on the executed command and publishes the state of the peeler and a description of the peeler to the respective topics.
    '''

    def __init__(self):
 

        '''
        The init function is neccesary for the peelerNode class to initialize all variables, parameters, and other functions.
        Inside the function the parameters exist, and calls to other functi ons and services are made so they can be executed in main.
        '''

        super().__init__('Master_Node')
        
        print("Wakey wakey eggs & bakey")

        # self.descriptionSer = self.create_service(List, 'description', self.descriptionCallback, 10)
        

        self.stateSub = self.create_subscription(String, 'state', self.stateCallback, 10)
        
        self.stateSub # prevent unused variable warning


###################################### Client writing in progress

        # self.actionCli = self.create_client(PeelerActions, 'add_two_ints')

        # while not self.actionCli.wait_for_service(timeout_sec=1.0):

        #     self.get_logger().info('service not available, waiting again...')

        # self.actionReq = PeelerActions.Request()


    # def send_request(self, msg):
    #     self.req.a = a
    #     self.req.b = b
    #     self.future = self.cli.call_async(self.req)
    #     rclpy.spin_until_future_complete(self, self.future)
    #     return self.future.result()

####################################
    def descriptionCallback(self, request, response):

        '''
        sets variable of commands, client command list, client commands, 
        and parameters to the name of the commands, client command list, client commands, and parameters
        '''
        
        for response_command in response.command:
            # Command name
            # Format: <command name>
            globals()[f'{response_command[0]}'] = response_command[0]
            
            # Peeler commands
            #Format: <command name>_command_list
            globals()[f'{response_command[0]}_command_list'] = response_command[1]



            # Each Peeler Command
            # Format: <command name>_<peeler_command(without parentheses)>
            for peeler_command_index,peeler_command in enumerate(response_command[1]):
                globals()[f'{response_command[0]}_{peeler_command}'] = peeler_command

                

                # Parameter List
                # Format: <command name>_<peeler_command(without parentheses)>_parameter_list
                for parameter_list in response_command[2]:
                    globals()[f'{response_command[0]}_{peeler_command}_parameter_list'] = response_command[2][peeler_command_index]
                
                    # Parameter
                    # Format: <command name>_<peeler_command(without parentheses)>_<parameter>
                    for parameter in parameter_list:
                        globals()[f'{response_command[0]}_{peeler_command}_{parameter}'] = parameter


        response.success = True


    def stateCallback(self, msg):

        '''
        The stateCallback function is called to subscribe to the state published by the peelerNode
        '''

        self.get_logger().info('My state is: "%s"' % msg.data)


def main(args = None):

    rclpy.init(args=args)  # initialize Ros2 communication

    node = masterNode()

    rclpy.spin(node)     # keep Ros2 communication open for action node

    rclpy.shutdown()     # kill Ros2 communication


if __name__ == '__main__':

    main()
