#리스트와 내장함수2

a=[23,12,36,53,19]

for x in enumerate(a): #인덱스와 같이 나옴
    print(x)
##(0, 23)
##(1, 12)
##(2, 36)
##(3, 53)
##(4, 19)


for x in enumerate(a):
    print(x[0],x[1]) #a의 값을 () 없이 바로빼옴


for index,value in enumerate(a): #위와같이 ()제거하고 사용
    print(index,value)     #바로위의 로직보다 결과가같지만 많이사용




#튜플 : 리스트와 달리, 튜플은 값 수정이 불가능하다 
b=(1,2,3,4,5)
print(b[0]) # // 1



