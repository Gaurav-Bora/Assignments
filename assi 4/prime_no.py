#reversing number
def reversing(num):
    reverse = 0
    while num != 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse
    
A=int(input('enter first num :'))    
B=int(input('enter second num :  '))    
X = reversing(A)
Y = reversing(B)

#prime condition
for i in range (2,X):
    if X % i == 0 and Y % i == 0 :
        print(A*B)
        break
    elif X % i != 0 or Y % i != 0 :
        print(A+B)
        break
    else:
        print(X+Y)
        break
    


    


    
