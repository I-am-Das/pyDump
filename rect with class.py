class rect():
    def set_dim(self,w,h):
        self.w=w
        self.h=h
    def area(self):
        print(self.w*self.h)
    def peri(self):
        print(self.w+self.h)
l=[]
n=int(input("Enter the number of rectangles:"))
for i in range(n):
    r=rect()
    w=int(input("Enter the width of the rectangle".format(i+1)))
    h=int(input("Enter the height of the rectangle".format(i+1)))
    r.set_dim(w,h)
    l.append(r)
    
for i in range(n):
    print("Rectangle NO{}".format(i+1))
    l[i].area()
    l[i].peri()
    print("---------")
print(i)
