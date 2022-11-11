import hashlib
import sys
from typing import Union


class MerkleNode:
    def __init__(self, val: str, child_1: Union['MerkleNode', None], child_2: Union['MerkleNode', None]) -> None:
        self.value = val
        self.child_1 = child_1
        self.child_2 = child_2


if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} <elem_1> <elem_2> ... <elem_n>")
    exit(0)

blocks = sys.argv[1:]
hashed_blocks = [hashlib.md5(elem.encode()).hexdigest() for elem in blocks]

merkle_nodes = []
for i in range(len(hashed_blocks)):
    leaf = MerkleNode(hashed_blocks[i], None, None)
    merkle_nodes.append(leaf)

new_merkle_nodes = merkle_nodes.copy()
while len(merkle_nodes) > 1:
    new_merkle_nodes = []

    for i in range(0, len(merkle_nodes), 2):
        idx = i+1 if (i != len(merkle_nodes) - 1) else i

        s = (merkle_nodes[i].value + merkle_nodes[idx].value).encode()
        val = hashlib.md5(s).hexdigest()
        node = MerkleNode(val, merkle_nodes[i], merkle_nodes[idx])
        new_merkle_nodes.append(node)

    merkle_nodes = new_merkle_nodes.copy()


merkle_root = merkle_nodes[0]
print(merkle_root.value)