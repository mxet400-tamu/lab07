#!/usr/bin/env python3
# This line tells Linux this is a Python3 script

# ===== IMPORT SECTION =====
import rclpy  # Import the ROS2 Python library
from rclpy.node import Node  # Import the Node class
from geometry_msgs.msg import Vector3  # Import the Vector3 message type


# ===== CLASS DEFINITION =====
class MinimalSubscriber(Node):
    """
    A subscriber node that listens for Vector3 messages and calculates volume.
    """
    
    def __init__(self):
        """
        Constructor: Sets up the subscriber.
        """
        # Call the parent class (Node) constructor and name this node
        super().__init__('minimal_subscriber')
        
        # Create a subscriber object:
        # - It will listen for Vector3 messages
        # - On the topic named 'topic'
        # - When a message arrives, call listener_callback
        # - Queue size of 10
        self.subscription = self.create_subscription(
            Vector3,                   # Message type
            'topic',                   # Topic name
            self.listener_callback,    # Callback function
            10)                        # Queue size
        
        # Prevent unused variable warning
        self.subscription
        
        # Print a message to confirm the node started
        self.get_logger().info('Listener node has been started and is waiting for messages...')
    
    def listener_callback(self, msg):
        """
        This function is called automatically every time a message arrives.
        Calculates the volume (x * y * z) and logs the dimensions and volume.
        """
        # Calculate volume based on received x, y, z dimensions
        volume = msg.x * msg.y * msg.z
        
        # Log the received message and calculated volume to the terminal
        self.get_logger().info('I heard: "x: %.2f, y: %.2f, z: %.2f" (Volume: %.2f)' % (msg.x, msg.y, msg.z, volume))


# ===== MAIN FUNCTION =====
def main(args=None):
    """
    The main function that runs when you execute this script.
    """
    # Initialize the ROS2 Python library
    rclpy.init(args=args)
    
    # Create an instance of our MinimalSubscriber class
    minimal_subscriber = MinimalSubscriber()
    
    # Keep the node running and listening for messages
    rclpy.spin(minimal_subscriber)
    
    # Clean up
    minimal_subscriber.destroy_node()
    
    # Shutdown the ROS2 Python library
    rclpy.shutdown()


# ===== SCRIPT ENTRY POINT =====
if __name__ == '__main__':
    main()
