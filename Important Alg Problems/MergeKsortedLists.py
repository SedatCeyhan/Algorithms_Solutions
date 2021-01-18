from queue import PriorityQueue
from collections import defaultdict

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        if not lists: return None

        def merge2Linked(node1, node2):
            head = curr = ListNode(-1)

            while node1 and node2:
                if node1.val < node2.val:
                    curr.next = ListNode(node1.val)
                    curr = curr.next
                    node1 = node1.next

                elif node2.val < node1.val:
                    curr.next = ListNode(node2.val)
                    curr = curr.next
                    node2 = node2.next

                else:
                    curr.next = ListNode(node1.val, ListNode(node1.val))
                    curr = curr.next.next
                    node1, node2 = node1.next, node2.next

            if node1: curr.next = node1
            else: curr.next = node2

            return head.next

        while len(lists) > 1:
            temp = []
            i = 0
            while i < len(lists) - 1:
                temp.append(merge2Linked(lists[i], lists[i + 1]))
                i += 2
            if i == len(lists) - 1: temp.append(lists[-1])
            lists = temp


        return lists[0]




class Solution2:
    def mergeKLists(self, lists):
        if not lists: return None
        pq = PriorityQueue()
        map = defaultdict(list)
        for node in lists:
            pq.put(node.val)
            map[node.val].append(node)

        head = curr = ListNode(-1)
        while not pq.empty():
            minVal = pq.get()
            minNode = map[minVal][0]
            curr.next = ListNode(minVal)
            curr = curr.next
            map[minVal] = map[minVal][1:]

            if minNode.next:
                pq.put(minNode.next.val)
                map[minNode.next.val].append(minNode.next)

        return head.next


pq = PriorityQueue()
l = [1,2,1,2,3,3,4,5,5]
