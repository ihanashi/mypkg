import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

class PersonPublisher(Node):

    def __init__(self):
        super().__init__('person_talker')
        self.pub = self.create_publisher(Person, 'person', 10)
        self.timer = self.create_timer(0.5, self.cb)
        self.count = 0

    def cb(self):
        msg = Person()
        msg.name = "Hanashi"
        msg.age = self.count % 100
        self.pub.publish(msg)
        self.get_logger().info(
            f"Publish: name={msg.name}, age={msg.age}"
        )
        self.count += 1


def main():
    rclpy.init()
    node = PersonPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

