d_lis=[]
d_rec=int(input('How many numbers do you want to enter?: '))

i = 0
while i<d_rec:
    num=int(input('Enter a whole digit: '))
    d_lis.append(num)
    i+=1

d_ser=input('Would you like to multiply(m) or divide(d)?')

#for number in d_lis:

mul = 1
div = 1
if d_ser.lower()=='m':
    for x in d_lis:
        mul *= x
    print(mul)
elif d_ser.lower()=='d':
    for x in d_lis:
        div /= x
    print(div)
else:
        print('Option unavalable')

 
print(d_lis)

