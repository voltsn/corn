def traversDom(node: Node, depth: int = 1) -> None :
    if node == None:
        return

    print_node(node, depth)

    for child in node.children:
        traversDom(child, depth + 1)

    

def print_node(node: Node, depth: int) -> None :
    obj_attrs = node.__dict__

    print("-"*depth, end="")

    if obj_attrs['node_type'] == 'ELEMENT':
        print(obj_attrs['tag_name'])
    else:
        print('#' + obj_attrs['node_type'] + ' ' + obj_attrs['data'])
