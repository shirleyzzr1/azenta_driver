#! /usr/bin/env python3
"""Sealer Node"""

from typing import List, Tuple

import rclpy  # import Rospy
from azenta_driver.sealer_client import A4S_SEALER_CLIENT  # import sealer driver
from rclpy.node import Node  # import Rospy Node
from sp_module_services.srv import PeelerActions, PeelerDescription
from std_msgs.msg import String

class sealerNode(Node):

    """
    The init function is neccesary for the sealerNode class to initialize all variables, parameters, and other functions.
    Inside the function the parameters exist, and calls to other functions and services are made so they can be executed in main.
    """

    def __init__(self, PORT = "/dev/ttyUSB0", NODE_NAME = "Sealer_Node"):
        """Setup sealer node"""

        super().__init__(NODE_NAME)

        self.sealer = A4S_SEALER_CLIENT(PORT)
        print("Sealer is online")               # Wakeup Message
        self.state = "UNKOWN"

        self.description = {
            'name': NODE_NAME,
            'type':'',
            'actions':
            {
                'prepare_sealer':'%d %d'
            }
            }

        timer_period = 0.5  # seconds
        self.statePub = self.create_publisher(String, "sealer_state", 10)       # Publisher for sealer state
        self.stateTimer = self.create_timer(timer_period, self.stateCallback)   # Callback that publishes to sealer state

        self.actionSrv = self.create_service(PeelerActions, NODE_NAME + "/actions", self.actionCallback)

        self.descriptionSrv = self.create_service(PeelerDescription, NODE_NAME + "/description", self.descriptionCallback)


    def descriptionCallback(self, request, response):
        """The descriptionCallback function is a service that can be called to showcase the available actions a robot
        can preform as well as deliver essential information required by the master node.

        Parameters:
        -----------
        request: str
            Request to the robot to deliver actions
        response: Tuple[str, List]
            The actions a robot can do, will be populated during execution

        Returns
        -------
        Tuple[str, List]
            The robot steps it can do
        """
        response.description_response = str(self.description)

        return response

    def actionCallback(self, request: str, response: str) -> None:

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
        self.manager_command = "prepare_sealer"  # request.action # Run commands if manager sends corresponding command

        self.state = "BUSY"

        if "prepare_sealer" in self.manager_command:
            sealer.set_time()
            sealer.set_temp()
            sealer.reset()

            response.action_response = True
        else:
            response.action_response = False

        self.state = "COMPLETED"

    def stateCallback(self):
        """The state of the robot, can be ready, completed, busy, error"""

        msg = String()

        msg.data = "State %s" % self.state

        self.statePub.publish(msg)

        self.get_logger().info('Publishing: "%s"' % msg.data)

        self.state = "READY"


def main(args=None):  # noqa: D103

    PORT = "/dev/ttyUSB0"       # Port name for peeler
    NODE_NAME = "Sealer_Node"   # Node name for peeler   

    rclpy.init(args=args)  # initialize Ros2 communication

    node = sealerNode()

    rclpy.spin(node)  # keep Ros2 communication open for action node

    rclpy.shutdown()  # kill Ros2 communication


if __name__ == "__main__":

    main()
