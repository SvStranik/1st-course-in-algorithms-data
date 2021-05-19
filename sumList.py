def sumList(s1,s2):
    if s1.len() == s2.len() and s1.len() >= 1: 
        s3 = LinkedList()
        node,node2 = s1.head,s2.head
        while node:
            per = node.value + node2.value
            s3.add_in_tail(Node(per))
            node,node2 = node.next,node2.next
        return s3   
    return None
