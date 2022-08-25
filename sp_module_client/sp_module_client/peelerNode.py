#! /usr/bin/env python3
"""Peeler node"""

from typing import List, Tuple

import rclpy  # import Rospy
from azenta_driver.peeler_driver import BROOKS_PEELER_CLIENT  # import peeler driver
from rclpy.node import Node  # import Rospy Node
from wei_services.srv import WeiActions, WeiDescription
from std_msgs.msg import String


class peelerNode(Node):
    """
    The peelerNode inputs data from the 'action' topic, providing a set of commands for the driver to execute. It then receives feedback,
    based on the executed command and publishes the state of the peeler and a description of the peeler to the respective topics.
    """

    def __init__(self, PORT="/dev/ttyUSB0", NODE_NAME="peelerNode"):
        """
        The init function is neccesary for the peelerNode class to initialize all variables, parameters, and other functions.
        Inside the function the parameters exist, and calls to other functions and services are made so they can be executed in main.
        """

        super().__init__(NODE_NAME)

        self.peeler = BROOKS_PEELER_CLIENT(PORT)
        print("Peeler is online")                   # Wakeup Message
        self.state = "UNKNOWN" 

        self.description = {
            'name': NODE_NAME,
            'type':'',
            'actions':
            {
                'peel':'%d %d'
            }
            }

        timer_period = 1  # seconds
        self.statePub = self.create_publisher(String, "peeler_state", 10)       # Publisher for peeler state
        self.stateTimer = self.create_timer(timer_period, self.stateCallback)   # Callback that publishes to peeler state

        self.actionSrv = self.create_service(WeiActions, NODE_NAME + "/actions", self.actionCallback)

        self.descriptionSrv = self.create_service(WeiDescription, NODE_NAME + "/description", self.descriptionCallback)

    def descriptionCallback(self, request, response):
        """The descriptionCallback function is a service that can be called to showcase the available actions a robot
        can preform as well as deliver essential information required by the master node.

        Parameters:
        -----------
        request: str
            Request to the robot to deliver actions
        response: str
            The actions a robot can do, will be populated during execution

        Returns
        -------
        str
            The robot steps it can do
        """
        response.description_response = str(self.description)

        return response
        
        
    def actionCallback(self, request, response):
        """The actions the robot can perform, also performs them

        Parameters:
        -----------
        request: str
            Request to the robot to perform an action
        respone: bool
            If action is performed

        Returns
        -------
        None
        """

        action_handle = request.action_handle  # Run commands if manager sends corresponding command
        self.state = "BUSY"
        self.stateCallback()

        if "status" in action_handle:
            self.peeler.reset()
            self.peeler.check_version()
            self.peeler.check_status()

            response.action_response = True

        elif "peel" in action_handle:
            self.peeler.seal_check()
            self.peeler.peel(1, 2.5)

            response.action_response = True

        elif "check_threshold" in action_handle:
            self.peeler.sensor_threshold()

            response.action_response = True

        else:
            response.action_response = False

        self.state = "COMPLETED"

        if "Error:" in self.peeler.peeler_output:
            self.state = self.peeler.error_msg

        return response

    def stateCallback(self):
        """The state of the robot, can be ready, completed, busy, error"""

        msg = String()

        msg.data = "State: %s" % self.state

        self.statePub.publish(msg)

        self.get_logger().info('Publishing: "%s"' % msg.data)

        self.state = "READY"


def main(args=None):  # noqa: D103

    PORT = "/dev/ttyUSB1"       # Port name for peeler
    NODE_NAME = "peelerNode"   # Node name for peeler   

    rclpy.init(args=args)       # initialize Ros2 communication

    node = peelerNode(PORT=PORT, NODE_NAME=NODE_NAME)

    rclpy.spin(node)            # keep Ros2 communication open for action node

    rclpy.shutdown()            # kill Ros2 communication


if __name__ == "__main__":

    main()
