from nodes import Type

def print_node(node):
    obj_attrs = node.__dict__

    output = ""
    for key in obj_attrs:
        output += f"-- {key} : {obj_attrs[key]}\n" 
        if key == "children":
            for val in obj_attrs[key]:
                output += f"  -- {val}\n"
        elif key == "attributes":
            for attr_key in obj_attrs[key]:
                output += f"-- {attr_key}"

    print(output)

