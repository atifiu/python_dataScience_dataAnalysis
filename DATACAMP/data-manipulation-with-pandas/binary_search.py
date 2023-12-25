def binary_search(array, array2) -> int:
    for i in range(0, len(array) ):
        print(i)
        element = array[i]
        print(f"element to be searched = {element}")
        left, right = 0, len(array2)
        while left < right:
            
            mid = left + (right - left) // 2
            print(f" left = {left}, right = {right}, mid = {mid}")
            print(f"array2= {array2}")
            if element <= array2[mid]:
                right = mid
            else: #element > array2[mid]:
                left = mid + 1
        array2.insert(left, element)
    print(array2)
    return 0
        
list1 = [1, 4, 6, 7, 10]
list2 = [2, 3,5,8, 9]
binary_search(list1, list2)