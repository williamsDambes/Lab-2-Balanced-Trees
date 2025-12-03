{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "ae1c5fd0-cee5-44c0-8bcd-c36aa7bb5176",
      "cell_type": "code",
      "source": "import matplotlib.pyplot as plt\nimport random\nimport math\n\n# Colors\nRED = True\nBLACK = False\n\nclass RBNode:\n    def __init__(self, key, color=RED, parent=None, left=None, right=None):\n        self.key = key\n        self.color = color\n        self.left = left\n        self.right = right\n        self.parent = parent\n\nclass RedBlackTree:\n    def __init__(self):\n        self.TNULL = RBNode(0, color=BLACK) # Sentinel node (replaces None)\n        self.root = self.TNULL\n\n    def insert(self, key):\n        # Standard BST Insert first\n        node = RBNode(key, color=RED, parent=None, left=self.TNULL, right=self.TNULL)\n        parent = None\n        curr = self.root\n\n        while curr != self.TNULL:\n            parent = curr\n            if node.key < curr.key:\n                curr = curr.left\n            else:\n                curr = curr.right\n        \n        node.parent = parent\n        if parent is None:\n            self.root = node\n        elif node.key < parent.key:\n            parent.left = node\n        else:\n            parent.right = node\n        \n        # Fix violations\n        if node.parent is None:\n            node.color = BLACK\n            return\n\n        if node.parent.parent is None:\n            return\n\n        self._fix_insert(node)\n\n    def _fix_insert(self, k):\n        while k.parent.color == RED:\n            if k.parent == k.parent.parent.right:\n                u = k.parent.parent.left # Uncle\n                if u.color == RED:\n                    u.color = BLACK\n                    k.parent.color = BLACK\n                    k.parent.parent.color = RED\n                    k = k.parent.parent\n                else:\n                    if k == k.parent.left:\n                        k = k.parent\n                        self._right_rotate(k)\n                    k.parent.color = BLACK\n                    k.parent.parent.color = RED\n                    self._left_rotate(k.parent.parent)\n            else:\n                u = k.parent.parent.right # Uncle\n                if u.color == RED:\n                    u.color = BLACK\n                    k.parent.color = BLACK\n                    k.parent.parent.color = RED\n                    k = k.parent.parent\n                else:\n                    if k == k.parent.right:\n                        k = k.parent\n                        self._left_rotate(k)\n                    k.parent.color = BLACK\n                    k.parent.parent.color = RED\n                    self._right_rotate(k.parent.parent)\n            if k == self.root:\n                break\n        self.root.color = BLACK\n\n    def _left_rotate(self, x):\n        y = x.right\n        x.right = y.left\n        if y.left != self.TNULL:\n            y.left.parent = x\n        y.parent = x.parent\n        if x.parent is None:\n            self.root = y\n        elif x == x.parent.left:\n            x.parent.left = y\n        else:\n            x.parent.right = y\n        y.left = x\n        x.parent = y\n\n    def _right_rotate(self, x):\n        y = x.left\n        x.left = y.right\n        if y.right != self.TNULL:\n            y.right.parent = x\n        y.parent = x.parent\n        if x.parent is None:\n            self.root = y\n        elif x == x.parent.right:\n            x.parent.right = y\n        else:\n            x.parent.left = y\n        y.right = x\n        x.parent = y\n\n    # Helper to calculate height (black nodes or total height)\n    def get_height(self, node):\n        if node == self.TNULL:\n            return 0\n        return 1 + max(self.get_height(node.left), self.get_height(node.right))",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 4
    },
    {
      "id": "4991ebb7-07ae-4a52-a17d-cf59764d92a2",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}
