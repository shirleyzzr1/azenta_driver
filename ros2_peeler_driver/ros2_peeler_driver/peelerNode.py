#! /usr/bin/env python3

import rclpy                 # import Rospy
from rclpy.node import Node  # import Rospy Node
from std_msgs.msg import String


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


        timer_period = 0.5  # seconds

        self.i1 = 0         # Count 1 

        self.i2 = 0         # Count 2
        

        self.actionSub = self.create_subscription(String, 'action', self.actionCallback, 10)

        self.actionSub  # prevent unused variable warning


        self.statePub = self.create_publisher(String, 'state', 10)

        self.stateTimer = self.create_timer(timer_period, self.stateCallback)

        
        # self.stateOutput = self.create_timer(timer_period, self.driverCommunication)      Publishing peeler output

        
        self.descriptionPub = self.create_publisher(String, 'description', 10)

        self.descriptionTimer = self.create_timer(timer_period, self.descriptionCallback)


    def actionCallback(self, msg):

        '''
        Stores the data received from the 'action' topic.
        '''

        self.get_logger().info('I am the action topic "%s"' % msg.data)


    def stateCallback(self):
        '''
        Publishes the peeler state to the 'state' topic.
        '''
        msg1 = String()
        msg1.data = 'This is the state topic: %d' % self.i1
        self.statePub.publish(msg1)
        self.get_logger().info('Publishing: "%s"' % msg1.data)
        self.i1 += 1

    def descriptionCallback(self):
        '''
        Publishes the peeler description to the 'description' topic.
        '''

        msg2 = String()
        msg2.data = 'This is the description topic %d' % self.i2
        self.descriptionPub.publish(msg2)
        self.get_logger().info('Publishing: "%s"' % msg2.data)
        self.i2 += 1

        
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
