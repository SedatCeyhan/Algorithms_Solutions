# class DoublyLinkedNode():
#     def __init__(self, key = -1, val = -1, prev=None, next=None):
#         self.val = val
#         self.key = key
#         self.prev = prev
#         self.next = next
#
#
# class LRUCache(object):
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {}
#         self.head, self.tail = DoublyLinkedNode(), DoublyLinkedNode()
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     def pushToTop(self, node):
#         node.prev = self.head
#         node.next = self.head.next
#
#         self.head.next.prev = node
#         self.head.next = node
#
#
#     def removeNode(self, node):
#         node.next.prev = node.prev
#         node.prev.next = node.next
#
#     def get(self, key):
#         if key not in self.cache:
#             return -1
#         self.removeNode(self.cache[key])
#         self.pushToTop(self.cache[key])
#         return self.cache[key].val
#
#
#     def put(self, key, value):
#         if key not in self.cache:
#             newNode = DoublyLinkedNode(key, value, self.head, self.head.next)
#             self.cache[key] = newNode
#             self.pushToTop(newNode)
#
#             if len(self.cache.keys()) > self.capacity:
#                 nodeToDelete = self.tail.prev
#                 self.removeNode(nodeToDelete)
#                 self.cache.pop(nodeToDelete.key)
#
#         else:
#             modifiedNode = self.cache[key]
#             modifiedNode.val = value
#             self.removeNode(modifiedNode)
#             self.pushToTop(modifiedNode)
#
#
#
#
#
#
#
# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)

class DoublyLinkedNode:
    def __init__(self, key=-1, value=-1, prev = None, next = None):
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
            node = DoublyLinkedNode(key,value)
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





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)