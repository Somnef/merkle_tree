import hashlib
import sys

def md5_list(l):
    return [hashlib.md5(elem.encode()).hexdigest() for elem in l]


def pair_concat(l):
    new_l = []
    for i in range(0, len(l), 2):
        if i != len(l) - 1:
            new_l.append(l[i] + l[i+1])
        else:
            new_l.append(l[i] + l[i])

    return new_l


if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} <elem_1> <elem_2> ... <elem_n>")
    exit(0)

blocks = sys.argv[1:]
hashed_blocks = md5_list(blocks)

while len(blocks) > 1:
    blocks = pair_concat(hashed_blocks)
    hashed_blocks = md5_list(blocks)

root = hashed_blocks[0]
print(root)