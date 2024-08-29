Submission 1 - https://www.onlinegdb.com/Qb7FVgiXR

```python
'''
Lab2 Submission 1
By Pratham Gupta and Gavish Bansal and Krishna Aggarwal (Team work)
Pratham : prathamgupta@iisc.ac.in || Sr no. 23626
Gavish  : gavishbansal@iisc.ac.in || Sr no. 23650
Krishna : krishnaagarw@iisc.ac.in || Sr no. 23755

'''

from heapq import heapify 

x = 10
y = 11
z = 10**2
z = z**0.5

print(f"z is x :{z is x}")

arr = [x,y,z]
print(arr)
print(f"arr[0] is arr[2] : {arr[0] is arr[2]}")
print(f"arr[0] == arr[2] : {arr[0] == arr[2]}")
print(f"arr[0] is z : {arr[0] is z}")
print(f"arr[2] is x : {arr[2] is x}")
print(f"arr[0] is x : {arr[0] is x}")
print(f"arr[2] is z : {arr[2] is z}")


heapify(arr)

print(arr)
print(f"arr[0] is arr[2] : {arr[0] is arr[2]}")
print(f"arr[0] == arr[2] : {arr[0] == arr[2]}")
print(f"arr[0] is z : {arr[0] is z}")
print(f"arr[2] is x : {arr[2] is x}")
print(f"arr[0] is x : {arr[0] is x}")
print(f"arr[2] is z : {arr[2] is z}")

# x was initially ancestor of z but after heapify z has become ancestor of x
# so the heapify function is not working stably 

print("Case failed for x and z")
```

---
Submission 2 - https://onlinegdb.com/-yj1c3YQz

```python


'''
Lab2 Submission 2
By Pratham Gupta and Gavish Bansal and Krishna Aggarwal (Team work)
Pratham : prathamgupta@iisc.ac.in || Sr no. 23626
Gavish  : gavishbansal@iisc.ac.in || Sr no. 23650
Krishna : krishnaagarw@iisc.ac.in || Sr no. 23755

'''

from heapq import heapify as _helper_heapify

def heapify(arr:list) -> None:
    '''
    arr : list of integers/floats/etc 
    The function will heapify the list in place making it a min heap
    heapification will be stable
    '''
    heap_indexing_table = {}
    n = len(arr)
    for i in range(n):
        ele = arr[i]
        if(ele not in heap_indexing_table):
            heap_indexing_table[ele] = [[],0]
        heap_indexing_table[ele][0].append(i)
    dup_arr = arr[:]
    _helper_heapify(dup_arr)
    for i in range(n):
        ele = dup_arr[i]
        original_index = heap_indexing_table[ele][0][heap_indexing_table[ele][1]]
        heap_indexing_table[ele][1] += 1
        dup_arr[i] = arr[original_index]

    for i in range(n):
        arr[i] = dup_arr[i]
    return
```
