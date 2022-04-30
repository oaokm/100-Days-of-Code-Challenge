
def binary_search(arr, item):
    """
    binary_search: is an algorithm for search, and fast.
    arr: Array.
    item: The target.
    """
    #* step 1: main values

    first = 0
    last = len(arr) - 1

    #* step 2: scan about target (item)
    while(first <= last):
        mid = (first + last) // 2
        if arr[mid] == item :
            #* if find a target, return position target (item) with True
          return (True, arr.index(item))
        elif item < arr[mid]:
          last = mid - 1
        else:
            first = mid + 1
    #* if not find a target, return Fales
    return False

#* Array 
array = [1,2,897,45,1451]

#* OUTPUT *#
target = int(input("Enter > "))
print("*"*15)
print(f"\t[Array]\n {array}\n\t[Result]\n{binary_search(array, target)}")
print("*"*15)
