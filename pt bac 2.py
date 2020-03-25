a=int(input('Nhap a:'))
b=int(input('Nhap b:'))
c=int(input('Nhap c:'))
deltha= b**2-4*a*c
if deltha < 0:
     print('phương trình vô nghiệm')
elif deltha==0:
    print('phương trình có nghiệm kép')
    x=-b/(2*a)
    print('Nghiệm của x là :', x)
else:
    import math
    print('phương trình có 2 nghiệm')
    x1=(-b-(math.sqrt(deltha)))/(2*a)
    x2=(-b+(math.sqrt(deltha)))/(2*a)
    print('Nghiệm của x1 là :',x1)
    print('Nghiệm của x2 là :', x2)


