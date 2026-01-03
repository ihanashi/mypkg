import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

class PersonCounter(Node):

    def __init__(self):
        super().__init__('person_listener')
        self.sub = self.create_subscription(
            Person,
            'person',
            self.cb,
            10
        )
        self.total = 0
        self.sum_age = 0

    def cb(self, msg):
        self.total += 1
        self.sum_age += msg.age
        avg = self.sum_age / self.total

        self.get_logger().info(
            f"Received {self.total} people | "
            f"Latest: {msg.name} ({msg.age}) | "
            f"Average age: {avg:.1f}"
        )


def main():
    rclpy.init()
    node = PersonCounter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

