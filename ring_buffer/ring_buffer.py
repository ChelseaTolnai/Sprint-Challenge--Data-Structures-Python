class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity  # Space: O(1)
    self.current = 0  # Space: O(1)
    self.storage = [None]*capacity  # Space: O(k)
    self.length = 0  # Space: O(1)

  def append(self, item):
    self.storage[self.current] = item  # Time: O(1) / Space: O(1)
    self.current += 1  # Time: O(1) / Space: O(1)
    if self.current == self.capacity:  # Time: O(1)
      self.current = 0  # Time: O(1) / Space: O(1)
    if self.length < self.capacity:  # OTime: (1)
      self.length += 1  # Time: O(1) / Space: O(1)

  def get(self):
    return self.storage[:self.length]  # O(k) / O(k)



# buffer = RingBuffer(3)
# print(buffer.get())
# buffer.append('1')
# print(buffer.get())
# print(len(buffer.storage))
# buffer.append('2')
# print(buffer.get())
# print(len(buffer.storage))
# buffer.append('3')
# print(buffer.get())
# print(len(buffer.storage))
# buffer.append('4')
# print(buffer.get())
# print(len(buffer.storage))