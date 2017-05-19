##

class SingleListNode:
    def __init__(self, val, next=None):
        self.val = val 
        self.next = next 

    def insert(self, val):
        p = self.next
        self.next = SingleListNode(val, p)
        return self.next

    def __iter__(self):
        p = self
        while p is not None:
            yield p.val
            p = p.next

    def reverse(self, phead=None):
        p = self
        while p is not None:
            tmp = p.next
            p.next = phead
            phead = p
            p = tmp
        return phead

        

class DoubleListNode(SingleListNode):
    def __init__(self, val, next=None, prev=None):
        self.val = val 
        self.next = next 
        self.prev = prev 

    def insert(self, val):
        p = self.next
        self.next = DoubleListNode(val, next=p, prev=self)
        if p is not None: p.prev = self.next
        return self.next

    def insert_head(self, val):
        prev = self.prev
        self.prev = DoubleListNode(val, next=self, prev=prev)
        if prev is not None: prev.next = self.prev
        return self.prev

    def remove(self):
        next = self.next
        prev = self.prev
        if next is not None: next.prev = prev
        if prev is not None: prev.next = next

##
class CircularQueue:
    def __init__(self):
        self.last = None
        self.size = 0

    def enqueue(self, val):
        if self.last is None:
            self.last = SingleListNode(val)
            self.last.next = self.last
        else:
            self.last.next = SingleListNode(val, self.last.next)
            self.last = self.last.next
        self.size += 1

    def dequeue(self):
        if self.last is None: return None 
        self.size -= 1
        if self.last.next == self.last: 
            val = self.last.val
            self.last.next = None
            self.last = None
            return val
        head = self.last.next 
        val = head.val
        self.last.next = head.next
        return val

    
    def __iter__(self):
        return iter(self.last)

    def __repr__(self):
        vals = []
        if self.last is None: return repr(vals)
        p = self.last.next
        while p is not None:
            vals.append(p.val)
            if p == self.last: break
            p = p.next
        return repr(vals)
    
    def __len__(self):
        return self.size
##

class Buffer:
    def __init__(self):
        from collections import deque
        self.left = deque()
        self.right = deque()
    
    def insert(self, char):
        self.left.append(char)

    def get(self):
        if not self.left: return None
        return self.left[-1]

    def delete(self):
        if not self.left: return None
        return self.left.pop()

    def left(self, step):
        try: 
            for _ in range(step): self.right.append(self.left.pop())
        except IndexError: pass

    def right(self, step):
        try:
            for _ in range(step): self.left.append(self.right.pop())
        except IndexError: pass

    def __len__(self):
        return len(self.left) + len(self.right)

##
class StackPermutationChecker:
    def __init__(self, N):
        self.N = N

    def check(self, perms):
        from collections import deque
        nums = deque()
        used = -1
        for v in perms:
            while not nums or v > nums[-1]:
                used += 1
                nums.append(used)
            if v != nums[-1]: return False
            nums.pop()
        return True
##
class JosephusChecker(CircularQueue):
    def __init__(self, M, N):
        super().__init__()
        self.M = M
        self.N = N

    def elimination(self):
        for v in range(self.N): self.enqueue(v)
        while self:
            self.rotate(self.M-1)
            yield self.dequeue()


    def rotate(self, step):
        if self.last is None: return
        for _ in range(step): self.last = self.last.next

##
class GeneralizedQueue(CircularQueue):
    def __init__(self):
        super().__init__()

    def rotate(self, step):
        if self.last is None: return
        p = self.last
        for _ in range(step-1): p = p.next
        return p

    def insert(self, val):
        self.enqueue(val)

    def delete(self, k):
        if k == 1: return self.dequeue()
        p = self.rotate(k - 1)
        val = p.next.val
        p.next = p.next.next
        self.size -= 1
        return val
##



