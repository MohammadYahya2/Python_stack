import random
def randInt(min=0   , max=100 ):
    if min > max:
        min, max = max, min  
    return round(random.random() * (max - min) + min)
print(randInt())
print(randInt(max=50)) 
print(randInt(min=50, max=500))   

