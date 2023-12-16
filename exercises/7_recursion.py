def FA(x):
    if x > 2:
        return 7
    else:
        return x - FA(x+1)
    
FA(-2)