from typing import TypeVar, Generic
from enum import Enum

# Define a custom type
Node = TypeVar('Node')

# Define possible types of Node objects
class Node_types(Enum):
    ELEMENT = 1
    ATTRIBUTE_NODE = 2
    TEXT = 3

class Node:
    node_type: Node_types
    children: list

    def __init__(self, node_type: Node_types, children: list):
        self.node_type = node_type
        self.children = children

    def append_child(self, element: Generic[Node]) -> None:
        element.parent_node = self
        self.children.append(element);
    

class Text_node(Node):
    data: str

    def __init__(self, data: str):
        super().__init__(Node_types.TEXT.name, [])
        self.data = data

class Element_node(Node):
   tag_name: str
   attributes: dict[str, str]

   def __init__(self, name: str, attr: dict[str, str]):
       super().__init__(Node_types.ELEMENT.name, [])

       self.tag_name = name
       self.attributes = attr



