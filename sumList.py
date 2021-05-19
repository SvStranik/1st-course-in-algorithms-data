def sumList(s1,s2):
    if len(s1) == len(s2) and len(s1) >= 1:
        node1, node2= s1[0],s2[0]
        resultat = []
        while node1:
            resultat.append(node1.value + node2.value)
            node1, node2 = node1.next,node2.next  
        return resultat
    return []
