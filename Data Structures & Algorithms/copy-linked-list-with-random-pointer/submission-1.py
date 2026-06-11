"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldToCopy = {None: None}

        cur = head# start 
        while cur:
            copy = Node(cur.val) #init a new Node
            oldToCopy[cur] = copy #have old node as Key and New Node as Value
            cur = cur.next #onto next
        
        cur = head#restart
        while cur:
            copy = oldToCopy[cur] #get the New Node
            copy.next = oldToCopy[cur.next] #have New Node's next pointer to the New Node
            copy.random = oldToCopy[cur.random]#update New node's random pointer
            cur = cur.next #move on

        return oldToCopy[head]#return the New head Node
        