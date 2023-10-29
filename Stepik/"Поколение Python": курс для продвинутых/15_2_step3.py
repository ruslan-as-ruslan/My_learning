def mean(*args):
    total = 0
    q = 0
    for i in args:
        if type(i) == int or type(i) == float:
            q = q + 1
            total = total + i   
    
    if total == 0: return 0
    
    return total / q  