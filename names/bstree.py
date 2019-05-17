class BinarySearchTree:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == None:
        self.value = value
        return

    if value < self.value and self.left is None:
      self.left = BinarySearchTree(value)
    elif value >= self.value and self.right is None:
      self.right = BinarySearchTree(value)
    else:
      branch = self.left if value < self.value else self.right
      return branch.insert(value)

  def contains(self, target):
    branch = self.left if target < self.value else self.right
    if self.value == target:
      return True
    elif branch is None:
      return False
    else:
      return branch.contains(target)
