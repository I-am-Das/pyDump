class sim:
    comp="DAS"
    def dim(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d 
        self.e=0 
        self.f=0
    def tax(self):
        self.e= self.c*.10
    def share(self):
        self.f=self.c*.10
    def disp(self):
        self.tax()
        self.share()
        print("NAME:{} ".format(self.a))
        print("AGE: {}".format(self.b))
        print("COMPANY NAME:",sim.comp)
        print("SALARY: {}".format(self.c))
        print("tax to pay:{}".format(self.e))
        print("Share:{}".format(self.f))
s=sim()
d=sim()
s.a="DAS"
d.a="ARJUN"
s.b=21
d.b=22
s.c=50000
d.c=40000
s.disp()
print("-------------------------")
d.disp()
 
