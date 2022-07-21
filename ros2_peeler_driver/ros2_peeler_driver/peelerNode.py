#! /usr/bin/env python3

import rclpy                 # import Rospy
from rclpy.node import Node  # import Rospy Node
from std_msgs.msg import String
from services.srv import PeelerDescription


from .drivers.peeler_client import BROOKS_PEELER_CLIENT # import peeler driver

peeler = BROOKS_PEELER_CLIENT("/dev/ttyUSB0")           # port name for peeler

class peelerNode(Node):
    '''
    The peelerNode inputs data from the 'action' topic, providing a set of commands for the driver to execute. It then receives feedback, 
    based on the executed command and publishes the state of the peeler and a description of the peeler to the respective topics.
    '''
    def __init__(self):


        '''
        The init function is neccesary for the peelerNode class to initialize all variables, parameters, and other functions.
        Inside the function the parameters exist, and calls to other functions and services are made so they can be executed in main.
        '''

        super().__init__('Peeler_Node')
        
        print("Wakey wakey eggs & bakey")

        self.peelerDescription = ["Hello", "World"]


        timer_period = 0.5  # seconds

        self.i1 = 0         # Count 1   


        self.statePub = self.create_publisher(String, ' ', 10)

        self.stateTimer = self.create_timer(timer_period, self.stateCallback)


        # self.actionService = self.create_service(String, "actionCall", self.actionService)

#############################################################################
        self.srv = self.create_service(PeelerDescription, "peeler_description", self.descriptionCallback)


    def descriptionCallback(self, request, response):

        '''
        the descriptionCallback function is a service that can be called to showcase the available actions a robot
        can preform as well as deliver essential information required by the master node.
        '''

        if request.description_request == 'Peeler': 

            response.description_response = self.peelerDescription

            self.get_logger().info('Incoming request Good')
        
        else:

            response.description_response = 'Peeler Description Failed'

        return response


    # def actionService(self, request, response):


    #     self.manager_command = request.action # Run commands if manager sends corresponding command

    #     match self.manager_command:
            
    #         case "test_command":
    #             peeler.check_status()
    #             peeler.check_version()
    #             peeler.reset()

    #             response.success = True
            
    #         case other:
    #             response.success = False

    #     # while peeler.peeler_output.count("ready") < command_count:


    #     # return response
    

    def stateCallback(self):

        '''
        Publishes the peeler state to the 'state' topic. 
        '''

        msg1 = String()
        msg1.data = 'This is the state topic: %d' % self.i1
        self.statePub.publish(msg1)
        self.get_logger().info('Publishing: "%s"' % msg1.data)
        self.i1 += 1


        
    def driverCommunication(self):

        '''
        Matches action received from action subscriber to peeler actions,
        and makes driver execute the command required to complete the action.
        '''

        self.manager_command = "test_command"  # Run commands if manager sends corresponding command


        match self.manager_command:
            
            case "test_command":
                peeler.check_status()
                peeler.check_version()
                peeler.reset()
    
        # self.statePub.publish(peeler.peeler_output)
        # self.get_logger().info('Publishing: "%s"' % peeler.peeler_output)      Publishing peeler output


def main(args = None):

    rclpy.init(args=args)  # initialize Ros2 communication

    node = peelerNode()

    rclpy.spin(node)     # keep Ros2 communication open for action node

    rclpy.shutdown()     # kill Ros2 communication


if __name__ == '__main__':

    main()
