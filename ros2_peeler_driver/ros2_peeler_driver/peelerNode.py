#! /usr/bin/env python3

import rclpy                 # import Rospy
from rclpy.node import Node  # import Rospy Node
from std_msgs.msg import String


from .drivers.peeler_client import BROOKS_PEELER_CLIENT # import peeler driver

peeler = BROOKS_PEELER_CLIENT("/dev/ttyUSB0")           # port name for peeler

class peelerNode(Node):

    def __init__(self):

        super().__init__('Peeler_Node')

        print('Hi from ros2_peeler_driver.')


        timer_period = 0.5  # seconds

        self.i1 = 0         # Count 1 

        self.i2 = 0         # Count 2


        self.actionSub = self.create_subscription(String, 'action', self.actionCallback, 10)

        self.actionSub  # prevent unused variable warning


        self.statePub = self.create_publisher(String, 'state', 10)

        self.stateTimer = self.create_timer(timer_period, self.stateCallback)

        
        self.descriptionPub = self.create_publisher(String, 'description', 10)

        self.descriptionTimer = self.create_timer(timer_period, self.descriptionCallback)


    def actionCallback(self, msg):

        self.get_logger().info('I am the action topic: "%s"' % msg.data)


    def stateCallback(self):
        
        msg1 = String()
        msg1.data = 'This is the state topic: %d' % self.i1
        self.statePub.publish(msg1)
        self.get_logger().info('Publishing: "%s"' % msg1.data)
        self.i1 += 1

    def descriptionCallback(self):
        
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


        print(peeler.peeler_output)


def main(args = None):

    rclpy.init(args=args)  # initialize Ros2 communication

    node = peelerNode()

    rclpy.spin(node)     # keep Ros2 communication open for action node

    rclpy.shutdown()     # kill Ros2 communication


if __name__ == '__main__':

    main()
