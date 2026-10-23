#!/usr/bin/env python3
# This line tells Linux this is a Python3 script

# ===== IMPORT SECTION =====
import rclpy  # Import the ROS2 Python library
from rclpy.node import Node  # Import the Node class - the base for all ROS2 nodes
from geometry_msgs.msg import Vector3  # Import the Vector3 message type


# ===== CLASS DEFINITION =====
class MinimalPublisher(Node):
    """
    A publisher node that sends Vector3 (x, y, z) dimension messages.
    """
    
    def __init__(self):
        """
        Constructor: This runs when you create a MinimalPublisher object.
        It sets up the publisher, timer, and coordinate variables.
        """
        # Call the parent class (Node) constructor and name this node
        super().__init__('minimal_publisher')
        
        # Create a publisher object:
        # - It will publish Vector3 messages
        # - On the topic named 'topic'
        # - With a queue size of 10
        self.publisher_ = self.create_publisher(Vector3, 'topic', 10)
        
        # Create a timer that calls timer_callback every 0.5 seconds
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Initialize coordinate variables
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        
        # Print a message to confirm the node started
        self.get_logger().info('Talker node has been started!')
    
    def timer_callback(self):
        """
        This function runs every 0.5 seconds (because of the timer).
        It creates a Vector3 message, publishes it, and logs it to the console.
        """
        # Create a new Vector3 message object
        msg = Vector3()
        
        # Set the message fields (x, y, z)
        msg.x = self.x
        msg.y = self.y
        msg.z = self.z
        
        # Publish the message on the topic
        self.publisher_.publish(msg)
        
        # Log the message to the terminal
        self.get_logger().info('Publishing: "x: %.2f, y: %.2f, z: %.2f"' % (msg.x, msg.y, msg.z))
        
        # Increment the values for the next message
        self.x += 1.25
        self.y += 1.50
        self.z += 1.75


# ===== MAIN FUNCTION =====
def main(args=None):
    """
    The main function that runs when you execute this script.
    """
    # Initialize the ROS2 Python library
    rclpy.init(args=args)
    
    # Create an instance of our MinimalPublisher class
    minimal_publisher = MinimalPublisher()
    
    # Keep the node running and processing callbacks
    rclpy.spin(minimal_publisher)
    
    # Clean up
    minimal_publisher.destroy_node()
    
    # Shutdown the ROS2 Python library
    rclpy.shutdown()


# ===== SCRIPT ENTRY POINT =====
if __name__ == '__main__':
    main()
