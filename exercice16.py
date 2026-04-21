#1-Given an integer array numbers sorted in non-decreasing order (ascending order), return an 
#array of the squares of each number sorted in non-decreasing order (ascending order). 

#Ex: [-4, -1, 0, 3, 10]   -> [16, 1, 0, 9, 100] 
#Output: [0, 1, 9, 16, 100] 

#Ex: [-7,-3,2,3,11] 
#Output: [4,9,9,49,121] 

#Ex: [1, 2, 3, 4] 
#Output: [1. 4. 9. 16]

array = [1, 2, 3, 4] 

def array_to_sort_asc(a):
    array_cop = []
    for x in a:
        array_cop.append(x * x)

    array_cop.sort() 
    return array_cop

#array_cop = array_to_sort_asc(array) 
#print(f"the new array is : {array_cop}")

# 2-Given a sorted integer array nums, remove the duplicates in-place such that each element appears only, 
# once and return the new length.
# You must modify the array in place without using extra space.

array = [-3,-3,-2,-2,6,8,10]
def no_duplicate(b):
    new_array = []
    for i in b :
        if i not in new_array:
            new_array.append(i)  
    
    return new_array
new_array =  no_duplicate(array) 
print(f" the array clear: {new_array}")
longitud = len(new_array)
print(f" his length is : {longitud}")