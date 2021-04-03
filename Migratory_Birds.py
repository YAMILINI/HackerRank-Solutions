# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr.sort()  
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for k,v in count.items():
        if v == max(count.values()):
            return k
