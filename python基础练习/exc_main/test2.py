
import time
begin=time.time()
print(begin)
def fun(nums,target):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
           if nums[i]+nums[j]==target:
              return [i,j]


def twoSum(nums,target):
    hashmap={}
    for index,num in enumerate(nums):
        print(index,num)
        hashmap[num]=index
    for i,num in enumerate(nums):
        j=hashmap.get(target-num)
        if j is not None and i!=j:
            return [i,j]

def twoSum1(nums,target):
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target-num) is not None:
            print(hashmap.get(target-num))
            return [i,hashmap.get(target-num)]
        hashmap[num] =i
    print(hashmap)
#
# 0 7  9-7=2
# 1 3
# 2 1
# 3 2
# 4 5
# 5 2
# 6 9
# hashmap[7]=0
# hashmap[3]=1



nums = [7, 3, 1, 2,5,2,9]
target = 9
# print(fun(nums, target))
# print(twoSum(nums, target))
print(twoSum1(nums, target))

end=time.time()
print(end)





# dict={}
# dict.get()

# def sort(array):
#     list0 = []
#     while len(array) > 0:
#      min0 = min(array)
#      list0.append(min0)
#      array.pop(min0)
#     return list0
#
# def min(arry):
#     list1 = sort(arry)
#     print(list1)

x=min([24, 9, 38, 110, 315, 4, 44, 238, 6, 35, 90])
list=[24, 9, 38, 110, 315, 4, 44, 238, 6, 35, 90]
print(list.pop(x))