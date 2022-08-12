#! /usr/bin/env python3
"""Peeler Node"""

from typing import List, Tuple

import rclpy  # import Rospy
from azenta_driver.sealer_client import A4S_SEALER_CLIENT  # import sealer driver
from rclpy.node import Node  # import Rospy Node
from std_msgs.msg import String

sealer = A4S_SEALER_CLIENT("/dev/ttyUSB0")  # port name for sealer


class sealerNode(Node):

    """
    The init function is neccesary for the sealerNode class to initialize all variables, parameters, and other functions.
    Inside the function the parameters exist, and calls to other functions and services are made so they can be executed in main.
    """

    def __init__(self):
        """Setup sealer node"""

        super().__init__("Sealer_Node")

        print("Sealer is online")

        self.state = "READY"

        timer_period = 0.5  # seconds

        # Format:
        # [
        # [ command, [sealer command 1, sealer command 2]]
        # ]

        self.sealerDescription = [["prepare_sealer", ["set_time", "set_temp", "reset"]]]

        self.i1 = 0  # Count 1

        self.i2 = 0  # Count 2

        self.actionSub = self.create_subscription(
            String, "action", self.actionCallback, 10
        )

        self.actionSub  # prevent unused variable warning

        self.statePub = self.create_publisher(String, "state", 10)

        self.stateTimer = self.create_timer(timer_period, self.stateCallback)

        # self.stateOutput = self.create_timer(timer_period, self.driverCommunication)      Publishing sealer output

        self.descriptionPub = self.create_publisher(String, "description", 10)

        self.descriptionTimer = self.create_timer(
            timer_period, self.descriptionCallback
        )

    def descriptionCallback(
        self, request: str, response: Tuple[str, List]
    ) -> Tuple[str, List]:

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

        if request.description_request == "Sealer":

            response.description_response = self.sealerDescription

            self.get_logger().info("Incoming  Good")

        else:

            response.description_response = "Sealer Description Failed"

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
            # sealer.reset()

            response.action_response = True
        else:
            response.action_response = False

        self.state = "COMPLETED"

    def stateCallback(self):
        """The state of the robot, can be ready, completed, busy, error"""

        msg1 = String()

        msg1.data = "State %s" % self.state

        self.statePub.publish(msg1)

        self.get_logger().info('Publishing: "%s"' % msg1.data)

        self.i1 += 1

        self.state = "READY"


def main(args=None):  # noqa: D103

    rclpy.init(args=args)  # initialize Ros2 communication

    node = sealerNode()

    rclpy.spin(node)  # keep Ros2 communication open for action node

    rclpy.shutdown()  # kill Ros2 communication


if __name__ == "__main__":

    main()
