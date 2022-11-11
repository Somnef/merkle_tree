# Merkle Tree

Simple implementation of a Merkle Tree construction algorithm for my blockchain homework.

Usage: python merkle_tree.py \<elem_1\> \<elem_2\> ... \<elem_n\>

Example:
```
> python build_merkle_tree.py a b c d
'dfbd34a5b6634d7ccd0aa26a4dec2ecc'
        '3bc22fb7aaebe9c8c5d7de312b876bb8'
                '0cc175b9c0f1b6a831c399e269772661'
                '92eb5ffee6ae2fec3ad71c777531578f'
        '1ee715fcc373a83611d163d9d4ea02a3'
                '4a8a08f09d37b73795649038408b5f33'
                '8277e0910d750195b448797616e091ad'
```
