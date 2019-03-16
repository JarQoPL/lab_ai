from treelib import Tree, Node

tree = Tree()
tree.create_node("Harry", "h")  # korzen
tree.create_node("Jane", "j", parent="h")
tree.create_node("Bill", "b", parent="h")
tree.create_node("Diane", "d", parent="j")
tree.create_node("Mary", "m", parent="d")
tree.create_node("Harry", "h2", parent="j")

tree.show()

x = tree.get_node("m")
print(x.tag)
print()
print(x.identifier)
print()
y = tree.parent("m")
print(y.tag)
print()
print(y.identifier)
print()
z = tree.get_node("h2")
print(z.tag)
print()
print(z.is_root())
print()
print(z.is_leaf())
print()
print(tree.paths_to_leaves())
print(tree.parent('h'))


def duplicate_node_path_check(tree, node):

    check_node = tree.get_node(node)
    current_node = check_node
    while tree.parent(current_node.identifier) is not None:
        current_node = tree.parent(current_node.identifier)
        if check_node.tag == current_node.tag:
            return True
    return False


print(duplicate_node_path_check(tree, 'm'))

