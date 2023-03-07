from enum import Enum

class Type(Enum):
    ELEMENT = 1
    ATTRIBUTE_NODE = 2
    TEXT = 3

class Node:
    node_type: Type
    children: list

    def __init__(self, node_type: Type, children: list):
        self.node_type = node_type
        self.children = children

class Text_node(Node):
    data: str

    def __init__(self, data: str):
        self.data = data
        super().__init__(Type.TEXT.name, [])

class Element_node(Node):
   tag_name: str
   attributes: dict[str, str]

   def __init__(self, name: str, attr: dict[str, str]):
       super().__init__(Type.ELEMENT.name, [])

       self.tag_name = name
       self.attributes = attr
       
def create_text_node(text: str) -> Node:
    return Text_node(text)

def create_element_node(name: str, attrs: dict[str, str]) -> Node:
    return Element_node(name, attrs)



