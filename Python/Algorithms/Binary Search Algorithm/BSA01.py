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
array = [1,1451,897,45,2,9]

#* alphabetical order for array & input
a_to_z_array      = sorted(array)
target            = int(input("Enter > "))
output_befor_atoz = binary_search(array, target)
output_after_atoz = binary_search(a_to_z_array, target)

#* OUTPUT *#
print("*"*15)
print(f"\t[Befor Array]\n{array}\n\t[After Array]\n{a_to_z_array}\n\t[Results]\n\t[Befor]\n{output_befor_atoz}\n\t[After]\n{output_after_atoz}")
print("*"*15)
