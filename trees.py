class Node(object):

    def __init__(self, data):
        """
        Initialize a node in a binary tree
        """
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        """
        Insert a value into a binary tree node
        """
        # check if the value is less than the node data
        if value < self.data:
            # if so, check if the left node contains a value
            if self.left:
                # if so, insert the value to the left of the node
                self.left.insert(value)
            else:
                # if not, the value becomes the left node's data
                self.left = Node(value)
        else:
            # if the value is greater than the node data
            # begin by checking if the right node contains a value
            if self.right:
                # if so, insert the value to the right of the node
                self.right.insert(value)
            else:
                # if not, the value becomes the right node's data
                self.right = Node(value)

    def contains(self, value):
        """
        Check if a binary tree node contains a certain value
        Returns a boolean
        """
        # check if the value is equal to the node's data
        if value == self.data:
            # if so, the tree contains the value
            return True
        else:
            # if not, check if the value is less than the node's data
            if value < self.data:
                # if so, check if it has a left node
                if self.left is None:
                    # if not, the tree does not contain the value
                    return False
                else:
                    # if so, recursively check whether any of
                    # the left nodes contain the value
                    left_node = Node(self.left)
                    return left_node.contains(value)
            else:
                # if value is greater than node's data,
                # check if it has a right node
                if self.right is None:
                    # if not, the tree does not contain the value
                    return False
                else:
                    # if so, recursively check whether any of
                    # the right nodes contain the value
                    right_node = Node(self.right)
                    return right_node.contains(value)

    def print_inorder(self):
        """
        Inorder traversal of a binary tree
        """
        # first print left node
        if self.left:
            left_node = Node(self.left)
            left_node.print_inorder()
        # then print root
        print self.data
        # then print right node
        if self.right:
            right_node = Node(self.right)
            right_node.print_inorder()

    def print_preorder(self):
        """
        Preorder traversal of a binary tree
        """
        # first print root
        print self.data
        # then print left node
        if self.left:
            left_node = Node(self.left)
            left_node.print_inorder()
        # then print right node
        if self.right:
            right_node = Node(self.right)
            right_node.print_inorder()

    def print_postorder(self):
        """
        Postorder traversal of a binary tree
        """
        # first print left node
        if self.left:
            left_node = Node(self.left)
            left_node.print_inorder()
        # then print right node
        if self.right:
            right_node = Node(self.right)
            right_node.print_inorder()
        # then print root
        print self.data
