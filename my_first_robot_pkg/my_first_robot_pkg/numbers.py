#!/usr/bin/env python3
# ===== IMPORT SECTION =====
import rclpy
from rclpy.node import Node
# MODIFY HERE: Import the Vector3 message type from geometry_msgs


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        
        # MODIFY HERE: Create a publisher for Vector3 messages on the topic 'topic' with a queue size of 10
        # self.publisher_ = ...
        
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Initialize coordinate variables
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        
        self.get_logger().info('Numbers publisher node has been started!')
    
    def timer_callback(self):
        # MODIFY HERE:
        # 1. Create a Vector3 message object
        # 2. Set the x, y, and z fields from self.x, self.y, self.z
        # 3. Publish the message
        # 4. Log the published coordinates to the console
        # 5. Increment self.x by 1.25, self.y by 1.50, and self.z by 1.75
        pass

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
