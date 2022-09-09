import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class TeleopKeyboard(Node):
    def __init__(self, topic='cmd_vel', linear_vel=0.2, angular_vel=math.radians(20)):
        super().__init__('teleop_keyboard')

        self.pub = self.create_publisher(Twist, topic, 10)
        self.linear_vel = linear_vel
        self.angular_vel = angular_vel
        self.vel = Twist()
    
    def print_description(self):
        self.get_logger().info("w:forward, x:back, a:turn_left, d:turn_right")
    
    def stop(self):
        self.vel.linear.x = 0.0
        self.vel.linear.y = 0.0
        self.vel.linear.z = 0.0
        self.vel.angular.x = 0.0
        self.vel.angular.y = 0.0
        self.vel.angular.z = 0.0
        self.pub.publish(self.vel)
    
    def spin(self):
        key = input("Type Command:")
        if key == "w":
            self.get_logger().info("forward")
            self.vel.linear.x = self.linear_vel
            self.vel.angular.z = 0.0
            self.pub.publish(self.vel)
        if key == "a":
            self.get_logger().info("turn left")
            self.vel.angular.z = self.angular_vel
            self.vel.linear.x = 0.0
            self.pub.publish(self.vel)
        if key == "x":
            self.get_logger().info("back")
            self.vel.linear.x = -self.linear_vel
            self.vel.angular.z = 0.0
            self.pub.publish(self.vel)
        if key == "d":
            self.get_logger().info("turn right")
            self.vel.angular.z = -self.angular_vel
            self.vel.linear.x = 0.0
            self.pub.publish(self.vel)
        if key == "s":
            self.get_logger().info("stop")
            self.stop()
        self.get_logger().info("Velocity: Linear=%f Angular=%f" % (self.vel.linear.x,self.vel.angular.z))

def main(args=None):
    rclpy.init(args=args)
    node = TeleopKeyboard()
    while rclpy.ok():
        try:
            node.spin()
        except KeyboardInterrupt:
            node.stop()
            break
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()