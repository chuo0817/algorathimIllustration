#coding=utf-8
# 算法图解第一章  二分查找（有序）
# def binary_search(list,item):
#     low = 0;
#     high = len(list) - 1
#
#     while low <= high:
#         mid = (low + high)/2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid -1
#         else:
#             low = mid + 1
#     return None
#
# my_list = [1,3,5,7,9]
# print binary_search(my_list,3)
# print binary_search(my_list,-1)
# 第二章 选择排序
# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1,len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index

# def selecttionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
# print selecttionSort([5,3,6,2,10])
# 第三章 递归
# def countdown(i):
#     print i
#     if i <= 0:
#         return
#     else:
#         countdown(i-1)
# countdown(6)
# 阶乘
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x*fact(x-1)
# print fact(3)
# 第四章 快速排序
# def sum(arr):
#     total = 0
#     for x in arr:
#         total +=x
#     return total
# print sum([1,2,3,4])
# 求和
# def sum(list):
#     if list ==[]:
#         return 0
#     return list[0] + sum(list[1:])
# print sum([4,5,7,8])
# 快速排序
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:]  if i <=pivot ]
#         greater = [i for i in array[1:] if i > pivot ]
#         return quicksort(less) + [pivot] + quicksort(greater)
# print quicksort([10,5,2,3])
# def qsort(list):
#     if not list:
#         return []
#     else:
#         pivot = list[0]
#         less = [x for x in list     if x <  pivot]
#         more = [x for x in list[1:] if x >= pivot]
#         return qsort(less) + [pivot] + qsort(more)
# print qsort([2,3,75,34,1,9])
# 第五章
# book = dict()
# book["apple"] = 0.67
# book["milk"] = 1.49
# print book["milk"]
# 散列表防止重复
voted = {}
def check_voter(name):
    if voted.get(name):
        print "kick them out!"
    else:
        voted[name]=True
        print "let them vote!"
check_voter("mike")
check_voter("mike")
