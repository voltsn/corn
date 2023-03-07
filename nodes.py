from dataclasses import dataclass
from enum import Enum

class ElementData:
    tag_name = str
    attributes = int

class NodeType(Enum):
    text = str
    element = ElementData

@dataclass
class Node:
    childern: []
    node_type: NodeType


