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

        self.stateSub = self.create_subscription(String, 'state', self.stateCallback, 10)
        
        self.stateSub # prevent unused variable warning


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
