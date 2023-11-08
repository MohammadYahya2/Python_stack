def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"

my_list=[1,-5,-7,-9,5]
biggie_size(my_list)
print(my_list)

def count_positives(arr):
   count =0
   for num in arr:
      if num >0:
         count+=1
         if count > 0:
            arr[-1]=count
            return arr
my_list=[1,5,7,8,9,-2]
count_positives(my_list)
print(my_list)
def sum_total(lst):
    total = 0
    for num in lst:
        total += num
    return total

resuelt=sum_total([1,2,3,4])
print(resuelt)
def average(lst):
        total = 0
        for num in lst:
            total += num
        avg = total / len(lst)
        return avg
resulte=average([1,2,3,4])
print(resulte)
def length(lst):
    count = 0
    for j in lst:
        count += 1
    return count
res=length([1,2,3,5])
print(res)


def MIN(lst):
    if not lst:
        return False  
    MIN_value = lst[0]  

    for num in lst:
        if num < MIN_value:
            MIN_value = num

    return MIN_value


res=MIN([1,5,3,4,0,-19])
print(res)


def max(lst):
    if not lst:
        return False  
    max_value = lst[0]  

    for num in lst:
        if num > max_value:
            max_value = num

    return max_value


res=max([1,5,3,4,0,-19])
print(res)
def ultimate_analysis(lst):
    if not lst:
        return False  

    sum_total = sum(lst)
    avg = sum_total / len(lst)
    min_value = min(lst)
    max_value = max(lst)
    length = len(lst)

    result = {
        'sumTotal': sum_total,
        'average': avg,
        'minimum': min_value,
        'maximum': max_value,
        'length': length
    }

    return result
result = ultimate_analysis([37, 2, 1, -9])
print(result)  

def reverse_list(lst):
    lst.reverse()
my_list = [37, 2, 1, -9]
reverse_list(my_list)
print(my_list)  

    
