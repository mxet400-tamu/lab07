#!/usr/bin/env python3
# ===== IMPORT SECTION =====
import rclpy
from rclpy.node import Node
# MODIFY HERE: Import the Vector3 message type from geometry_msgs


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        
        # MODIFY HERE: Create a subscription for Vector3 messages on the topic 'topic' with callback listener_callback
        # self.subscription = ...
        
        self.get_logger().info('Volume listener node has been started and is waiting for messages...')
    
    def listener_callback(self, msg):
        # MODIFY HERE:
        # 1. Calculate volume based on received x, y, z dimensions (volume = x * y * z)
        # 2. Log the dimensions and calculated volume to the terminal
        pass

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
