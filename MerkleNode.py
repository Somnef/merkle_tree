from typing import Union
import hashlib

class MerkleNode:
    def __init__(self, child_1: Union['MerkleNode', None], child_2: Union['MerkleNode', None], val: Union[str, None] = None) -> None:
        self.child_1 = child_1
        self.child_2 = child_2

        if child_1 == None or child_2 == None:
            self.value = val
        else:
            self.value = hashlib.md5((str(child_1.value) + str(child_2.value)).encode()).hexdigest()

    def __str__(self) -> str:
        return f"Left child: {self.child_1 if self.child_1 == None else self.child_1.value}\nRight"\
               f"child: {self.child_2 if self.child_2 == None else self.child_2.value}\n"\
               f"Value: {self.value}"

    def print_tree(self, level=0):
        print('\t' * level + repr(self.value))
        for child in [self.child_1, self.child_2]: 
            if child != None:
                child.print_tree(level+1)