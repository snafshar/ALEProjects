def binary_search(values,target):
    low,high,comparisons=0,len(values)-1,0
    while low<=high:
        middle=(low+high)//2; comparisons+=1
        if values[middle]==target:return middle,comparisons
        if values[middle]<target:low=middle+1
        else:high=middle-1
    return -1,comparisons
if __name__=='__main__':print(binary_search([1,2,3,4,5],4))