class sim:
    def add(self):
        return self.a + self.b

    def dis(self):
        print("Hi")


s = sim()
s.a = 10
s.b = 12
print(s.add())
s.dis()


class cal:
    
    def set_(self, r):
        self.r = r

    def circle(self):
        return 3.14 * self.r * self.r


c = cal()
c.set_(10)
print(c.circle())

class simple:
    def set_dim(self,a,b):
        self.a=a
        self.b=b 
    def dis_len(self):
        print(self.a)
    def dis_wid(self):
        print(self.b)
    def cal(self):
        print(self.a*self.b)
r=simple()
r.set_dim(20,30)
r.dis_len()
r.dis_wid()
r.cal()
        
