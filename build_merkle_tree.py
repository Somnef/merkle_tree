import hashlib
import sys
import pickle
from MerkleNode import MerkleNode

def make_merkle_tree(blocks: list[str]):
    """
    Makes the merkel tree based on the initial blocks of data.
    returns: root of the tree
    """
    hashed_blocks = [hashlib.md5(elem.encode()).hexdigest() for elem in blocks]

    merkle_nodes = []
    for i in range(len(hashed_blocks)):
        leaf = MerkleNode(None, None, hashed_blocks[i])
        merkle_nodes.append(leaf)

    new_merkle_nodes = merkle_nodes.copy()
    while len(merkle_nodes) > 1:
        new_merkle_nodes = []
        for i in range(0, len(merkle_nodes), 2):
            idx = i+1 if (i != len(merkle_nodes) - 1) else i

            node = MerkleNode(merkle_nodes[i], merkle_nodes[idx])
            new_merkle_nodes.append(node)
        merkle_nodes = new_merkle_nodes.copy()

    return merkle_nodes[0]


if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} <elem_1> <elem_2> ... <elem_n>")
    exit(0)

blocks = sys.argv[1:]
merkle_root = make_merkle_tree(blocks=blocks)

merkle_root.print_tree()
with open("tree.pkl", "wb") as f:
    pickle.dump(merkle_root, f)