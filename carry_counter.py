a = int(input("enter a number"))
b = int(input("enter a number"))
num1 = str(a)[::-1]
num2 = str(b)[::-1]
carry = 0
k = 0
z = min(len(num1), len(num2))
for i in range(z):
    sum = int(num1[i]) + int(num2[i]) + carry
    if sum >= 10:
        k += 1
        carry = 1
    else:
        carry = 0

if len(num1)>z:
    for i in range(z,len(num1)):
        sum=int(num1[i])+carry
        if sum >= 10:
            k += 1
            carry = 1
        else:
            carry = 0
if len(num2)>z:
    for i in range(z,len(num1)):
        sum=int(num2[i])+carry
        if sum >= 10:
            k += 1
            carry = 1
        else:
            carry = 0

print(k)
