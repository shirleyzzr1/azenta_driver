#! /usr/bin/env python3
"""Peeler node"""

from typing import List, Tuple

import rclpy  # import Rospy
from azenta_driver.peeler_client import BROOKS_PEELER_CLIENT  # import peeler driver
from rclpy.node import Node  # import Rospy Node
from sp_module_services.srv import PeelerActions, PeelerDescription
from std_msgs.msg import String


class peelerNode(Node):
    """
    The peelerNode inputs data from the 'action' topic, providing a set of commands for the driver to execute. It then receives feedback,
    based on the executed command and publishes the state of the peeler and a description of the peeler to the respective topics.
    """

    def __init__(self, PORT="/dev/ttyUSB0", NODE_NAME="Peeler_Node"):
        """
        The init function is neccesary for the peelerNode class to initialize all variables, parameters, and other functions.
        Inside the function the parameters exist, and calls to other functions and services are made so they can be executed in main.
        """

        super().__init__(NODE_NAME)

        self.peeler = BROOKS_PEELER_CLIENT(PORT)

        print("peeler is online")

        self.state = "UNKNOWN"

        # Format:
        # [
        # [command, [peeler command 1, peeler command 2], [[paramater 1( peeler command 1), paramater 2( peeler command 1)], [""],[""]]
        # repeat
        # ]

        self.peelerDescription = [
            [
                "prepare_peeler",
                ["reset", "check_version", "check_status"],
                [[""], [""], [""]],
            ],
            ["standard_peel", ["seal_check", "peel"], [[""], ["loc", "time"]]],
            ["check_threshold", ["sensor_threshold"], [[""]]],
        ]

        timer_period = 0.5  # seconds

        self.statePub = self.create_publisher(String, "state", 10)

        self.stateTimer = self.create_timer(timer_period, self.stateCallback)

        self.actionSrv = self.create_service(
            PeelerActions, "peeler_actions", self.actionCallback
        )

        self.descriptionSrv = self.create_service(
            PeelerDescription, "peeler_description", self.descriptionCallback
        )

    def descriptionCallback(self, request: str, response: Tuple[str, List]):
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
        if request.description_request == "Peeler":

            response.description_response = self.peelerDescription

            self.get_logger().info("Incoming  Good")

        else:

            response.description_response = "Peeler Description Failed"

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

        self.manager_command = (
            request.action_request
        )  # Run commands if manager sends corresponding command

        self.state = "BUSY"

        self.stateCallback()

        if "prepare_peeler" in self.manager_command:
            self.peeler.reset()
            self.peeler.check_version()
            self.peeler.check_status()

            response.action_response = True

        elif "standard_peel" in self.manager_command:
            self.peeler.seal_check()
            self.peeler.peel(1, 2.5)

            response.action_response = True

        elif "check_threshold" in self.manager_command:
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

    PORT = "/dev/ttyUSB0"  # port name for peeler
    NAME = "Peeler_Node"

    rclpy.init(args=args)  # initialize Ros2 communication

    node = peelerNode(PORT=PORT, NODE_NAME=NAME)

    rclpy.spin(node)  # keep Ros2 communication open for action node

    rclpy.shutdown()  # kill Ros2 communication


if __name__ == "__main__":

    main()
