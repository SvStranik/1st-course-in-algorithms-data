def sumList(s1,s2):
    if len(s1) != len(s2): return
    resultat = []
    for i in range(len(s1)):
        resultat.append(s1[i].value + s2[i].value)
    return resultat
  
