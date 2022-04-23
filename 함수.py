#함수

def add(a,b):
    c=a+b
    d=a-b
    return c,d ##여러개의 값을 return가능하다
print(add(3,2))


##소수구하기
def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
        return True
    
    
a=[12,13,7,9,19]
for y in a:
    if isPrime(y):
        print(y,end=' ')
    
    