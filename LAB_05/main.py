from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value = None, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


    def __repr__(self):
        return str(self.value)


    def is_leaf(self):
        if self.left_child == None and self.left_child == None:
            return True
        return False


    def add_left_child(self, value):
        self.left_child = BinaryNode(value)


    def add_right_child(self, value):
        self.right_child = BinaryNode(value)


    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child != None:
            self.right_child.traverse_in_order(visit)



    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_post_order(visit)
        if self.right_child != None:
            self.right_child.traverse_post_order(visit)
        visit(self)



    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)



    def show(self, temp=0):
        if self.right_child != None:
            self.right_child.show(temp + 1)
        print('   ' * temp , self.value)
        if self.left_child != None:
            self.left_child.show(temp + 1)





class BinaryTree:
    root: BinaryNode


    def __init__(self, value):
        self.root=BinaryNode(value)


    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)



    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)



    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)



    def show(self):
        self.root.show()




n1 = BinaryNode(10)

n1.add_left_child(9)
n1.left_child.add_left_child(1)
n1.left_child.add_right_child(3)
n1.add_right_child(2)
n1.right_child.add_left_child(4)
n1.right_child.add_right_child(6)
#print(n1.left_child.right_child)

n1.traverse_in_order(print)


print()

binary_tree = BinaryTree(10)
binary_tree.root.add_left_child(9)
binary_tree.root.left_child.add_left_child(1)
binary_tree.root.left_child.add_right_child(3)
binary_tree.root.add_right_child(2)
binary_tree.root.right_child.add_left_child(4)
binary_tree.root.right_child.add_right_child(6)


binary_tree.traverse_post_order(print)
binary_tree.show()


assert binary_tree.root.value == 10

assert binary_tree.root.right_child.value == 2
assert binary_tree.root.right_child.is_leaf() is False

assert binary_tree.root.left_child.left_child.value == 1
assert binary_tree.root.left_child.left_child.is_leaf() is True


binary_tree.traverse_post_order(print)