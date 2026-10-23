#!/usr/bin/env python3
# This line tells Linux this is a Python3 script

# ===== IMPORT SECTION =====
import rclpy  # Import the ROS2 Python library
from rclpy.node import Node  # Import the Node class
from std_msgs.msg import String  # Import the String message type


# ===== CLASS DEFINITION =====
class MinimalSubscriber(Node):
    """
    A simple subscriber node that listens for messages.
    This class inherits from Node, just like the publisher.
    """
    
    def __init__(self):
        """
        Constructor: Sets up the subscriber.
        """
        # Call the parent class (Node) constructor and name this node
        super().__init__('minimal_subscriber')
        
        # Create a subscriber object:
        # - It will listen for String messages
        # - On the topic named 'topic' (MUST match the publisher's topic name!)
        # - When a message arrives, call listener_callback
        # - Queue size of 10
        self.subscription = self.create_subscription(
            String,                    # Message type
            'topic',                   # Topic name
            self.listener_callback,    # Callback function
            10)                        # Queue size
        
        # This prevents unused variable warnings (Python thing)
        self.subscription
        
        # Print a message to confirm the node started
        self.get_logger().info('Listener node has been started and is waiting for messages...')
    
    def listener_callback(self, msg):
        """
        This function is called automatically every time a message arrives.
        The 'msg' parameter contains the received message.

        For this example, data is the name of the variable within the String message
        and is a string message type. So msg.data is the actual string content of the message.
        """
        # Log the received message to the terminal
        self.get_logger().info('I heard: "%s"' % msg.data)


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
    # This is a blocking call - the program stays here until Ctrl+C
    rclpy.spin(minimal_subscriber)
    
    # Clean up: Destroy the node explicitly
    minimal_subscriber.destroy_node()
    
    # Shutdown the ROS2 Python library
    rclpy.shutdown()


# ===== SCRIPT ENTRY POINT =====
if __name__ == '__main__':
    # If this script is run directly, execute main()
    main()
