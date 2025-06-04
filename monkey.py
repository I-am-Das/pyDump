def cal(ht,up,down):
    m=0
    climb=0
    while True:
        m=m+1
        climb+=up
        if climb>=ht:
            print("The monkey climbs up{} in {}".format(up,m))
            return 
        climb-=down
        if down>0 and up<ht:
            m+=1
cal(30,10,5)
cal(21,5,3)
