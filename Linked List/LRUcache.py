class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.members = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)

        self.left.next = self.right
        self.right.previous = self.left

    def insert(self, node):
        recent = self.right.previous
        recent.next = node
        self.right.previous = node
        node.next = self.right
        node.previous = recent
        return

    def remove(self, node):
        future = node.next
        past = node.previous
        past.next = future
        future.previous = past
        return

    def get(self, key: int) -> int:
        if key in self.members.keys():
            self.remove(self.members[key])
            self.insert(self.members[key])
            value = self.members[key].value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.members.keys():
            self.remove(self.members[key])
            self.members[key] = Node(key, value)
            self.insert(self.members[key])
        else:
            self.members[key] = Node(key, value)
            self.insert(self.members[key])

        if len(self.members) > self.capacity:
            del self.members[self.left.next.key]
            self.remove(self.left.next)
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''Commentary:
In order to keep track of the Least Recent Used item, we use a linked list. This allows get and put operations in 
constant time. '''