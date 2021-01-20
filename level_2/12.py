def min(a, b, c):
    if ((a <= b) and (a <= c)): 
        return a; 
    elif ((b <= a) and (b <= c)): 
        return b; 
    elif ((c < a) and (c < b)): 
        return c; 
 
print(min(1, 2, 3))
print(min(-1, -2, -3))
print(min(3, 5, 3))
print(min(5, 5, 10))