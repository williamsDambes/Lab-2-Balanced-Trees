# Lab-2-Balanced-Trees
This project implements and compares three types of search trees:
1. Binary Search Tree (BST)
2. AVL Tree (self-balancing)
3. Red-Black Tree (self-balancing)

 Files in the project:
- `bst.ipynb` - Binary Search Tree implementation
- `avl.ipynb` - AVL Tree implementation (extends BST)
- `red_black.ipynb` - Red-Black Tree implementation
- `final experiments.ipynb` - Testing and experiments
- `requirements.txt` - Dependencies

 How to run:

1. Install requirements:
2. Run the experiments:
3. To test individual trees:
```python
from bst import BST
from avl import AVLTree
from red_black import RedBlackTree

# Create and use trees
bst = BST()
bst.insert[10, 5, 15, 3, 7, 12, 18]
print(bst.get_height())
