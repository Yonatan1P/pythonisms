from codefellows.dsa.binary_tree import BinaryTree
import string

class IterableBinaryTree(BinaryTree):

    def __iter__(self):

        def value_generator():

            def walk(root):

                if not root:
                    return None

                yield root.value
                
                yield from walk(root.left)

                yield from walk(root.right)

            return walk(self.root)

        return value_generator()
        