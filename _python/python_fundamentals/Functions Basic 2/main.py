#1Countdown
def countDown(n):
    countDownList = []
    for i in range(n,-1,-1):
        countDownList.append(i)
    print(countDownList)
countDown(10)

#2Print and Return
def printandReturn(list):
    print(list[0])
    return list[1]
y = printandReturn([1,2])
print(y)

#3First Plus Length
def firstPlusLength (list):
    return list[0]+len(list)
y = firstPlusLength([5,6,7,8,9,10])
print(y)

#4Values Greater than Second
def valuesGreaterthanSecond(list):
    list1 = []
    list_second_value = list[1]
    for n in range(len(list)):
        if(n > list_second_value):
            list1.append(n)
    return list1
y = valuesGreaterthanSecond([5,2,3,2,1,4])
print(y)

#5This Length, That Value
def thisLengthThatValue(size, value):
    return([value]*size)
y = thisLengthThatValue(5,3)
print(y)