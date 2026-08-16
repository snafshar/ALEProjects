def merge_sort(values):
    if len(values)<=1:return values[:]
    middle=len(values)//2; left=merge_sort(values[:middle]); right=merge_sort(values[middle:]); result=[]
    while left and right: result.append((left if left[0]<=right[0] else right).pop(0))
    return result+left+right
if __name__=='__main__':print(merge_sort([5,1,4,2,3]))