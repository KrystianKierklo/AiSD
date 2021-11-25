from typing import Any, List

class TreeNode:
    value: Any
    children: List['TreeNode']


    def __init__(self, value=Any):
        self.value = value
        self.children = list()


    def is_leaf(self):
        if self.children==[]:
            return True
        return False


    def add(self, child: 'TreeNode'):
        self.children.append(child)


    def for_each_deep_first(self, visit):
        visit(self)
        if self.children == []:
            return "Jest puste"
        else:
            for child in self.children:
                child.for_each_deep_first(visit)


    def for_each_level_order(self, visit):
        visit(self)
        temp_fifo = queue.Queue()
        while temp_fifo.empty() == 0:
            temp = temp_fifo.get()
            visit(temp)
            for child in temp.children:
                temp_fifo.put(child)


    def search(self, value):
        if self.value == value:
            return True
        for node in self.children:
            if node.search(value):
                return True
        else:
            return False


    def __repr__(self):
        return self.value




class Tree:
    root: TreeNode


    def __init__(self):
        self.root = root


    def add(self, value, parent_name):
        temp = queue.Queue()
        added_node = self.root
        if self.root.value == parent_name:
            self.root.add(TreeNode(value))
        else:
            for child in node.children:
                temp.pu(child)
        while(temp.empty() != 1):
            temp2 = temp.get()
            if temp2.value == parent_name:
                temp2.add(TreeNode(value))
            else:
                for child in temp2.children:
                    temp.put(child)



    def for_each_level_order(self, visit):
        self.root.for_each_level_order(visit)


    def for_each_deep_first(self, visit):
        self.root.for_each_deep_first(visit)





n1 = TreeNode("A")
n2 = TreeNode("B")
n3 = TreeNode("C")

n1.add(n2)

print(n1.__repr__())
print(n1.children)