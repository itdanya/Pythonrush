class min:
    def forr(a, b, c, d): 
        if ((a <= b) and (a <= c) and (a <= d)):
            print(a)
        elif ((b <= a) and (b <= c) and (b <= d)):
            print(b)
        elif ((c <= a) and (c <= b) and (c <= d)):
            print(c)
        else:
            print(d)

    def two(a, b): 
        if (a <= b):
            print(a)
        else: 
            print(b) 

min.two(-20, -10)
min.forr(-40, -10, -30, 40)
min.forr(-20, -40, -30, 40)
min.forr(-20, -10, -40, 40)
min.forr(-20, -10, -30, -40)