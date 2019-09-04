#Improved serach assuming we have an ordered list
#Will be on the final

def search(num,numlist):
        mid = (low + max) // 2
        item = numlist[mid]
        if low > max:
            return -1
        if num == item:
            return mid
        elif num < item:
            max = mid -1
            search(num,numlist,low,max)
        else:
            low = mid + 1

numlist = [23,34,23,45,234,45,56,123,435,4535,123,325,4351,4,6,2,7,8]
numlist.sort()
print(numlist)
for x in numlist:
    search(x,numlist,0,len(numlist)-1)
