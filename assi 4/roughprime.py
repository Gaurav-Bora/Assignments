A = int(input('enter number : '))
B = int(input('enter number : '))
X = 0
Y = 0
while A != 0:
    digit = A % 10
    X = X * 10 + digit
    A = A // 10
while B != 0:
    digit = B % 10
    Y = Y * 10 + digit
    B = B // 10


    

    
    if X > 0:
        
        for i in range (2,X):
            if X % i != 0 and Y % i != 0 :
                print(X+Y)
                break
            elif X % i != 0 or Y % i != 0 :
                print(A+B)
                break
            else:
                print(A*B)
                break
            elif X < Y:
                print(A*B)
                
        for i in range (2,Y):
            if X % i != 0 and Y % i != 0 :
                print(X+Y)
                break
            elif X % i != 0 or Y % i != 0 :
                print(A+B)
                break
            else:
                print(A*B)
                    
    
        
    
    

