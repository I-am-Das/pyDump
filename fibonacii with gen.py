def gen_fibo(x):
    a,b=0,1
    for i in range(x):
        yield a
        a,b=b,a+b
c=int(input())
for i in gen_fibo(c):
    print(i,end=' ')
