class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.nodeMap = {}
        self.capacity = capacity
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        # must update dummy -> to this key.
        if key not in self.nodeMap:
            return -1
        else:
            node = self.nodeMap[key]
            self.removeNode(node)
            self.addToFront(node)

            return node.val


    def put(self, key: int, value: int) -> None:
        # key exists or not.
        # create key if not, else update
        # must update dummy -> to this key.
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.removeNode(node)
            self.addToFront(node)
        else:
            newNode = Node(key,value)
            self.nodeMap[key] = newNode
            self.addToFront(newNode)
        
        if len(self.nodeMap) > self.capacity:
            lru = self.right.prev
            self.removeNode(lru)
            del self.nodeMap[lru.key]
    
    def removeNode(self, node: Node) -> None:
        nextNode = node.next
        prevNode = node.prev

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def addToFront(self, node: Node) -> None:
        # update old head
        oldHead = self.left.next
        oldHead.prev = node

        # update head
        self.left.next = node

        # update new node ptrs
        node.prev = self.left
        node.next = oldHead

