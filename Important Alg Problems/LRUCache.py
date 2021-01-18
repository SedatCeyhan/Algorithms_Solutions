class DoublyLinkedNode:
    def __init__(self, key=-1, value=-1, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = DoublyLinkedNode(), DoublyLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def putToTop(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next = node
        node.next.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key not in self.cache: return -1
        node = self.cache[key]
        self.removeNode(node)
        self.putToTop(node)
        return node.val

    def put(self, key, value):
        if key not in self.cache:
            node = DoublyLinkedNode(key, value)
            self.cache[key] = node
            self.putToTop(node)

            if len(self.cache) > self.capacity:
                LRU_node = self.tail.prev
                self.removeNode(LRU_node)
                self.cache.pop(LRU_node.key)
        else:
            node = self.cache[key]
            self.removeNode(node)
            self.putToTop(node)
            node.val = value


